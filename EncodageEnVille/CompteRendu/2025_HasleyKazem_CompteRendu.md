# Compte Rendu - Encodage en ville


## Sommaire :


- [Présentation de l'activité](#présentation-de-lactivité)
- [Enjeu choisi](#enjeu-choisi)
- [Rapport de la séance](#rapport-de-la-séance)
- [Notes pour le futur](#notes-pour-le-futur)



</br>
</br>
</br>

# Présentation de l'activité

Nous avons choisi de présenter une activité du site [csunplugged.org](https://classic.csunplugged.org/documents/activities/public-key-encryption/unplugged-18-public_key_encryption_0.pdf), adaptée à un public plus jeune. L’activité Encodage
en Ville propose aux élèves de découvrir un procédé d’encodage et de décodage de messages (nombres) grâce à une
carte (un graphe, présenté comme la carte d’une ville). La découverte commence par l’explication et l’application
de l’algorithme d’encodage et de décodage, puis montre le fonctionnement de ce procédé et présente la notion de
problèmes difficiles à résoudre (NP-Complétude). Cette activité permet donc de présenter (grossièrement) à la fois la
notion de complexité théorique, ainsi qu’une application possible au travers de la cryptographie.
Cette activité ne nécéssite pas un matériel compliqué, mais une piste d’amélioration possible serait la manufacturation
d’un jeu de points et barres facilement arrangeable en graphe (à la manière de géomags, avec du velcro?) afin que les
élèves perçoivent et manipulent mieux cette notion de "carte" : Les élèves ont reçu :

* Un graphe "clé publique" (différent pour chaque membre d’un groupe)
* Le graphe "clé privée" associée

Pour cette activité, nous avons choisi l’organisation suivante :
1. Présentation de Nous, puis "histoire" de l’activité.
2. Présentation des algorithmes d’encodage et décodage.
3. Première tâche : Par groupe de deux, découvrir par la manipulation directe les algorithmes d’encodage et décodage.
4. Une fois cette première manipulation terminée, se mettre en groupe de quatre (le matériel a été distribué de
manière à ce que les membres des groupes de quatre n’aient jamais les mêmes graphes). Envoyer des messages
entre deux membres du groupes pendant que les deux autres essayent de décoder (et n’y arrivent pas!)
5. Remise en commun : Noter qu’il est compliqué de retrouver le message d’origine, il n’y a pas de meilleure solution
que le brute-force naïf. Remarquer que plus le graphe est grand, plus les opérations sont compliquées, et le
décodage devient difficile.
6. Montrer pourquoi cet encodage fonctionne et le problème de graphe sous-jacent (partition du graphe par des
ensembles $\{\text{sommet } s ∪ \{\text{voisins de } s\}\}$).
7. Reprise en groupe de quatre, Compétition : Demander aux groupes de trouver le plus grand graphe répondant au
problème (donc générer un graphe + trouver la partition si cette dernière existe, ce qui n’est pas garanti.)
8. Institutionnalisation + Trace écrite + Questions.
(Histoire de l’activité : Des espions essayent de se transmettre des messages sans se faire espionner, ces derniers
décident de placer des nombres à certains endroits de la ville, puis encodent et décodent ces messages avec la procédure
fournie.)

</br>
</br>
</br>

# Enjeu choisi


Comme dit précédemment, nous avons choisi d’aborder les notions de Cryptographie et de Complexité Algorithmique.
Cette activité permet de présenter le principe de la cryptographie commme le fait de cacher des messages, afin que le
décodage soit beaucoup trop demandant calculatoirement. La notion de NP-Complétude comme difficulté algorithmique
permet également de montrer et d’illustrer brièvement les problèmes de complexité théorique.

VERSION ÉLÈVE :

>
> <center><b> Encodage en Ville </b></center></br>
> <p, style="text-align: justify;"> Les ordinateurs peuvent nous servir à communiquer. Nous pouvons par exemple nous envoyer des messages entre nous, pour parler du dernier film de Marvel, pour acheter des objets en ligne ou encore pour partager ses pires secrets. Il est donc important que ces échanges de messages soient sécurisés : Personne d’autre que le destinataire ne doit être en mesure de lire le message envoyé. L’activité Encodage en Ville permet d’illustrer comment échanger de manière sécurisée, via une procédure appelée Algorithme de chiffrement. Notre algorithme de chiffrement se repose sur un problème que personne ne sait résoudre rapidement. De tels problèmes sont appelés Problèmes NP-Complets, et forment un sujet de recherche encore très actif. À tel point que savoir résoudre ces problèmes rapidement peut mener à une récompense de 1 Million de Dollars!</p>


(Les termes en gras ont évidemment vocation à être développés à l’oral)


</br>
</br>
</br>

# Rapport de la séance

À l’issue de cette séance, nous regrettons une présentation trop longue de notre part au début de l’activité. Présenter (même aussi simplement que possible) l’algorithme d’encodage et décodage sans manipulation directe par les élèves a mené à une incompréhension générale de la première partie. Nous avons donc choisi de laisser les élèves lire d’eux-même
l’algorithme et de répondre aux premières questions, avant de revenir au tableau pour refaire un exemple clair sur une carte simple. Cette modification on the fly du planning nous a poussé à accorder moins de temps à la partie "il est difficile de décoder". Ceci s’est ressenti lors de la première remise en commun et institutionnalisation, où peu d’élèves avaient compris l’intérêt de la méthode. Cependant, la deuxième partie (portant sur la difficulté algorithmique du problème de graphe) semble avoir été mieux comprise. Une fois le principe de "découpage" des sommets expliqué, nous avons entendu beaucoup d’extase venant des élèves. Ceci s’est également remarqué lors de l’activité, où très peu de questions (sur les règles de l’activité) ont été
posées. Nous sommes agréablement surpris de voir que quelques familles de graphes intéréssantes ont été proposées (comme des graphes étoilés, où le sommet particulier se trouve au centre, ainsi que des arrangements de triangles repris de nos premiers graphes). Beaucoup d’approches différentes de la part des élèves nous ont permis de mettre en lumière la difficulté du problème
: Plus le graphe initial est grand, plus choisir une position correcte pour les sommets particuliers est compliqué, alors qu’un choix trivial des sommets particuliers amène à un décodage facile.
La mention de la récompense de $1 Million de l’institut Clay a évidemment interrogé et surpris les élèves, certains ayant immédiatement recherché des solutions au problème posé.


</br>
</br>
</br>

# Notes pour le futur

Si cette activité intéresse de futurs groupes, nous donnons ici quelques notes sur ce qu’il semble pertinent d’améliorer :
* Organisation de la première partie : Nous pensons qu’il soit plus pertinent de laisser les élèves explorer d’eux-même la procédure d’encodage et décodage (bien que le langage employé puisse être difficile à comprendre) avant d’expliquer au tableau. Notre présentation exhaustive de la procédure a pris trop de temps, ce qui a mené beaucoup d’élèves à décrocher à cause de la densité d’information.
  
* Le matériel : Les graphes mis à disposition sont peut-être trop grands pour la partie de familiarisation avec la procédure d’encodage : Beaucoup d’erreurs de calcul ont ralenti la bonne compréhension de la méthode (les élèves étaient sceptiques après avoir vu que le décodage ne fonctionnait pas à cause d’une erreur de calcul), sans mentionner le nombre trop important de calculs nécéssaires pour l’encodage sur un "grand" graphe. Une taille importante est néanmoins nécéssaire pour les essais de décodage brute-force (il est important d’avoir plusieurs sommets particuliers avec un placement non trivial).
  
* Description de la deuxième partie : Nous avons remarqué que certains élèves ont seulement dessiné la forme d’un
graphe. Aucun sommet n’était présent, seuls des traits symbolisant les arêtes étaient dessinés. Nous pensons qu’il peut être bénéfique de rapidement rappeler qu’une carte est composée de sommets et d’arêtes (employer un autre vocabulaire), et que l’objectif est de trouver un placement des sommets importants (les étoiles) afin de découper le graphe comme présenté.
