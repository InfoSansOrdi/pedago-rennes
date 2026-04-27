#set page("a4", flipped: false, margin: 0.8cm)

#let draw(d, size:1.4cm) = {
  let dp = d.flatten().map(c => {
    if c==0 {
      table.cell(fill: white, v(size))
    } else {
      table.cell(fill: black, v(size))
    }
  })
  
  table(
    columns: (size,)*6,
    inset: 0pt,
    row-gutter: 0pt,
    column-gutter: 0pt,
    stroke: black+1pt,
    ..dp
  )
}


// A imprimer pour chaque binôme, et découper d'une part les vides ensemble, et les remplis individuellement
#let empty = (
  (0,0,0,0,0,0),
  (0,0,0,0,0,0),
  (0,0,0,0,0,0),
  (0,0,0,0,0,0),
  (0,0,0,0,0,0),
  (0,0,0,0,0,0),
)

#let loss = (
  (0,1,0,1,0,0),
  (0,1,0,1,0,1),
  (0,1,0,1,0,1),
  (1,0,1,1,0,0),
  (1,0,1,1,0,0),
  (1,0,1,1,1,1),
)

#let sheep = (
  (0,0,0,0,0,0),
  (1,1,1,1,1,1),
  (1,0,1,1,0,1),
  (1,1,1,1,1,1),
  (0,1,1,0,1,0),
  (0,1,1,0,1,0),
)

#let Quinson = (
  (0,0,1,1,0,0),
  (0,1,0,0,1,0),
  (1,0,0,0,0,1),
  (1,0,0,1,0,1),
  (0,1,0,0,1,0),
  (0,0,1,1,0,1),
)

#align(center,
  grid(
    align: center+horizon,
    row-gutter: 1cm,
    column-gutter: 1cm,
    columns: 2,
    draw(loss),
    draw(loss),
    draw(sheep),
    draw(sheep),
    draw(Quinson),
    draw(Quinson)
  )
)

#pagebreak()
// A imprimer en nombre réduit

#let LWSS = (
  (
    (0,0,0,0,0,0),
    (0,1,0,0,1,0),
    (1,0,0,0,0,0),
    (1,0,0,0,1,0),
    (1,1,1,1,0,0),
    (0,0,0,0,0,0),
  ),
  (
    (0,0,0,0,0,0),
    (0,1,1,0,0,0),
    (1,1,0,1,1,0),
    (0,1,1,1,1,0),
    (0,0,1,1,0,0),
    (0,0,0,0,0,0),
  ),
  (
    (0,0,0,0,0,0),
    (1,1,1,1,0,0),
    (1,0,0,0,1,0),
    (1,0,0,0,0,0),
    (0,1,0,0,1,0),
    (0,0,0,0,0,0),
  ),
)

#align(center,
  grid(
    align: center+horizon,
    row-gutter: 1cm,
    column-gutter: 1cm,
    columns: 2,
    draw(LWSS.at(0)),
    draw(empty),
    draw(LWSS.at(1)),
    draw(empty),
    draw(LWSS.at(2)),
    draw(empty)
  )
)

#pagebreak()

#align(center,
  grid(
    align: center+horizon,
    row-gutter: 1cm,
    column-gutter: 1cm,
    columns: 2,
    draw(empty),
    draw(empty),
    draw(empty),
    draw(empty),
    draw(empty),
    draw(empty)
  )
)

#pagebreak()

// A projeter

#let alternate = (
  (1,0,1,0,1,0),
  (1,0,1,0,1,0),
  (1,0,1,0,1,0),
  (1,0,1,0,1,0),
  (1,0,1,0,1,0),
  (1,0,1,0,1,0),
)

#let emoji = (
  (0,1,0,0,1,0),
  (0,1,0,0,1,0),
  (0,1,0,0,1,0),
  (0,0,0,0,0,0),
  (1,0,0,0,0,1),
  (0,1,1,1,1,0),
)

#let cat = (
  (1,0,0,0,0,1),
  (1,1,1,1,1,1),
  (1,0,1,1,0,1),
  /*(1,1,0,0,1,1),
  (0,1,1,1,1,0),
  (0,0,1,1,0,0),*/
  (0,0,0,0,0,0),
  (0,0,0,0,0,0),
  (0,0,0,0,0,0),
)

#let king = (
  (0,0,0,0,0,0),
  (0,0,0,0,0,0),
  (0,0,0,0,0,0),
  /*(1,0,1,0,1,0),
  (1,1,1,1,1,1),
  (0,1,1,1,1,0),*/
  (0,1,1,1,1,0),
  (0,1,1,1,1,0),
  (0,0,1,1,0,0),
)

#align(center,
  grid(
    align: center+horizon,
    row-gutter: 1cm,
    column-gutter: 1cm,
    columns: 2,
    draw(emoji), // Une image B&W facile
    [
      Gauche: \
      0, 2, 2, 2 \
      1, 4, 1 \
      2, 2, 2 \

      Droite: \
      0, 1, 1, 1, 1, 1, 1 \
      0, 6 \
      1, 4, 1
    ],
    draw(cat),
    draw(king),
    draw(empty), // Court à compresser
    draw(alternate), // Long à compresser
  )
)

