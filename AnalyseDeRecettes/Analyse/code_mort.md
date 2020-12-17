On va essayer de trouver le code inutile.
Il se découpe en deux catégories distinctes
Premièrement il y a le code qui n'est jamais exécuté Cela arrive quand on a une condition qui ne peut pas être vrai.
Ce code ne prend pas d'effort mais il rend le programme plus difficile a lire, l'effacer permet donc de rendre le code plus
lisible et de sauver de la mémoire

La deuxième catégorie de code mort est celui que l'on exécute mais qui n'est pas utile.
Par exemple si un bloque de code sert a produire une valeur X mais que cette dernière n'est
jamais utilise par la suite, alors c'est du temps et des ressources perdu.


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
