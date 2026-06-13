#import "schemas.typ": *
#import "@preview/wrap-it:0.1.1": wrap-content

#set page("a4", flipped: false, margin: 1.2cm)
#set text(12pt, lang: "fr")

#let graphe = schem(
  node((0, 0), [Fonction `f`]),
  edge("->"),
  node((0, 1), [
    $i <- 0$
    #linebreak()
    $"somme" <- 0$
  ]),
  edge("->"),
  node((0, 2), $i < n thick ?$, shape: diamond, name: <test>),
  edge("->", [Oui], bend: 30deg),
  node((0, 3), [
    $i <- i + 1$
    #linebreak()
    $"somme" <- i$
  ], name: <corps>),
  edge(<corps>, <test>, "->", bend: 30deg),
  
  node((1, 2), $"somme" > 2 thick ?$, shape: diamond, name: <fin>),
  edge("->", [Oui]),
  node((1, 1), [Réussite]),
  node((1, 3), [Bug], name: <bug>),

  edge(<test>, <fin>, "->", [Non], bend: 30deg),
  edge(<fin>, <bug>, "->", [Non]),
)

#let resume = [
  #set par(justify: true)
  Aujourd'hui nous avons joué avec des *graphes de flot de contrôle* représentant des recettes de cuisine pour faire des confitures. Ils contiennent des *instructions* et des *conditions*, portant sur des *variables*. Ces graphes ont pu être plus ou moins complexes, avec notamment des *boucles*.

  Ces graphes représentent en réalité des *algorithmes*, qui comme pour les recettes, peuvent réussir ou échouer :  on parle alors de *bugs*.

  Afin d'éviter ces bugs, les informaticiens mettent en place des *tests*, programmes exécutés par eux et non par les utilisateurs, afin d'essayer de prouver que leurs programmes ne possèdent pas de bugs.

  Pour mesurer la qualité de ces tests, ils s'intéressent à la *couverture* de ces tests, c'est à dire à quels point ces tests passent par toutes les instructions et conditions *(couverture par sommet)* ou par toutes les flèches *(couverture par arêtes)*. Cependant, rien n'assure dans cette méthode l'absence totale de bugs.

  Pour être sûr qu'il n'y a pas de bug, certains informaticiens peuvent utiliser de l'*exécution symbolique* afin de chercher depuis un bug quelles entrées les causent. Cependant, cette technique demande de résoudre des grands systèmes d'équations, ce qui est lent. C'est pourquoi cette méthode n'est pas souvent utilisée.
]

#let trace = wrap-content(graphe, resume)

#trace
#v(2cm)
#trace
