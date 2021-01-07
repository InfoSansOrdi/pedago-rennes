# Principe
On souhaite trouver le code inutile dans le programme. On s'intéresse a deux types de code inutile : 
Premièrement le code qui n'est jamais exécuté Cela arrive lorsque l'on a une condition qui ne peut pas être vrai.
Ce code ne prend pas d'effort mais il rend le programme plus difficile a lire, l'effacer permet donc de rendre le code plus
lisible et de sauver de la mémoire.

La deuxième catégorie de code mort est celui que l'on exécute mais dont le résultat n'est pas utilisé.
Cette analyse n'est pas trop complexe avec notre programme car il y n'y a pas d'effet de bord complexe.
Par exemple si un bloque de code sert a produire une valeur X mais que cette dernière n'est
jamais utilise par la suite, alors calculer X est optionnel.

# Exemples
On donne des exemples canonique, c'est à dire qu'ils portent l'idée pour chaque type de code mort.
Libre a vous de les arranger comme vous le souhaitez pour donner des exercices interessant.
Nous conseillons tout de même de commencer par des programmes ne comportant qu'un type de code mort avant de les mélanger.

## Code jamais exécuté

On commence par un exemple de programme avec du code qui n'est jamais exécuté. Dans la première partie du If, Var3 ne peut pas être égale à Rond donc on prendra toujours la branche else.
    ```
Function1(VarB) :
    If VarB = Triangle
        -> Carré
    If VarB = Pentagone
        -> Triangle
    If VarB = Carré
        -> Pentagone


Program1:
    -> Var3 Function1(Var1)
    If Var3 = Rond
        ...
    Else
        If Var3 = Triangle
            Var3 Triangle -> Var2 Carré
        If Var3 = Carré
            Var3 Carré -> Var2 Triangle
```
On peut ainsi remplacer ce code par une version sans code mort
    ```
Function1(VarB) :
    If VarB = Triangle
        -> Carré
    If VarB = Pentagone
        -> Triangle
    If VarB = Carré
        -> Pentagone


Program1:
    -> Var3 Function1(Var1)
    If Var3 = Triangle
        Var3 Triangle -> Var2 Carré
    If Var3 = Carré
        Var3 Carré -> Var2 Triangle
```

## Résultat jamais utilisé
On présente ensuite un exemple de programme avec un résultat calculé mais jeté avant d'être utilisé.
KLa valeur dans VarC est abandonné quand la fonction retourne et n'est pas utilisé dans ce laps de temps.
```
Function2(VarB) :
    If VarB = Triangle
        -> VarC Carré
    If VarB = Pentagone
        -> VarC Triangle
    If VarB = Carré
        -> VarC Pentagone

    If VarB = Triangle
        -> Carré
    If VarB = Pentagone
        -> Triangle
    If VarB = Carré
        -> Pentagone
```

On propose une autre variante où la valeur est réécrite avant la prochaine utilisation.
```
Function2(VarB) :
    If VarB = Triangle
        -> VarC Carré
    If VarB = Pentagone
        -> VarC Triangle
    If VarB = Carré
        -> VarC Pentagone

    -> VarC Rond

    If VarB = Triangle
        -> Carré
    If VarB = Pentagone
        -> Triangle
    If VarB = Carré
        -> Pentagone
```
