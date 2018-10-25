import svgwrite
import random
import os
import yaml

path = os.path.dirname(os.path.abspath(__file__)) + '/img/'

class Board:
  
  # Available patterns
  patterns = ['dog', 'cat', 'crow', 'fish']
  
  def __init__(self, boardWidth, boardHeight, cellSize):
    """Creates a board object.

    :param int boardWidth: Width of the board in px.
    :param int boardHeight: Height of the board in px.
    :param int cellSize: Dimension of the square cells in the board in px.
    :return: Board object
    :rtype: Board
    """
    
    self.boardWidth = boardWidth
    self.boardHeight = boardHeight
    self.cellSize = cellSize
    self.NW = int(boardWidth / cellSize) # Number of cells per line
    self.NH = int(boardHeight / cellSize) # Number of cells per column
    
  def uniform(self):
    return self.patterns[random.randint(0, len(self.patterns) - 1)]
    
  def gen(self, output, skew=False, seed=268656267568):
    """Generate a board picture and saves it in a file.

    :param str output: Name of output file, should end as .svg
    :param bool skew: Indicates if generation of patterns is uniform or skewed
    :param int seed: seed for the PRNG.
    """
    assert(output[-4:] == ".svg")
    random.seed(seed)
    
    # Create drawing
    dwg = svgwrite.Drawing(output, size=(self.boardWidth, self.boardHeight))
    
    # Create the bord with colors and their labels
    for i in range(self.NW):
      for j in range(self.NH):
        
        if skew:
          # Skewed distribution, more of first pattern and less of last
          if random.getrandbits(1):
            pattern = self.patterns[1]
          else:
            pattern = self.uniform()
            if pattern == self.patterns[-1]:
              if random.getrandbits(1):
                pattern = self.patterns[1]
        else:
          # Uniform distribution
          pattern = self.uniform()
        
        # Create cells
        d = self.cellSize // 10
        img = svgwrite.image.Image(path + pattern + '.svg', insert=(i * self.cellSize + d, j * self.cellSize + d), size=(self.cellSize - 2 * d, self.cellSize - 2 * d))
        dwg.add(img)
    
    # Save file
    dwg.save()


# Main

# Read config file
configFilename = "boardConfig.yml"
with open(configFilename, 'r') as stream:
  cfg = yaml.safe_load(stream)
board = Board(cfg['boardWidth'], cfg['boardHeight'], cfg['cellSize'])
board.gen(cfg['output'], skew=cfg['skew'], seed=cfg['seed'])
