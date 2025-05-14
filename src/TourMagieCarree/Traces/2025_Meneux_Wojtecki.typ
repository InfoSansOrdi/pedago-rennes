#set page(
  flipped: true,
  header: align(left)[
    *Carrés Magiques* #h(1fr) 10 mars 2025
    #line(length: 100%)
  ]
)


#set text(size: 20pt) // font: "Fraktur BT")

#set par(justify: true)

#let dotsline() = box(width: 1fr, repeat(" _ "))

#set table(
  fill: (x, y) =>
    if x == 5 or y == 5 { silver },
)


#let show_grid(g, length) = {
  table(
    gutter: 3pt,
    stroke: (x,y) => if x>4 or y>4 {
      (dash: "dashed", thickness: 1pt)
    } else {1pt},
    fill: (i, j) => if g.at(j).at(i) == 1 {black} else {white},
    columns: (length,) * 6,
    rows: (length,) * 6,
  )
}

Dans un carrée de côté 5, on colorie aléatoirement certaines cases (État 1).\
Ensuite, le magicien va venir ajouter une ligne et une colonne sur lesquelles il va colorier des cases pour que chaque ligne et chaque colonne ait #dotsline()\ #dotsline() (État 2).\
Juste après, le magicien se retourne et pendant ce temps là, une personne de modifie une seule case (État 3).

#let size_cell = 17pt

#align(center, grid(
  columns: 3,
  column-gutter: 30pt,
  row-gutter: 10pt,
  align: center + horizon,
  show_grid(
    (
      (1,0,0,1,0,0),
      (1,0,0,1,0,0),
      (0,1,1,0,1,0),
      (0,0,1,0,1,0),
      (1,0,1,1,0,0),
      (0,0,0,0,0,0)
    ), size_cell
  ),
  show_grid(
    (
      (1,0,0,1,0,0),
      (1,0,0,1,0,0),
      (0,1,1,0,1,1),
      (0,0,1,0,1,0),
      (1,0,1,1,0,1),
      (1,1,1,1,0,0)
    ), size_cell
  ),
  show_grid(
    (
      (1,0,0,1,0,0),
      (1,0,0,1,0,0),
      (0,1,1,0,1,1),
      (0,0,1,0,1,0),
      (1,0,0,1,0,1),
      (1,1,1,1,0,0)
    ), size_cell
  ),
  "État 1",
  "État 2",
  "État 3"
))

Finalement, quand le magicien se retourne il peut instantanément dire quelle case a été modifiée. *Comment a-t-il fait ?*\
Il faut trouver la ligne et la colonne qui ont un nombre #dotsline() de cases\
#dotsline() et la case modifiée est celle où la ligne et la colonne se #dotsline().\
Dans l'exemple au dessus, c'est au croisement de la ligne \_ \_ et de la colonne \_ \_.
