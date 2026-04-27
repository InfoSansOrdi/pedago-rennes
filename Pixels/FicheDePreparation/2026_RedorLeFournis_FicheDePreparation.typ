#set page("a4", flipped: true, margin: 0.8cm)
#set text(11pt, lang: "fr")

#let activite(titre, membres, duree, prerequis, description, materiel, content, extensions, etayages) = {
  for i in range(calc.div-euclid(content.len(), 5)) {
    content.at(i*5+1) = strong(content.at(i*5+1))
  }
  table(
  columns: (2fr, 3.3fr, 12fr, 3fr, 4fr),
  stroke: black+1pt,
  align: center+horizon,
  [*Titre*], table.cell(colspan: 4, titre),
  [*Membres*], table.cell(colspan: 4, membres),
  [*Durée*], table.cell(colspan: 4, duree),
  ..{ if prerequis != [] {([*Prérequis*], table.cell(colspan:4, prerequis))}},
  [*Description*], table.cell(colspan: 4, description),
  [*Matériel*], table.cell(colspan: 4, materiel),
  [*Durée*], [*Phase*], [*Activités*], [*Orga*], [*Matériel*],
  ..content,
  ..{ if extensions != [] {([*Extensions*], table.cell(colspan:4, extensions))}},
  ..{ if etayages != [] {([*Étayages*], table.cell(colspan:4, etayages))}},
)
}

#activite([Pixels], [Ewan, Joachim], [1h], [Activité RLE + une activité parlant d'algorithmique peuvent permettre de mieux comprendre l'enjeu de certaines notions abordée. Dans l'absolu, aucun prérequis n'est essentiel à la compréhension de l'activité.],
  [Introduire la notion de complexité de Kolmogorov au travers de la description d'images colorées],
  [
  ],
  (
    [5'],
    [Introduction],
    [
      - Reparler de l'activité RLE qu'on avait fait il y a 2 semaines, notamment les images matricielles utilisant des palettes pour la couleur
      - Expliquer comment on mesure le coût d'une solution (nombre de mots), et que l'objectif reste le même : décrire une image à un autre
      - Montrer que RLE n'est pas une solution "miracle", avec un exemple où en choisissant le bon langage, la solution de décrire en français (naturelle pour les élèves) est bien plus efficace
    ],
    [],
    [],

    [10'-15'],
    [Explication et activité],
    [
      - On a expliqué avant l'activité de se décrire en trinôme, mais peut être faire intervenir au tableau un élève s'il y a des doutes
      - Leur donner une dizaine d'images, en finissant par des cas intéressant dont on rediscutera après pour voir qui a la solution la plus courte
    ],
    [],
    [],

    [0'-5'],
    [Comparaison de solutions],
    [
      - Reprendre les dernières images et faire intervenir les élèves pour qu'ils proposent leurs solutions en les comparant
    ],
    [],
    [],

    [20'],
    [Compétition],
    [
      - Découper la classe en 4 groupes, pour faire 4 duels de 4 minutes de description d'images
    ],
    [],
    [],

    [20'],
    [Conclusion et trace écrite],
    [
      - Leur expliquer le lien de l'activité avec algorithmes/langages de programmation (possiblement mentionner le principe de turing completness selon le temps)
      - Leur faire deviner (ou leur donner l'intuition selon le temps) du fait que le langage choisi n'importe pas à constante près
    ],
    [],
    []

    
  ),
  [],
  [],
)