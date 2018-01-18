But : découvrir la classification et ses enjeux !

Matériel : des images d'animaux.

- Exercice 1 : "feature extraction"
  - On présente unes à unes quelques images d'animaux "simples".
  - On pose la question : ils vivent sur terre, sur mer ou dans les airs ?
  - On pose la question : qu'est-ce qui vous fait dire ça ? On espère qu'ils relèvent des caractéristiques telles que "ailes", "4 pattes", "plumes", "écailles", etc.

- Exercice 2 : "learning"
  - On recommence l'exercice 1, mais les cartes sont cachées. Les élèves doivent poser des questions jusqu'à ce qu'ils soient sûrs de leur décision.
  - On espère qu'une suite de question émerge (il s'agit d'un arbre de décision, presque).
  - On relève cette suite de question.

- Exercice 3 : "testing"
  - On propose aux élèves de tester cette suite de questions. Ils vont classifier ~10 images d'affilée, et on verra les réponses (% de réussite) à la fin.
  - On recommence, mais avec des animaux "non-standards" :
    - poisson-volant (ailes, mais vit sous l'eau)
    - crabe (plein de pattes, mais vit sous l'eau)
    - poule (des ailes, mais vit sur terre)
    - pégase
  Haha ! Ça ne marche plus !

- Exercice 4 (WIP) : "adversarial examples"
  - On améliore le classifieur ?
  - Adversarial examples : modifier un animal pour qu'il soit mal classifié.
  - Adversarial examples : images ridicules qui trompent le clasifieur (une enclume avec des ailes).
