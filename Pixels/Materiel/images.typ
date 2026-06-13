 #let draw(input, size: 1.2cm) = {
   let width = input.at(0).len()
   for i in input {
     assert(i.len() == width)
   }

  let colors = (
    "Y" : (yellow, "sunny.svg"),
    "R" : (red, "fire.svg"),
    "G" : (green, "leaf.svg"),
    "B" : (blue, "water.svg"),
    "P" : (purple, "flower.svg"),
    "W" : (white, none)
  )

   block(breakable: false, table(
      columns: (size,)*width,
      inset: 0pt,
      row-gutter: 0pt,
      column-gutter: 0pt,
      stroke: black+1pt,
      ..input.map(line => {
        line.codepoints().map((c) => {
          let f = colors.at(c)
          table.cell(
            fill: f.at(0),
            if (f.at(1) != none) {
              image(f.at(1), width: size, height: size) 
            } else {
              v(size)
            }
          )
        })
      }).flatten()
      
    ))
}

#let empty(input, size: 1.2cm) = {
  draw(input.map((line) => {
    (("W",)*line.len()).join("")
  }), size:size)
}

#set page("a4", margin: 1.5cm, flipped: false)

#let demos = (
  // Denmark
  (
   "RRWRRR",
   "RRWRRR",
   "WWWWWW",
   "RRWRRR",
   "RRWRRR",
   "RRWRRR"
 ),

 // Benin
 (
   "GGYYY",
   "GGYYY",
   "GGRRR",
   "GGRRR"
 ),

 (
   "WWBWW",
   "WWBWW",
   "BBBBB",
   "WWBWW",
   "WWBWW"
 ), 
)

#grid(
  columns: (1fr, 1fr),
  row-gutter: 1cm,
  column-gutter: 1cm,
  align: center+horizon,
  ..demos.map(draw)
)

#pagebreak()

#set page("a4", flipped: true)

#let empt = (
   "WWWWWWW",
   "WWWWWWW",
   "WWWWWWW",
   "WWWWWWW",
   "WWWWWWW",
   "WWWWWWW",
   "WWWWWWW",
 )

#grid(
  columns: (1fr, 1fr),
  row-gutter: 1cm,
  column-gutter: 1cm,
  align: center+horizon,
  ..range(2).map((_) => { draw(empt)})
)

#set page("a4", margin: 1.5cm, flipped: false)

#pagebreak()

#let firstExemples = (

 // Costa rica
 (
   "BBBBBB",
   "WWWWWW",
   "RRRRRR",
   "RRRRRR",
   "WWWWWW",
   "BBBBBB"
 ),

 // Bahhrein
 (
   "WWRRRR",
   "WWWRRR",
   "WWRRRR",
   "WWWRRR",
   "WWRRRR"
 ),

 // Simili georgie
 (
   "WRWWWBW",
   "RRRWBBB",
   "WRWWWBW",
   "WWWWWWW",
   "WYWWWGW",
   "YYYWGGG",
   "WYWWWGW",
 ),

 // Diagonales
 (
   "RGBYP",
   "GRGBY",
   "BGRGB",
   "YBGRG",
   "PYBGR"
 ),

 // spirale anti-horaire 
 (
   "RGGGGG",
   "RYPPPG",
   "RYWWPG",
   "RYYYYG",
   "RRRRRR"
 ),

 // 1/4
 (
   "RWRWR",
   "WWWWW",
   "RWRWR",
   "WWWWW",
   "RWRWR"
 ),

  // 6 7
 (
   "RRRWPPP",
   "RWWWWWP",
   "RRRWWWP",
   "RWRWWWP",
   "RRRWWWP"
 ),

 // Translation
 (
   "RGBWWW",
   "GBYWWW",
   "PYRWWW",
   "WWWRGB",
   "WWWGBY",
   "WWWPYR",
 ),

 // Rotation
 (
   "RGRWWW",
   "YPGWWW",
   "PGYWWW",
   "WWWPYR",
   "WWWGPG",
   "WWWYGR"
 ),

 // Serpentin RGBYP horraire
 (
   "RGYP",
   "PRGR",
   "YPYG",
   "GRPY"
 )
)

#grid(
  columns: (1fr, 1fr),
  row-gutter: 1cm,
  column-gutter: 1cm,
  align: center+horizon,
  ..firstExemples.map(draw)
)

#pagebreak()

#grid(
  columns: (1fr, 1fr),
  row-gutter: 1cm,
  column-gutter: 1cm,
  align: center+horizon,
  ..firstExemples.map(empty)
)

#pagebreak()

#let race = (
  // Cible
 (
   "RRRRR",
   "RBBBR",
   "RBYBR",
   "RBBBR",
   "RRRRR"
 ),

 // Pyramide
 (
   "WWYWW",
   "WPPPW",
   "GGGGG"
 ),

 // Intertwin
 (
   "YPYPYP",
   "PYPYPY",
   "YPYPYP",
   "PYPYPY"
 ),

 // Un pixel ?
 (
   "RRRRR",
   "RRRRR",
   "RRRGR",
   "RRRRR"
 ),

 // Un T
 (
   "PPPPP",
   "GGPGG",
   "GGPGG",
   "GGPGG",
   "GGPGG"
 ),

 // Patches
 (
   "PYYPPP",
   "PYYPPP",
   "PPPGPP",
   "PPPGPP"
 ),

 // Une croix
 (
   "BYYYYB",
   "YBYYBY",
   "YYBBYY",
   "YYBBYY",
   "YBYYBY",
   "BYYYYB",
 ),

 // Une forme incomplète
 (
   "GGGGGGG",
   "GWWWWWW",
   "GWWWWWW",
   "GWWWWWW",
   "GWWWWWW",
   "GGGGGGG",
 ),

 // Un emoji
 (
   "WRWWRW",
   "WRWWRW",
   "WWWWWW",
   "RWWWWR",
   "WRRRRW"
 ),

 // Le Z
 (
   "PPPPP",
   "GGGPG",
   "GGPGG",
   "GPGGG",
   "PPPPP"
 ),

 // Le losange
 (
   "RRYRR",
   "RYYYR",
   "YYYYY",
   "RYYYR",
   "RRYRR"
 ),

 // De simples colonnes SAUF la dernière ligne en symétrique
 (
   "RYGBP",
   "RYGBP",
   "RYGBP",
   "RYGBP",
   "PBGYR"
 ),

 // Des cadrants
 (
   "RRGG",
   "RRGG",
   "PPYY",
   "PPYY"
 ),

 // Un L à l'envers ?
 (
   "RRR",
   "WWR",
   "WWR",
   "WWR"
 ),

 // ?
 (
   "YWW",
   "WYW",
   "WWY",
   "WYW",
   "YWW"
 ),

 // Une maison ?
 (
   "WWGWW",
   "WGGGW",
   "GGGGG",
   "WGGGW",
   "WGGGW",
 ),

 
)

#grid(
  columns: (1fr, 1fr),
  row-gutter: .5cm,
  column-gutter: .5cm,
  align: center+horizon,
  ..race.map(draw)
)

/*
#pagebreak()
#let empty = (
  "WWWWWWW",
  "WWWWWWW",
  "WWWWWWW",
  "WWWWWWW",
  "WWWWWWW",
  "WWWWWWW",
  "WWWWWWW",
)

#grid(
  columns: (1fr, 1fr),
  row-gutter: .7cm,
  column-gutter: .8cm,
  align: center+horizon,
  ..range(6).map((_) => { draw(empty)})
)
*/
