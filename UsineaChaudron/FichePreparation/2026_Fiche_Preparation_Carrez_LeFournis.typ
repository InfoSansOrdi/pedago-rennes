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

#activite([9001 chaudrons (Usine à chaudrons)], [Adam, Joachim], [1h], [],
  [Faire découvrir la notion de graphe de flot de contrôle.],
  [Suffisament des graphes pour les élèves + de quoi projeter les exemples au tableau],
  (
    [15'],
    [Mise en situation],
    [
      - Présentation du contexte : un sorcier veut produire de la confiture
      - Explication des graphes (instructions, conditions et variables) et du chemin emprunté en suivant une entrée
      - Faire venir un élève au tableau sur un premier petit exemple pour expliquer les consignes pour la suite
    ],
    [],
    [Graphe 1 au tableau],
    
    [2'],
    [Distribution],
    [],
    [],
    [],

    [15'],
    [Instance fixée],
    [
      - Trouver où on arrive dans le graphe lorsque l'instance est fixée
      - Donner les valeurs finales des variables
    ],
    [],
    [Graphe 2 à 4],

    [8'],
    [Couvertures et consignes],
    [
      - Rapide retour si nécessaire sur incompréhensions de l'activité précédente
      - Expliquer la notion de couverture, interroger sur les exemples précédents
      - Parler du dernier exemple avec les boucles
      - Expliquer que l'on aura maintenant 2 sorties : réussite et échec
      - Consignes pour l'activité suivante : trouver si des entrées font exploser le chaudron, et si oui en donner
    ],
    [],
    [Exemple au tableau],

    [2'],
    [Distribution],
    [],
    [],
    [Graphes pochetés, feutres],

    [10'],
    [Instance à trouver],
    [Trouver des entrées qui peuvent faire échouer le programme],
    [],
    [Graphes 5 à 8],

    [8'],
    [Institutionnalisation],
    [
      - Recette=algorithme, donc se généralise au reste de l'informatique
      - On a développé deux utilisations courantes de ce genre de graphe :
        - Créer des tests qui essayent de couvrir le plus un programme (code coverage)
        - Trouver automatiquement d'éventuels bugs (exécution symbolique)
      - Parler du fait qu'on s'est intéressé qu'à un unique type de bugs (des assertions qu'on voudrait éviter), mais que comme on a pu le voir au début il existe aussi les boucles infinies
    ],
    [],
    [Diapo, Traces écrites],
  ),
  [Le graphe 9 peut être particulièrement long s'il faut les garder occuper],
  []
)
