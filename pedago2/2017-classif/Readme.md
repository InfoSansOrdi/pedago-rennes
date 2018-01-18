Cette activité est basée sur une idée original de Dominique Barbe. Elle est distribuée sous licence CC-BY.

But : découvrir la classification et ses enjeux !

Matériel : des images d'animaux (libres de droits).

# Exercice 1 : "feature extraction"

## Déroulé
- On présente unes à unes quelques images d'animaux "simples".
- On pose la question : ils vivent sur terre, sur mer ou dans les airs ?
- On pose la question : qu'est-ce qui vous fait dire ça ? On espère qu'ils relèvent des caractéristiques telles que "ailes", "4 pattes", "plumes", "écailles", etc.

## Objectif
On se prépare aux exercices suivants (où les images seront cachées). Voir quelques images en avance permettra d'éviter de se disperser. Peut-être peut-on se passer de ce premier exercice avec des élèves plus agés ? Aussi, on va indurie volontairement en erreur les élèves vers des features "simples".
On illustre ici la phase de création de features: des données numériques/catégoriques (nombre de pattes) extraites d'objets (d'images) utilisables pour la classification.

# Exercice 2 : "learning"

## Déroulé
- On recommence l'exercice 1, mais les cartes sont cachées. Les élèves doivent poser des questions jusqu'à ce qu'ils puissent répondre à la question (terre/mer/air ?).
- On espère qu'une suite de question émerge (il s'agit d'un arbre de décision, presque).
- On relève cette suite de question.

## Objectif
On illustre ici la phase d'apprentissage : à partir d'un suite d'exemples on construit et améliore un classifieur. Puisque les élèves interrogent avec de questions, on a affaire à une strucure d'arbre :
Il a 4 pattes ?
- (oui) Terre !
- (non) Il a des plumes ?
  - (oui) Air !
  - (non) Mer !

# Exercice 3 : "testing"

## Déroulé
- Une fois que les élèves ont un classifieur qui marche bien (les nouvelles images sont toujours bien classifiées), on leur propsoe de le tester ! Ils vont classifier ~10 images d'affilée, et on verra les réponses (% de réussite) uniquement à la fin.
- On recommence, mais avec des animaux "non-standards" :
  - poisson-volant (ailes, mais vit sous l'eau)
  - crabe (plein de pattes, mais vit sous l'eau)
  - poule (des ailes, mais vit sur terre)
  - pégase
Haha ! Ça ne marche plus !

## Objectif
On illustre la phase de test : le classifieur est fixe, et est utilisé pour classifier de nouvelles images.
Ce qui est intéressant, c'est surtout la deuxième phase, où on sort des animaux plus originaux. *Puisque les élèves n'en ont pas eu pendant l'apprentissage, leur classifieur ne saura pas les classifier*. Et là on touche du doigt quelque chose de très important (et dont on peut discuter looooongtemps avec les élèves). On peut alors parler des classifieurs utilisés actuellement par divers entreprises/gouvernements, et de leurs dangers potentiels.

# Exercice 4 (WIP) : "adversarial examples"
- On améliore le classifieur avec les exemples tordus de la fois précédente ?
- Adversarial examples : modifier un animal subtilement pour qu'il soit mal classifié.
- Adversarial examples : images ridicules qui trompent le clasifieur (une enclume avec des ailes).
