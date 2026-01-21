#set page(
  header: align(left)[
    Chateau pas très fort #h(1fr) 24 février 2025
    #line(length: 100%)
  ],
  flipped: true,
)

// #set heading(numbering: "I.1.a -")

#set text(size: 17pt) // font: "Fraktur BT")

#set par(justify: true)

#let dotsline() = box(width: 1fr, repeat(" _ "))

= Les opérateurs
- ET : la formule $A$ ET $B$ est vraie quand #dotsline()

- OU : la formule $A$ OU $B$ est vraie quand #dotsline()

- NON : la formule NON $A$ est vraie quand #dotsline()

- $circle.filled$ : la formule $circle.filled A$ est vraie quand _A sera vraie au moins une fois._

- $~ #h(-3pt) ~$ : la formule $~ #h(-3pt) ~ A$ est vraie quand _A sera toujours vraie._

- $- #h(-2pt) circle.filled$ : la formule $- #h(-2pt) circle.filled A$ est vraie quand _dans la pièce d'après A sera vraie._


- $~ #h(-3pt) circle.filled$ : la formule $A ~ #h(-3pt) circle.filled B$ est vraie quand _A est d'abord vraie, puis B sera vraie._

= Vérifier nos formules
Avec ces opérateurs on a pu créer des formules que l'on veut pouvoir vérifier dans notre château, ce qu'on peut faire facilement dans notre cas, mais en général on va utiliser un algorithme. Pour l'exemple de la formule "_Il existe un chemin tel qu'un jours on trouve un trésor_", on va :
1. Mettre un point sur les salles où il y a #dotsline()
2. Remplacer chaque point par une croix et mettre un point sur les salles qui vont dans les salles qui avaient un point
3. Recommencer le point 2 jusqu'à ce que #dotsline()