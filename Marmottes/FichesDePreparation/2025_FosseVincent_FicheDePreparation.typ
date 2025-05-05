#import "@preview/diagraph:0.3.0":*
#import "@preview/algorithmic:0.1.0"
#import algorithmic: algorithm


#set page(
  paper: "a4",
  margin: (x:0.75in, y: 1in), 
  numbering: "1/1",
  header:context[Info sans ordi#h(1fr) Samuel F. & Noé V.],
  footer: context [
  mars 2025
  #h(1fr)
  #counter(page).display(
    "1 sur 1",
    both: true,
  )
]
)
#v(3em)
#align(center, text(18pt)[Les marmottes au sommeil léger])#v(0em)
#align(center, text(14pt)[Fiche de préparation])

#set heading(numbering: "I.1.a -")
#v(1em)

*Niveau*: CM2

*Durée*: 50 min

*Au préalable*: 
- Organiser la classe en ilôt par groupes de 4 jeunes (ce nombre n'est pas fixe, groupe de 3 ou 5 marche aussi, 4 est le plus simple à organiser).

- Préparer les "portions" de materiel à fournir à chaque groupe (sachet congélation marche très bien).

- Disposer d'un surplus de materiel (au moins 1.5 marmottes et 1 galerie par groupe) afin de palier aux pertes/casses/erreurs de préparation.

*Objectif pédagogique*: construire des arbres pondérés, minimiser un paramêtre, se familiariser avec l'algorithme d'Huffman et la compression.

*Scénario*:
#table(columns:(1fr,2.5fr,5fr,2fr),table.header[*Durée*][*Phase*][*Activité et consignes*][*Organisation et matériel*], 
[5'],[Introduction],[On se présente puis on présente l’activité. Il faut appuyer sur les normes de construction: galeries dans le bon sens, branchements licites (pas plus de 2 au même point, le haut d'une galerie avec le bas d'une autre), pas de marmottes au milieu d'une galerie. Distribuer le materiel (4 (ou 5) galeries par groupe, marmottes (1,2,2,3,4)).],[ tableau ],[10'],[Prise en main (par ilôt de 4)],[Les groupes essaient chacun de manipuler l'arbre pour minimiser le dérangement. On les aide à améliorer l'arbre/on verifie qu'il est minimal],[Marmottes et branchements de terrier.],[5'],[Mise en commun + présentation de l'algo.],[On présente un arbre optimal parmi ceux des élèves. On présente l'algorithme de Huffman et on construit l'arbre de huffman avec la classe. On verifie que les deux arbres ont la même perf.],[Matériel, au tableau.  ],[10'],[Pivot vers l'algorithmique du texte],[On présente un terrier particulier avec des lettres à la place des marmottes et on dit que ce terrier permet des déchiffrer un code secret. Exemple avec "Maman". ],[tableau],[15'],[Prise en main de l'algo],[Décodage du mot fournit en exemple (on fournit l'arbre associé à BARBARAS et le binaire)],[Ardoises],[5'],[Conclusion + Institutionnalisation],[La Compression])

*Présentation de l'activité*:
Aujourd'hui, nous allons aider des marmottes (Est-ce que vous connaissez ces animaux ?). Ces marmottes vont hiberner dans un terrier, on va les aider à construire ce terrier, avec des galeries en forme de "V" inversé, qui sont les plus solides. Sauf qu'il y a un problème, les marmottes se réveillent pendant l'hiver pour prendre l'air, ainsi aucune ne veut dormir au milieu d'une galerie pour ne pas se faire marcher dessus. Aussi, elles font du bruit à chaque fois qu'elles traversent une galerie et certaines se reveillent plus de fois que d'autre. Exemple avec un terrier sous optimal, on compte ensemble le bruit du terrier. On cherche donc à les aider à faire un terrier le plus silencieux possible. Ex: améliorer le terrier encore au tableau, montrer qu'il est moins bruyant.



*Institutionnalisation*:
C'est de l'informatique car utiliser cette méthode d'encodage et de décodage permet de stocker des données sur un espace réduit. En effet, les lettres ne sont pas stockées directement dans le disque dur mais sous forme de 0 et de 1, en fait chaque lettre a besoin de plusieurs 0 et 1 pour être représentée en mémoire. L'algorithme est donc utilisé pour "compresser" de l'information. Pour créer le meilleur terrier pour représenter un mot, on utilise l'algorithme qu'on a présenté avec les marmottes. Sauf qu'ici, on utilise la fréquence d'apparition des lettres dans le mot à la place du nombre de réveils. Cela permet d'avoir les lettres utilisées fréquement en haut de l'arbre et donc de les encoder avec peu de 0 et de 1 (par ex dans barbaras, le "a" s'encodait avec seulement "1" ou alors en français il y a bcp de "e", donc pour compresser un texte en français le "e" serait en haut).

*Etayages/Extension*: 
- On appuie sur l'importance de la hauteur de l'arbre pour que les élèves trouvent le meilleur terrier (et ne se limitent pas à un peigne ou autre solution sous-optimale).
- On propose de creer un arbre (potentiellement pas efficace) qui encode leurs prénoms.


