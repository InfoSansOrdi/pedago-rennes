#let doc_title = [Activité "Algorithmes de Tris"]

#set par(justify: true)

#set page(
    footer :context [
        #doc_title
        #h(1fr)
        #counter(page).display(
            "1 / 1",
            both: true,
        )
    ]
)

#align(center, [
    = #doc_title
    
    Benjamin WOJTECKI #h(2em) Timothée MENEUX
])
\
== Résumé de l'activité

- *Objectif :* découvrir des tris classiques et la dichotomie, ainsi que leur intérêt.
- *Niveau :* CM2
- *Durée totale :* 55 minutes
- *Organisation :* par groupes, de préférence en binôme.
\

== Organisation de l'activité
#table(
    columns: (10%, 15%, 35%, 20%, 20%),
    align: (center,left, left, left, left),
    [*Durée*],[*Phases*],[*Activité et consignes*],[*Organisation*],[*Matériel*],
    [5'],[Présentation globale],[Les élèves vont devoir chercher une carte parmi plusieurs cartes, puis à nouveau mais une fois triées. Enfin, ils devront utiliser un algorithme pour trier les cartes],[Oral],[Un sous-jeu de cartes pour expliquer les règles],
    [5'],[Mise en pratique\ (Phase 1)],[Recherche d’une carte parmi un groupe de carte mélangé.\ Noter au tableau les stats des groupes],[En groupes],[Un jeu de cartes d’une seule couleur (13)],
    [10],[Mise en pratique\ (Phase 2)],[Recherche d’une carte parmi un groupe de carte trié.\ Noter au tableau les stats des groupes"],[En groupe],[Un jeu de cartes d’une seule couleur (13)],
    [5'],[Mise en commun],[Expliquer la dichotomie et sa "rapidité"],[Oral],[Aucun],
    [10'],[Mise en pratique\ (Phase 3)],[Objectif : trouver un tri, commencer avec peu de cartes (peut-être 5 ?)],[En groupe],[Un jeu de cartes d’une seule couleur (13)],
    [5'],[Mise en commun],[Les élèves ont-ils réussi à trier les cartes ? Si non, normal. Si oui, était-ce facile ? Rapide ?],[Oral],[Aucun],
    [10'],[Mise en pratique\ (Phase 4)],[Donner les fiches explicatives des tris, en faire un, puis le deuxième si temps le permet.],[En groupe],[Un jeu de cartes d’une seule couleur (13)],
    [5'],[C’est de l’info car…],[Reprendre les stats avec et sans dichotomie pour expliquer l’intérêt de trier et en particulier pour l’informatique],[Oral],[Ramassage (en parallèle)]
)
\

== Les différentes phases :
+ L'un des deux élèves regarde les cartes, retient la valeur d'une d'entre elles puis les étale toutes sur la table, allignées et face cachée. Ensuite, son partenaire retourne les cartes une à une jusqu'à retrouver la bonne, puis annonce le nombre de cartes retournées.

+ On change l'expérience, cette fois-ci les cartes à l'envers mais rangées dans l'ordre croissant. La personne qui choisit la carte ne dit plus la valeur de la carte dès le départ, mais quand son partenaire retourne les cartes, annonce si c'est la carte cherchée (auquel cas on s'arrête et on annonce le nombre de cartes retournées avant de trouver) ou bien si la carte à trouver est plus grande ou plus petite que la carte retournée.

+ On recommence presque comme à la phase 1, on mélange les cartes puis on les étale face cachée. L'informaticien demande à l'ordinateur d'effectuer des opérations avec les cartes (en comparer deux, en déplacer une, en échanger deux, etc.). L'informaticien doit réussir à trier les cartes.

+ Idem qu'à la phase précédente, mais l'on doit suivre les instructions d'un algorithme.