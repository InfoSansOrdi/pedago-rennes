#import "@preview/fletcher:0.5.8" as fletcher: diagram, node, edge
#import fletcher.shapes: diamond

#let w = 15pt
#set text(w, weight: "semibold")
#set page("a4", flipped: true, margin: 1cm)

#let sugar = image("sugar.svg", width: 60%*w)
#let cherry = image("cherry.svg", width: 68%*w)
#let strawberry = image("strawberry.svg", width: 80%*w)

#let schem(..body) = align(center+horizon, diagram(
  cell-size: 100%*w,
  node-shape: rect,
  node-inset: 10pt,
  // debug: 3,
  node-stroke: 1.2pt,
  edge-stroke: 1.2pt,
  label-sep: 0em,
  // node-fill: gradient.radial(white, blue, center: (40%, 20%), radius: 150%),
  ..body
))

#let start = node((0, 0), "Recette")

// Exemple au tableau
#schem(
  start,
  edge("->"),
  node((0, 1), [
    $#strawberry <- #cherry + #sugar$
    #linebreak()
    $#sugar <- #sugar + 1$
  ]),
  edge("->"),
  node((0, 2), $#strawberry > 5 + #cherry thick ?$, shape: diamond, name: <cond1>),
  edge("->", [Oui]),
  node((0, 3), $#cherry <- #sugar + 5$),
  edge("->"),
  node((1.4, 3), "Réussie", name: <end>),
  
  node((1.4, 2), $#strawberry <- #strawberry + 5$, name: <instr1>),
  edge(<cond1>, <instr1>, "->", [Non]),
  edge(<instr1>, <end>, "->"),
)

#pagebreak()


#let g1 = schem(
  start,
  edge("->"),
  node((0, 1), $#sugar = #cherry thick ?$, shape: diamond, name: <cond11>),
  edge("->", [Non]),
  node((0.0001, 2), $#cherry <- #sugar$),
  edge("->"),
  node((-1, 2), $#sugar  = #cherry thick ?$, shape: diamond, name:<instr11>),
  edge( <cond11>, <instr11>, "->", [Oui]),
  edge("->", [Oui]),
  node((-1, 3), [Réussie]),

  node([
    - $#sugar <- 5, #cherry <- 5$
    - $#sugar <- 8, #cherry <- 4$
  ], enclose: ((-1, 0), (-0.5, 1)), stroke: none)
)


#grid(
  columns: 3,
  column-gutter: 1.7cm,
  row-gutter: 1cm,
  ..(g1,)*6
)

#pagebreak()

#let g2 = stack(dir: ltr,
  spacing: 1cm,
  schem(
  start,
  edge("->"),
  node((0, 1), $cherry = strawberry thick ?$, shape: diamond, name: <cond1>),

  edge("->", [Oui]),
  node((0.75, 2), $sugar = cherry + strawberry thick ?$, shape: diamond, name: <cond2>),

  edge("->", [Oui]),
  node((0.75, 3), [Réussie], name: <end>),

  node((-0.75, 2), $cherry <- strawberry$, name: <instr1>),
  edge("d", "->"),
  node((-0.75, 3), $sugar <- strawberry + cherry$, name: <instr3>),
  edge(<instr3>, <cond2>, "->", bend: -20deg),

  edge(<cond1>, <instr1>, "->", [Non]),
  edge(<cond2>, <instr1>, "->", [Non]),
  ),
  rotate(90deg, origin: bottom+left, reflow: true)[
    - $#cherry <- 8, #strawberry <- 8, #sugar <- 16$
    - $#cherry <- 4, #strawberry <- 8, #sugar <- 12$
    - $#cherry <- 8, #strawberry <- 8, #sugar <- 15$
  ]
)

#grid(
  columns: 2,
  column-gutter: 2cm,
  row-gutter: 0.9cm,
  ..(g2,)*4
)

#pagebreak()

#let g4 = schem(
  start,
  edge("->"),
  node((0, 1), $#strawberry = 4 thick ?$, shape: diamond, name: <cond1>),
  edge("->", [Oui]),
  node((-1, 2), $#sugar <- #cherry$),
  edge("->"),
  node((-1, 3), $#cherry = #strawberry thick ?$, shape: diamond, name: <cond2>),
  edge("->", [Oui]),
  node((-2, 4), $#cherry <- #cherry+1\ #strawberry <- #strawberry+1\ #sugar <- #sugar + 1$, name: <instr1>),
  edge(<instr1>, "r,u", "->"),
  node((0.5, 2), $#cherry <- #cherry + 2$, name: <instr2>),
  node((0.5, 3), $#sugar <- #cherry + #strawberry$, name:<instr3>),
  edge("->"),
  node((0.5, 4), $#cherry = 0 thick ?$, shape:diamond, name: <cond3>),
  edge("->", [Non]),
  node((2.5, 4), $#sugar <- #sugar -2\ #cherry <- #cherry -1$),
  edge("u,l,dl", "->"),
  node((0.5, 5), $#cherry <- 3$, name: <instr4>),
  edge("->"),
  node((0.5, 6), $#strawberry = cherry thick ?$, shape:diamond, name: <cond4>),
  edge("->", [Oui]),
  node((2, 6), [Réussie]),
  node((-1, 6), $#sugar <- #sugar + #cherry$, name: <instr5>),
  
  edge(<instr5>, <cond2>, "->", bend:-40deg),
  edge(<cond4>, <instr5>, "->", [Non]),
  edge(<cond3>, <instr4>, "->", [Oui]),
  edge(<cond1>, <instr2>, "->", [Non]),
  edge(<instr2>, <instr3>, "->"),
  edge(<cond2>, <instr3>, "->", [Non]),

  node([
    - $#strawberry <- 3, #cherry <- 0, #sugar <- 5$
    - $#strawberry <- 5, #cherry <- 2, #sugar <- 5$
    - $#strawberry <- 4, #cherry <- 4, #sugar <- 0$
  ], enclose: ((-2, 0), (-2, 3)), stroke: none) 
)

#g4

// Interruption au tableau

#pagebreak()

#let g5 = schem(
  start,
  edge("->"),
  node((0, 1), $#cherry = 0 thick ?$, shape: diamond, name: <cond1>),
  edge("->", [Oui]),
  node((0, 2), [Boom]),
  node((-1, 2), $#strawberry = cherry thick ?$, shape: diamond, name: <cond2>),
  edge("->", [Oui]),
  node((-1, 3), [Réussie]),
  node((0, 3), $#cherry <- #cherry -1$, name: <instr1>),
  edge("r,uu,l", "->"),
  
  edge(<cond1>, <cond2>, "->", [Non]),
  edge(<cond2>, <instr1>, "->", [Non])
)

#align(horizon, grid(
  columns: (50%, 50%),
  align: center,
  g5, g5
))

#pagebreak()

#let g6 = schem(
  start,
  edge("->"),
  node((0, 1), $#sugar > #strawberry thick ?$, shape: diamond, name: <cond1>),
  edge("->", [Non]),
  node((-1, 2), $#sugar < #strawberry thick ?$, shape: diamond, name: <cond2>),
  edge("->", [Oui]),
  node((-1, 3), $#strawberry <- #sugar$),
  edge("->"),
  node((1, 3), $#sugar = #strawberry thick ?$, shape: diamond, name: <cond3>),
  edge("->", [Non]),
  node((0, 4), [BOOM]),

  node((1, 2), $#sugar <- #strawberry$, name: <instr1>),
  node((1, 4), [Réussie], name: <instr2>),

  edge(<cond1>, <instr1>, "->", [Oui]),
  edge(<instr1>, <cond3>, "->"),
  edge(<cond2>, <cond3>, "->", [Non]),
  edge(<cond3>, <instr2>, "->", [Oui]),
)

#align(horizon, grid(
  columns: (50%, 50%),
  align: center+horizon,
  g6, g6
))

#pagebreak()

#let g7 = rotate(90deg, origin: bottom+left, reflow: true, schem(
  start,
  edge("->"),
  node((0, 1), $#sugar > 5 thick ?$, shape: diamond, name: <cond11>),
  edge("->", [Non]),
  node((-1, 2), $#sugar <- #sugar + (#strawberry ÷ 2)$, name: <instr11>),
  edge("->"),
  node((1, 2), $#strawberry = 0 thick ?$, shape: diamond, name: <cond12>),
  edge("->", [Oui]),
  node((0, 3), [BOOM]),
  node((2, 3), $#sugar = 0 thick ?$, shape: diamond, name: <cond13>),
  edge("->", [Non], label-side: right),
  node((2, 2), [$#sugar <- #sugar - 1$ #linebreak() $#strawberry <- #strawberry - 1$], name: <instr12>),
  node((1, 3), [Réussie], name: <instr13>),
  
  edge(<cond11>, <cond12>, "->", [Oui]),
  edge(<instr12>, <cond12>, "->"),
  edge(<cond12>, <cond13>, "->", [Non], label-pos: 60%),
  edge(<cond13>, <instr13>, "->", [Oui]),
))

#align(horizon, grid(
  columns: (50%, 50%),
  align: center,
  g7, g7
))

#pagebreak()

#let g8 = schem(
  start,
  edge("->"),
  node((0, 1), $#sugar > #cherry thick ?$, shape: diamond, name: <cond1>),

  edge("->", [Oui]),
  node((1, 2), $#sugar <- #sugar - 2$, name: <instr1>),
  edge("u,l", "->"),

  node((0, 2), $#sugar < #strawberry thick ?$, shape: diamond, name: <cond2>),
  edge(<cond1>, <cond2>, "->", [Non]),

  node((-1, 2), $#sugar <- #sugar + 3$, name: <instr2>),
  edge(<cond2>, <instr2>, "->", [Oui]),
  edge("u,r", "->"),

  node((0, 3), $#strawberry > #cherry thick ?$, shape: diamond, name: <cond3>),
  edge(<cond2>, <cond3>, "->", [Non]),

  edge("->", [Oui]),
  node((-0.5, 4), [Boom]),

  edge(<cond3>, <end>, "->", [Non]),
  node((0.5, 4), [Réussie], name: <end>)
)

#align(horizon, grid(
  columns: (50%, 50%),
  align: center,
  g8, g8
))

#pagebreak()

#let g9 = schem(
  start,
  edge("->"),
  node((0, 1), $#strawberry < 33 thick ?$, shape: diamond, name: <cond1>),
  edge("->", [Oui], label-side: left),
  node((-1, 1), $#strawberry <- #strawberry + 1$, name: <instr1>),

  node((0, 2), $#cherry < 8 thick ?$, shape: diamond, name: <cond2>),
  edge("->", [Oui], label-side: left),
  node((-1, 2), $#cherry <- #cherry + 1$, name: <instr2>),

  node((0, 3), $#strawberry = 0 thick ?$, shape: diamond, name: <cond3>),
  edge("->", [Non], label-side: left),
  node((0, 4), $#sugar <- "reste de la"\ " division de"\ #cherry "par" #strawberry$),
  edge("->"),
  node((-1, 4), $#cherry <- #strawberry$),
  edge("->"),
  node((-1, 3), $#strawberry <- #sugar$, name: <instr3>),

  node((1, 3), $#cherry = 1 thick ?$, shape: diamond, name: <cond4>),
  edge("->", [Oui]),
  node((1, 2), [Boom]),
  node((1, 4), [Réussite], name: <instr4>),

  edge(<instr1>, <cond1>, "->", bend: 30deg),
  edge(<cond1>, <cond2>, "->", [Non], label-side: left),
  edge(<instr2>, <cond2>, "->", bend: 30deg),
  edge(<cond2>, <cond3>, "->", [Non], label-side: left),
  edge(<instr3>, <cond3>, "->"),
  edge(<cond3>, <cond4>, "->", [Oui]),
  edge(<cond4>, <instr4>, "->", [Non])
)

#align(horizon, grid(
  columns: (50%, 50%),
  align: center,
  g9, g9
))
