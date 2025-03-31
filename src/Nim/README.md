# Jeu de Nim



## Principe
Cette activité permet d'introduire la notion d'**algorithme** en la reliant à la
stratégie d'un jeu à deux joueurs. Elle a été testée très souvent à partir du
cycle 3 (dès le CM1).

## Déroulé

C'est un jeu à deux joueurs où l'on dispose de 12 ou 16 objets quelconques. On
peut utiliser des allumettes comme dans la [variante de
Marienbad](https://fr.wikipedia.org/wiki/Jeu_de_Marienbad), mais il est plus
pratique d'utiliser les jetons de la série d'activité SMN. Ce matériel est prêt
à être imprimé sur une feuille A4 autocollante, puis collé sur du carton plume.

Chacun à son tour prend 1, 2 ou 3 objets, et le but est de prendre le dernier
objet sur la table. Les participants connaissent souvent la variante de
l'émission de télévision *Fort Boyard*, où l'objectif est de **ne pas** prendre
le dernier objet.

L'intérêt de l'activité est l'existence d'une stratégie gagnante, que les
participants vont devoir découvrir en jouant ensemble, avant de la co-construire
pendant la remise en commun.

## Trucs d'animation (spoiler alert)

La stratégie gagnante consiste à toujours laisser sur la table un nombre de
jetons qui soit un multiple de quatre pour qu'au dernier tour, l'autre joueur ne
puisse pas ne laisser qu'un seul jeton sur la table ce qui me forcerait à le
prendre et à perdre. S'il y a 12 ou 16 jetons initialement, le premier joueur ne
peut pas atteindre cet état, et c'est donc pour le second joueur que la
stratégie s'applique.

#### Étayages

On aide les groupes en difficulté en jouant avec eux, de préférence en deuxième
pour pouvoir appliquer la stratégie qu'ils doivent découvrir. Si le groupe ne
trouve vraiment pas (ce qui est rare), on peut disposer les jetons sur la table
par groupe de quatre (par exemple par couleur) et prendre systématiquement les
derniers jetons de chaque paquet entamé.

#### Extensions

* On fait varier le nombre de jetons sur la table : "s'il y a maintenant 15
  jetons sur la table, tu commences ou je commence?" (réponse: la stratégie est
  maintenant pour le joueur qui commence)

* Variante de la règle : on a maintenant le droit de prendre un ou deux jetons
  seulement, et il y a 15 jetons sur la table. Tu commences ou je commence?
  (réponse: la stratégie est maintenant de laisser un nombre de jeton qui soit
  un multiple de trois. Avec 15 jetons, c'est pour le second joueur que la
  stratégie s'applique).

* On peut jouer à la version de Fort Boyard, où il s'agit de ne pas prendre le
  dernier jeton. La stratégie gagnante dans ce cas est de laisser un nombre de
  jetons qui *ne soit pas* un multiple de 4. Avec 16 jetons initialement, le
  premier joueur peut l'appliquer et gagner.

* Plus difficile : On peut maintenant prendre 1 ou 3 jetons. Trouver la stratégie
  demande de dessiner un automate des différentes configurations avec les coups
  autorisés dans chaque cas, et appliquer l'algorithme de
  [Min-Max](https://fr.wikipedia.org/wiki/Algorithme_minimax) sur ce graphe pour
  trouver la stratégie. Cette variante mériterait d'être mieux décrite ici, mais
  elle tiendra certainement occupé même les participants les plus rapides le
  temps que le reste du groupe trouve la version de base.

## C'est de l'informatique !

La notion de stratégie gagnante présentée ici est ce qu'on nomme **algorithme**
en informatique, et c'est absolument fondamental quand on veut utiliser des
ordinateurs. En effet, les ordinateurs ne font que ce qu'on leur demande, sans
aucune forme d'imagination ni d'initiative. Il faut donner des instructions
incroyablement détaillées à l'ordinateur pour qu'il fasse ce qui est attendu.

D'une certaine façon, programmer un ordinateur c'est chercher la stratégie
gagnante l'emmenant à coup sûr d'une situation initiale à la situation finale attendue.

## Matériel

- Fiches de prép : [v2017](nim_prep_2017_BautistaBordais.pdf)
- Trace écrite : [pdf imprimable](nim_trace_ecrite.pdf)
- Matériel à imprimer : le plus simple est d'utiliser les jetons de la série
  d'activité SMN, à imprimer sur une feuille A4 autocollante à coller sur du
  carton plume.

## Références et discussion

Cette activité est un grand classique du folklore de la médiation mathématique,
comme détaillé sur la [page wikipedia
associée](https://fr.wikipedia.org/wiki/Jeux_de_Nim). Quelques autres liens la
décrivant :

- Une [fiche du site
  Pixees](http://people.irisa.fr/Martin.Quinson/Mediation/SMN/) est consacrée à
  cette activité.
- Marie Duflot a [une page](https://members.loria.fr/MDuflot/files/med/nim.html) 
  et elle a fait [une
  vidéo](https://www.youtube.com/watch?list=PLWvGMqXvyJAPSMFgCiy6qVHW9bAPu93X5&v=3WIghG_B4nU)
  sur le jeu de Nim.
- Pour une variante avec une stratégie plus compliquée, allez donc voir le [jeu
  de Marienbad](https://fr.wikipedia.org/wiki/Jeu_de_Marienbad).


### Rapports d'expériences
 - [Adam et Timmerman](Rapports/2023_AdamTimmerman.html) (2023)
 - [Rautureau et Hamon](Rapports/2023_RautureauHamon.html) (2023)
 - [Troublé et Tanguy-Legac](Rapports/2024_TroubleTanguyLegac.html) (2024)
