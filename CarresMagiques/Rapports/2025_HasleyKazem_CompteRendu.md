<!-- Page de titre -->

<h1 align="center" style="font-size: 3em; font-weight: bold;">Compte rendu (NIM)</h1>

<p align="center" style="font-size: 1.5em; font-weight: bold;">
William Hasley &
Nowar Kazem
</p>

<div style="page-break-after: always;"></div>

<!-- Sommaire -->

# Sommaire

- [Présentation de l'activité](#présentation-de-lactivité)
- [Enjeu choisi](#enjeu-choisi)
- [Rapport de la séance](#rapport-de-la-séance)



# Présentation de l'activité
Pour cette activité, nous avons choisi l'activité carrés magiques, qui sert d’introduction aux codes correcteurs d’erreurs. 
Le principe est le suivant : Quelqu’un range des petits carrés à deux faces (une noire et l’autre blanche) 
dans un carré de 5x5 de sorte à ce que le nombre de carrés noirs dans chaque ligne et chaque colonne soit pair. Il demande à
une autre personne de tourner un carré puis demande au magicien de deviner le carré tourné.
Avec un simple calcul on y arrive. Le but est d’expliquer aux élèves l’idée derrière ce tour de magie. L’objectif était de 
faire découvrir aux élèves les codes correcteurs d'erreurs.Nous avons utilisé du matériel 
déjà existant, et chaque groupe a reçu 36 carrés.

Pour cette activité nous avons choisi l'organisation suivante : 
1. Présentation de Nous, puis présentation de l'activité, ensuite faire un exemple au tableau.
2. Répartition des élèves en groupes de quatre et distribution du matériel.
3. Un animateur par groupe faisait vivre l’activité, en jouant le rôle du magicien et en guidant les élèves pour les amener à découvrir le principe caché.
4. Après cette phase de découverte, nous avons repris l’attention de toute la classe pour expliquer collectivement le fonctionnement du tour.
5. Les élèves ont ensuite rejoué l’activité entre eux, en alternant les rôles, pour s’assurer qu’ils avaient bien compris.
6. Institutionnalisation + Trace écrite + Questions.


# Enjeu choisi
Comme mentionné précédemment, nous avons choisi de parler des codes correcteurs d'erreurs et de leur utilité.

---

<u>**VERSION PROF**</u> : 
C’est de l’informatique parce qu’on cherche à corriger des erreurs qui peuvent apparaître dans des messages. 
C’est exactement ce que fait l’activité des carrés magiques.

Le "secret" de l’activité est simple : on commence par construire une grille dans laquelle chaque ligne et 
chaque colonne contient un nombre pair de carrés noirs. Si quelqu’un retourne un carré (le passe du blanc 
au noir ou l’inverse), alors la ligne et la colonne où se trouve ce carré auront un nombre impair de carrés 
noirs. Il suffit de repérer ces deux indices pour retrouver le carré retourné.

En informatique, on appelle ce type de méthode un code correcteur d’erreurs. C’est un ensemble de règles 
ou un algorithme qui permet de détecter et parfois corriger les erreurs. Remarquons que, dans notre activité,
nous pouvons corriger au plus une erreur : Si on retourne deux carrés nous sommes a priori incapables de 
retrouver lesquels ont été retournés. 
Pour corriger deux erreurs, il faudrait ajouter deux lignes et deux colonnes supplémentaires. Mais plus 
on veut corriger d’erreurs, plus il faut ajouter d’informations, ce qui montre un compromis : on veut 
corriger le maximum d’erreurs, mais sans alourdir trop le message.

Les codes correcteurs sont partout autour de nous. Par exemple, dans les messages envoyés sur Internet, 
dans les CD, dans les satellites, ou encore dans les clés USB : le nom "USB" est lié à un standard qui 
utilise ce type de code pour assurer que les données ne sont pas perdues ou abîmées.

L’exemple des carrés magiques est bien sûr très simple, mais il montre l’idée de base que l’on retrouve 
dans les vrais codes correcteurs utilisés en informatique.

---

<u>**VERSION ÉLÈVE**</u> : 
Les ordinateurs, contrairement aux humains, communiquent par des câbles et par
des ondes. Mais de manière semblable aux humains, il arrive que de petites erreurs
s’introduisent dans les messages transmis : Tout comme le vent peut empêcher la
bonne réception, il arrive que du "bruit" perturbe un message. Il faut donc que
nos ordinateurs soient capables de corriger les erreurs. Là où nous serions tentés
de renvoyer le message (comme nous le ferions entre nous), cette approche à très
peu de chance de fonctionner, d’autant que dédoubler les messages se trouve être
long. L’activité Carrés Magiques présente une manière de corriger les messages
avec un Code Correcteur. En ajoutant quelques informations supplémentaires au
message, nous pouvons corriger un certain nombre d’erreurs très facilement, sans
avoir besoin de renvoyer le message.



# Rapport de la séance
Dans l’ensemble, la séance s’est très bien déroulée. Les élèves se sont montrés 
curieux, investis et ont bien joué le jeu. Dès le début, il y a eu un effet de 
surprise : ils étaient étonnés de nous voir deviner à chaque fois le carré qui avait été retourné.


Une fois la phase de recherche lancée, nous – les animateurs – avons réalisé plusieurs 
tours de magie avec les groupes pour les amener à comprendre le fonctionnement de cette "magie". 
Nous avons pris soin de changer régulièrement de groupe pour bien faire comprendre que 
connaître l’état initial de la grille n’était pas nécessaire.


Lorsque nous avons commencé à faire remarquer que nous comptions les carrés noirs, 
la majorité des élèves ont compris que le secret reposait sur une astuce de comptage.
Certains élèves ont cru que nous mémorisions la grille, mais nous avons pu les détromper 
facilement en changeant de groupe ou en faisant intervenir un animateur qui n’avait jamais 
vu la grille de départ. D’autres pensaient que la grille se retrouvait dans une configuration 
particulière "par hasard" (par exemple deux carrés noirs par ligne). Certains nous ont 
agréablement surpris en évoquant des idées liées à la parité, même s’ils ne trouvaient pas 
encore l’astuce exacte.


Certains élèves voulaient absolument nous "battre" (retourner un carré sans que nous ne sachions lequel), 
ils ont même triché pour ça : par exemple en retournant plusieurs carrés au lieu d’un seul, ou en 
modifiant la grille après que le magicien ait placé les lignes et colonnes magiques.


Après cette longue phase de recherche (la plus riche de la séance), nous avons repris l’attention 
de la classe pour expliquer le secret derrière le tour. Ensuite, les élèves ont pu s’exercer entre 
eux, en jouant à leur tour les magiciens, ce qui nous a permis de vérifier leur compréhension.
Nous avons toutefois été surpris de constater que certains élèves n’avaient pas bien compris le principe, 
et continuaient à mémoriser la grille de départ ou à désigner un carré au hasard. Pourtant, nous 
avions reprécisé plusieurs fois que le raisonnement ne dépendait pas de la mémoire, et nous avions 
même refait un exemple au tableau.


Enfin, lors de la phase d’institutionnalisation, aucun élève n’a spontanément fait le lien avec 
l’informatique, ni évoqué la correction d’erreurs. Cependant, certains ont parlé de la notion d’algorithme, 
ce qui nous a fait plaisir, car cela montrait qu’ils se souvenaient d’une notion vue lors d’une activité précédente. 


