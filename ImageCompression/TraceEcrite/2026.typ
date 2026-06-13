#import "@preview/wrap-it:0.1.1": wrap-content
#set page("a4", flipped: false, margin: 1.5cm)
#set text(14pt)
#set par(justify: true)
#import "../Images/2026.typ": draw

/* #draw((
  (0,0,1,0,0,0),
  (0,1,1,0,0,0),
  (1,1,1,0,0,0),
  /* 
  (0,0,1,0,0,0),
  (1,1,1,1,1,1),
  (0,1,1,1,1,0),
  */
  (0,0,0,0,0,0),
  (0,0,0,0,0,0),
  (0,0,0,0,0,0),
  ), size: 0.6cm) */

#let size = 0.6cm
#let bc = table.cell(fill: black, v(size))
#let wc = table.cell(fill: white, v(size))
#let im = table(
    columns: (0.6cm,)*6 + (1cm,2cm),
    inset: 0pt,
    row-gutter: 0pt,
    column-gutter: 0pt,
    stroke: black+1pt,
    align: horizon,
    wc, wc, bc, wc, wc, wc, table.cell(rowspan: 6, stroke: none)[], [],
    wc, bc, bc, wc, wc, wc, [],
    bc, bc, bc, wc, wc, wc, [],
    wc, wc, wc, wc, wc, wc, box(inset: 4pt)[0, 2, 1, 3],
    wc, wc, wc, wc, wc, wc, box(inset: 4pt)[6],
    wc, wc, wc, wc, wc, wc, box(inset: 4pt)[0, 1, 4, 1]
  )
// #let im = image("trace.png", width: 8cm)
#let te = [
    Aujourd'hui, nous avons vu qu'une image sur un ordinateur est composée de petits carrés nommés ................. /* pixels */, qui ici sont noirs et blancs. De plus, nous avons vu comment ............................... /* encoder */ ces images,  c'est-à-dire les décrire d'une façon compréhensible par un ordinateur, qui ne manipule que des nombres. Nous avons vu que la façon naturelle de le faire, en ne disant pour chaque pixel que s'il est blanc ou noir, est peu efficace. C'est pourquoi nous avons ensuite vu une façon de .................................... /* compresser */ cette image, nommée .................................................................................. /* encodage par longueur de plage */ Cette technique n'est plus utilisée aujourd'hui, mais a eu une place importante en informatique pour transmettre des images.
  ]
#let con = wrap-content(im, te)

#stack(
  dir: ttb,
  spacing: 2cm,
  con,
  con,
  con
)
