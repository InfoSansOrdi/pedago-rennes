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

#activite([Imagecompression], [Liliana, Joachim], [1h], [Savoir compter et colorier],
  [Faire découvrir la notion de pixel, la compression (et son intérêt) et une façon de le faire (le RLE)],
  [
    - par binôme : 1 feuille 3 grilles 6x6 vierge, 3 grilles 6x6 basiques
    - Quelques feuilles d'une animation 3 frames au cas où extension
    - à projeter : 1 grille entièrement complétée, 2 grilles à moitié complétées avec RLE pour la partie vide, 2 grilles variabilité compression
  ],
  (
    [5'],
    [Introduction],
    [
      - Expliquer ce qu'est un pixel et une image en noir et blanc (#emoji.warning et pas niveau de gris)
      - Consignes pour l'activité de la phase suivante
    ],
    [A présente, B prépare les feuilles pour après (sans les donner)],
    [Une image noire et blanc basse résolution projetée],

    [10'],
    [Encodage binôme sans compression],
    [
      - Bouger éventuellement les tables en binôme
      - Les binômes se séparent un travail : un décrit une image en disant "noir" ou "blanc", l'autre doit la reproduire sur sa feuille plastifiée
    ],
    [B distribue les feuilles, puis A et B viennent superviser],
    [une grille simple (6x6) remplie pour l'un, vide pour l'autre par binôme],

    [5'-10'],
    [Courte restitution et questionnement d'idées],
    [
      - 36 fois dire "blanc" ou "noir"
      - Des idées pour améliorer ça (guider si besoin avec "on veut juste des nombres")
    ],
    [A parle, B prépare le tableau interactif],
    [
      $emptyset$
    ],

    [15'],
    [Explication],
    [
      - Expliquer l'idée de la compression RLE
      - Demander comment encoder avec retour à la ligne
      - Que faire si on commence avec un noir/blanc
      - Faire venir au tableau un élève avec une seconde grille du même genre
    ],
    [B parle pendant que A prépare le matériel à donner],
    [Sur tableau interactif 2 grilles à moitié remplie au dessus, avec des valeurs en dessous],

    [15'],
    [Encodage RLE en binôme],
    [Faire appliquer l'encodage RLE par binôme, chacun étant à tour de rôle l'encodeur et le décodeur sur des nouvelles images],
    [A distribue et B prépare le tableau, puis A et B viennent superviser],
    [2x(nouvelle grille (6x6) remplie pour l'un, vide pour l'autre par binôme)],

    [10'],
    [Institutionnalisation],
    [
      - Nombre d'instructions pour décrire une image inférieur, et intérêt de réduire ce nombre pour communiquer
      - Mais mise en évidence de la variabilité de la taille de l'encodé
      - Intérêt historique pour compresser des images avec des palettes prédéfinies
    ],
    [B conclue la taille de RLE, A présente l'intérêt en info],
    [2 exemples avec des compressions de tailles opposés (une image uniforme, une alternance)]
  ),
  [
    Et quid de la vidéo ? (leur donner une feuille animation 3 frames) Comment  optimiser les retours à la ligne ? Comment le faire avec de la couleur ?
  ],
  [],
)
