# Hapt'n'Kart

## Description de l'activité

* **Pensée algorithmique** ☆
  * Encodage d'un message.
  * Conception des stimuli en s'assurant qu'ils sont discriminables par une majorité de la population.
* **Abstraction** ○
* **Décomposition** ○
* **Généralisation et motifs** ☆☆
  * Reconnaissance de motifs.
  * Interprétation des motifs comme un message transmis, une action, ...
* **Évaluation** ☆
  * Évaluer la qualité de la correspondance entre un message transmis et un message reçu.
* **Logique** ○

## Déroulement des activités

TODO : lien vers la feuille de prép

### Activité 1

* **Introduction** : Vous êtes au volant de votre simulateur de voiture Mario Kart. Vous voulez changer la climatisation ou la radio, mais vous ne pouvez pas quitter la route des yeux sous peine de perdre la course (vous êtes sur la course arc-en-ciel). Mais votre turbo-simulateur 2000 possède une technologie des plus avancées ! Vous avez en effet la possibilité de contrôler votre simulateur à l’aide de gestes dans l’air. Pour savoir où vous en êtes, cette interface va vous envoyer une sensation tactile permettant d’identifier la commande en cours, de valider une interaction, etc... Une des choses importantes est donc de pouvoir reconnaître le “message” envoyé par l’interface.
* **Objectifs** : Transférer un message à quelqu'un qui ne peut utiliser que son sens du toucher.
* **Matériel** : Un lot de "jetons" de différentes formes/tailles/poids(matériau) par table. Les formes peuvent être imprimées à partir des fichiers `.svg` [ici](https://github.com/InfoSansOrdi/pedago-rennes/tree/trunk/pedago2/2021-Haptique).
* **Consignes** : Il faut au moins deux personnes. L'une d'entre elles prend le rôle de *messager* et les autres prennent le rôle de *récepteur*. Le messager à un message à faire passer, initialement sous forme d'une suite de chiffres (ex : 1 2 1 1 2) et les récepteurs  doivent retrouver le message. Le récepteur va choisir une suite de jeton qu'il alignera devant les récepteurs afin de représenter le message à transmettre. Le récepteur doit avoir les yeux fermés pour ne pas voir les jetons. Le récepteur va essayer de retrouver le message initial en touchant successivement les jetons. Si il y a plusieurs récepteurs, ils doivent tous reconstruire l’entièreté du message. Une fois que le récepteur a assigné une valeur, le messager pose un morceau de papier sur le jeton (ou écrit sur une feuille à côté) pour se souvenir de la valeur assignée au jeton.
* **Extensions / aides** :
  * Aide : au lieu de transmettre des chiffres, on transmet des formes (cercle, carré, triangle, ...).
  * Aide : On donne aux messagers et récepteurs une liste de messages possibles (qui peuvent correspondre à des actions comme "tourner à droite", "ralentir", "le chauffage a été augmenté"). Cela permettrait probablement de mieux comprendre le processus "d'évaluation" : la transmission est bonne si le récepteur arrive à retrouver la bonne action. Cela permet aussi d'avoir quelques erreurs.
  * Extension : le récepteur n'a pas le droit de toucher un jeton qu'il a déjà touché auparavant.
  * Extension : transmettre des messages plus long.
  * Extension : transmettre des messages avec un plus grand alphabet.
* **Questions à poser** : 
  * Quelles difficultés ont été rencontrées ?
  * Quelles stratégies ont été utilisées pour transmettre le message ?
  * Quelles stratégies ont été utilisées pour reconnaître les formes ?
* **Ce qu'on en tire** :
  * C'est de l'informatique parce que :
    * [En/Dé]codage de messages : quand on veut transmettre un message et que l'on veut qu'il soit compris par tout le monde, il faut lui trouver une représentation intermédiaire "universelle"
    * Interactions Humain-Machine : On interagit avec une machine (ici machine → humain), qui nous permet d'améliorer des performances, améliorer l'immersion. Comment créer une interface qui permette des interactions sans stimulation visuelle.
  * Côté perception :
    * La perception tactile permet de discriminer des formes / poids / textures. On utilise des techniques différentes pour percevoir différentes modalités. Par exemple, on va soupeser un objet pour déterminer son poids, on va poser sa main dessus pour déterminer sa température, on va appuyer dessus avec un doigt pour obtenir sa dureté, on va faire glisser le doigt sur la surface pour déterminer sa texture, on va entourer l'objet pour déterminer sa forme.
    * La perception humaine a ses limites. Si deux objets sont différents mais "proches" l'un de l'autre, il sera plus compliqué de les différencier. Il existe plusieurs façons d'évaluer la perception, par le calcule de seuils de détection/différenciation.


Exemple de déroulé :
* Le premier jeton est arbitrairement attribué à un 1.
* Lorsque le récepteur touche le second jeton, il se rend compte qu'il est différent du premier → c'est un 2.
* Lorsqu'il touche le troisième jeton, il se rend compte qu'il est identique au premier → c'est un 3.

**Remarque** : L'important n'est pas nécessairement que les "1" soient perçus comme des "1", mais plutôt que tous les "1" soit perçus comme de la même façon. Par exemple, si le message à envoyer est 01110211202 et que le message reçu est 0**1**220122102, on peut considérer qu'il n'y a qu'une seule erreur, puisque tous les "2" envoyés sont bien interprétés de la même façon ("1" reçu), et de même pour les "0" ("0" reçu), mais un "1" est interprété comme "1" alors que tous les autres sont interprétés comme "2". L'exemple peut être donné au tableau et les élèves peuvent appeler les encadrants pour vérifier. Un autre élève peut essayer de noter un autre exemple pour vérifier la compréhension.

### Activité 2

* **Introduction** : Vous avez maintenant un copilote ! Le copilote peut regarder derrière et doit prévenir le pilote lors de l’arrivée d’une carapace. Les bruits du moteur et de la musique sont trop forts pour qu’ils puissent communiquer à l’oral. De plus, les deux personnes ne doivent pas quitter la route des yeux.
* **Objectifs** : Transférer un message à quelqu'un qui ne peut utiliser que son sens du toucher, sans voir ce qu'on envoie.
* **Matériel** : Un lot de "jetons" de différentes formes/tailles/poids(matériau) par table. Les formes peuvent être imprimées à partir des fichiers `.svg` [ici](https://github.com/InfoSansOrdi/pedago-rennes/tree/trunk/pedago2/2021-Haptique).
* **Consignes** : Comme l'activité 1, mais le messager ne peut aussi utiliser que son sens du toucher. Sachant qu'il doit quand même connaître le message à transmettre, on peut utiliser un paravent pour cacher le lot de jeton.
* **Extensions** : Idem activité 1.
* **Questions à poser** : 
  * Est-ce que les résultats ont été aussi bons ?
  * Est-ce que la difficulté a augmenté/diminué ?
  * Quels problèmes ont été rencontrés ? Comment ont-ils été résolus ? Pourquoi ces problèmes ce sont posés ?
* **Ce qu'on en tire** :
  * Côté perception :
    * La perception n’est pas identique pour tout le monde.
    * La personne qui conçoit les stimuli n’est généralement pas la même que celle qui va le ressentir.
    * Il faut un stimulus assez “général” pour que tout le monde puisse les différencier.
    * [Le messager sait ce qu’il doit envoyer et sa perception peut-donc être biaisé en fonction de ses attentes]
  * C'est de l'informatique parce que :
    * On peut calculer des seuils de différenciations moyens selon différentes modalités (courbure, longueurs, ...). Quand on veut créer deux stimuli et que l'on souhaite qu'ils soit perçu comme étant différents par le plus grand nombre, il faut s'assurer que la différence entre les deux est supérieure au seuil.

### Conclusion

L'haptique c'est quoi ?

C'est la science qui étudie le toucher.

Pourquoi on s'y intéresse ?

C'est un sens qui sert à énormément de choses, sans qu'on s'en rende compte : c'est ce qui permet de savoir comment on bouge sans regarder, ce qui nous permet d'attraper des objets sans les faire tomber, de marcher sans perdre l'équilibre (en partie), ...
Et c'est aussi un sens qui dont le fonctionnement et les capacités ne sont pas totalement connues, même aujourd'hui !

Où on se sert d'haptique ?

En réhabilitation (aider les personnes à marcher ou bouger un membre), immersion en réalité virtuelle ou pour des jeux vidéos (pouvoir toucher les objets), télé-opération (contrôler un robot à distance et sentir ce qu'il sent), contrôle sans les yeux (par exemple, changer le climatisation dans la voiture sans dévier le regard).

