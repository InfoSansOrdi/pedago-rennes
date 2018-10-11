import svgwrite
import random
import yaml

class Board:
  
  # Available colors: (colorName, label))
  colors = [('red', 'R'), ('green', 'V'), ('blue', 'B'), ('orange', 'O')]

  # Color of line separators
  cellSepColor = '#FFFFFF'
  blockSepColor = '#000000'
  
  def __init__(self, boardSize, cellSize):
    """Creates a board object.

    :param int boardSize: Dimension of the square board in px.
    :param int cellSize: Dimension of the square cells in the board in px.
    :return: Board object
    :rtype: Board
    """
    
    self.boardSize = boardSize
    self.cellSize = cellSize
    self.N = int(boardSize / cellSize) # Number of cells per line/column
    
  def uniform_color(self):
    return self.colors[random.randint(0, len(self.colors) - 1)]
    
  def gen(self, output, skew=False, divide=0, seed=268656267568):
    """Generate a board picture and saves it in a file.

    :param str output: Name of output file, should end as .svg
    :param bool skew: Indicates if generation of colors is uniform or skewed
    :param int divide: number of recursive rounds to display lines
                       for easy cutting with scissors (resulting number of
                       blocks is 4^divide)
    :param int seed: seed for the PRNG.
    """
    assert(output[-4:] == ".svg")
    assert(divide >= 0 and divide < 6) # arbitratry max recursion limit
    assert(self.N % (2 ** divide) == 0)
    random.seed(seed)
    
    # Create drawing
    dwg = svgwrite.Drawing(output, size=(self.boardSize, self.boardSize))
    
    # Create the bord with colors and their labels
    for i in range(self.N):
      for j in range(self.N):
        
        if skew:
          # Skewed distribution, more of first color and less of last
          if random.getrandbits(1):
            color = colors[1]
          else:
            color = self.uniform_color()
            if color == colors[-1]:
              if random.getrandbits(1):
                color = colors[1]
        else:
          # Uniform distribution
          color = self.uniform_color()
        
        # Create squares and text
        rectangle = svgwrite.shapes.Rect(insert=(i * self.cellSize, j * self.cellSize), size=(self.cellSize, self.cellSize), fill=color[0])
        dwg.add(rectangle)
        text = svgwrite.text.Text(color[1], insert=(i * self.cellSize + self.cellSize / 4, j * self.cellSize + 3 * self.cellSize / 4), style='font-size: 12pt; font-family: Ubuntu;')
        dwg.add(text)
  
    # Draw lines between the cells  
    for i in range(self.N):
      line = svgwrite.shapes.Line(start=(0, i * self.cellSize), end=(self.boardSize, i * self.cellSize), stroke=self.cellSepColor)
      dwg.add(line)
    for j in range(self.N):
      line = svgwrite.shapes.Line(start=(j * self.cellSize, 0), end=(j * self.cellSize, self.boardSize), stroke=self.cellSepColor)
      dwg.add(line)

    # Divide part
    def rec(middle, dx, dy, n):
      hline = svgwrite.shapes.Line(start=(dx, dy + middle), end=(dx + middle * 2, dy + middle), stroke=self.blockSepColor)
      dwg.add(hline)
      vline = svgwrite.shapes.Line(start=(dx + middle, dy), end=(dx + middle, dy + middle * 2), stroke=self.blockSepColor)
      dwg.add(vline)
      if n == 1:
        return
      else:
        rec(middle / 2, 0, 0, n - 1)
        rec(middle / 2, 0, middle, n - 1)
        rec(middle / 2, middle, 0, n - 1)
        rec(middle / 2, middle, middle, n - 1)
    rec(int(self.boardSize / 2), 0, 0, divide)
    
    # Save file
    dwg.save()


# Main

# Read config file
configFilename = "boardConfig.yml"
with open(configFilename, 'r') as stream:
  cfg = yaml.safe_load(stream)
board = Board(cfg['boardSize'], cfg['cellSize'])
board.gen(cfg['output'], skew=cfg['skew'], divide=cfg['divide'], seed=cfg['seed'])
