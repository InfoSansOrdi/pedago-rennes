Ce document présente une activité débranché basé sur le langage décris dans
[apprendre_langage](../apprendre_langage.md) pour introduire [l'analyse d'expression
disponible](https://en.wikipedia.org/wiki/Available_expression) aux apprenants.
Cette analyse a pour objectif de simplifier les recettes et de les rendre plus
simple à faire. Dans cette activité, nous espérons que les apprenants
apprendrons des conce pour rendre plus efficace.

# Différentes vision possible

Si les apprenants ne sont pas très friants de la simple idée de simplification
de recettes. L'activité peut être modifiée pour ressembler plus à un jeu. Pour
chaque programme, il peut être demandé à l'apprenant de réduire le nombre
d'occurences d'un operatuer en dessous d'un certain seuil. Avec un objectif
aussi claire les apprenants pourraient avoir plus de volonté à faire l'activité.

# Invariance de la sémantique des recettes

Il est important pendant l'activité de rendre claire que la semantique du
programme ne doit pas être changé. Si les apprenants ont déjà fait des activité
lié à la programation et la compréhension de la « bêtise » d'un ordinateur
([Blasons](../../Blasons), [Cargobot](../../Cargobot), etc...), il est possible
de s'appuyer dessus. Une façon de présenter la nécessité de l'invariance de la
sémantique pourrait être que les recettes d'alchimie peuvent être dangeureuses
si elles ne sont pas exécutées précisément. Ce n'est bien sûr qu'une suggestion.

# Suggestion de progression pour l'activité

Dans cette sections, nous suggérons un déroulement pour l'activité. Des
programmes seront présenté dans une syntaxe arbitraire car une bonne syntaxe
n'as pas encore été décidé.

Si la mise en pratique de l'activité montre des défauts ou si quelque chose vous
semble étrange, n'hésitez pas à l'adapter ou à proposer des modifications.

La progression se fait en modifiant des recettes de plus en plus complexe. Les
apprenants doivent être invité à executer les recettes pour qu'ils puissent se
rendre compte de la nécessité de simplification. Chaque nouvelle recette
introduis un nouveau concepte de l'analyse.

## Opérateur

Pour ces programme nous allons nous donner un opérateur qui est une fonction pas
très longue mais qui n'est pas immédiate à exécutée, donc embêtante lorsqu'il y
en a plusieurs dans une recette.
```
Function(VarB) :
    If VarB = Triangle
        -> Carré
    If VarB = Pentagone
        -> Triangle
    If VarB = Carré
        -> Pentagone
```
Cette fonction prend une variable et produit un objet géométrique. Nous
réprésenteron le fait de stocker le résultat de la fonction dans un variable
`VarX` par `-> VarX Function(VarY)`.

## Premier programme (Base)

```
-> Var3 Function1(Var1) 
If Var3 = Triangle
    Var3 Triangle -> Var2 Carré
If Var3 = Carré
    Var3 Carré -> Var2 Triangle
-> Var4 Function1(Var1)
-> Var5 Function1(Var1)
```

Dans ce programme, il est possible de remplacer toutes les occurences de
`-> VarX Function1` excepté la première par `Var3 -> VarX`. Il donne
une demonstration simple qu'un programme peut être simplifié.

La solution est la suivante,
```
-> Var3 Function1(Var1) 
If Var3 = Triangle
    Var3 Triangle -> Var2 Carré
If Var3 = Carré
    Var3 Carré -> Var2 Triangle
Var3 -> Var4
Var3 -> Var5
```

## Deuxième programme (Attention à la sémantique !)

```
-> Var3 Function1(Var1) 
If Var3 = Triangle
    Var3 Triangle -> Var2 Carré
If Var3 = Carré
    Var3 Carré -> Var2 Triangle
-> Var4 Function1(Var1)
Var2 -> Var1
-> Var5 Function1(Var1)
```

Ce programme est très similaire au premier, mais la valeur de `Var1` est changé
juste avant la dernière occurence de `-> VarX Function1(Var1)`. Ce programme
permet de montrer les limitations de l'algorithme naïf. Si une variable
paramêtre est changé, on ne peut pas remplacer les occurences suivantes.

La solution est la suivante,
```
-> Var3 Function1(Var1) 
If Var3 = Triangle
    Var3 Triangle -> Var2 Carré
If Var3 = Carré
    Var3 Carré -> Var2 Triangle
Var3 -> Var4
Var2 -> Var1
-> Var5 Function1(Var1)
```
    
## Troisième programme (Attention à la sémantique, mais dans les branches !)

```
-> Var3 Function1(Var1) 
If Var3 = Triangle
    Var3 Triangle -> Var2 Carré
If Var3 = Carré
    Var3 Carré -> Var2 Triangle
-> Var4 Function1(Var1)
If Var2 = Pentagone
    Var2 Pentagone -> Var1 Triangle
-> Var5 Function1(Var1)
```

Ici, `Var1` est changé conditionellement. Dans ce cas, il faut particuliérement
faire attention que changer le programme ne change pas sa sémantique. Ce n'est
pas parce que la sémantique ne change pas dans beaucoup d'exécution qu'elle
n'est pas changé dans une exécution.


La solution est la suivate,
```
-> Var3 Function1(Var1) 
If Var3 = Triangle
    Var3 Triangle -> Var2 Carré
If Var3 = Carré
    Var3 Carré -> Var2 Triangle
Var3 -> Var4
If Var2 = Pentagone
    Var2 Pentagone -> Var1 Triangle
-> Var5 Function1(Var1)
```

## Quatrième programme (Graphe de flot de contrôle)

```
-> Var3 Function1(Var1) 
If Var3 = Triangle
    Var3 Triangle -> Var2 Carré
If Var3 = Carré
    Var3 Carré -> Var2 Triangle
Var3 -> Var4
If Var2 = Pentagone
    Var2 Pentagone -> Var1 Triangle
Else
    -> Var2 Function(Var1)
-> Var5 Function1(Var1)
```

Ce programme a deux branche mutuellement exclusive. La première branche modifie
la variable `Var1` rendant l'expression `Function(Var1)` indisponible. Mais la
deuxième branche met l'expression `Function(Var1)` dans la variable `Var2`. Les
apprenant ici pourrait penser qu'on ne peut pas faire de modification dans la
deuxième branche. Or, ce n'est pas le cas car cette branche est exclusive à
l'autre. Ce programme est très bien pour introduire le concepte de [graphe de
flot de contrôle](https://fr.wikipedia.org/wiki/Graphe_de_flot_de_contr%C3%B4le)
aux apprenants, car cette représentation permet de voir clairement l'exclusivité
des deux branches.

La solution est la suivante,
```
-> Var3 Function1(Var1) 
If Var3 = Triangle
    Var3 Triangle -> Var2 Carré
If Var3 = Carré
    Var3 Carré -> Var2 Triangle
Var3 -> Var4
If Var2 = Pentagone
    Var2 Pentagone -> Var1 Triangle
Else
    Var3 -> Var2
-> Var5 Function1(Var1)
```

## Cinquième programme (Annotations et algorithme complet)

```
-> Var2 Function1(Var1)
-> Var3 Function1(Var2)
-> Var6 Function1(Var3)
If Var2 = Pentagone
    -> Var4 Function1(Var1)
If Var4 = Carré
    Var4 Carré -> Var4 Pentagone
    -> Var1 Triangle
-> Var7 Function1(Var3)
-> Var5 Function1(Var2)
If Var5 = Triangle
    -> Var4 Pentagone
    -> Var2 Triangle
Else
    -> Var4 Function1(Var2)
Var4 -> Var6
-> Var5 Function1(Var3)
-> Var4 Function1(Var2)
```

Ce dernier programme est bien plus grand et contient tout les concepts vue
précédemment. Les apprenants risquent de s'y perdre si ils n'utilisent pas
de graphe de flot de contrôle. De plus, pour simplifier la vie des apprenants,
il est bon de les pousser à annoter leur graphe de flot de contrôle. On peut
faire remarquer au apprenant que c'est exactement la façon dont fonctionne
l'algorithme d'analyse des expression disponibles.

<!--
Solution5 :
    -> Var2 Function1(Var1)
    -> Var3 Function1(Var2)             { (Var2, Function1(Var1)) }
    -> Var6 Function1(Var3)             { (Var2, Function1(Var1)), (Var3, Function1(Var2)) }
    If Var2 = Pentagone                 { (Var2, Function1(Var1)), (Var3, Function1(Var2)), (Var6, Function1(Var3)) }
        Var2 -> Var4                    { (Var2, Function1(Var1)), (Var3, Function1(Var2)), (Var6, Function1(Var3)) }
    If Var4 = Carré                     { (Var2, Function1(Var1)), (Var3, Function1(Var2)), (Var6, Function1(Var3)) }
        Var4 Carré -> Var4 Pentagone    { (Var2, Function1(Var1)), (Var3, Function1(Var2)), (Var6, Function1(Var3)) }
        -> Var1 Triangle                { (Var2, Function1(Var1)), (Var3, Function1(Var2)), (Var6, Function1(Var3)) }
    Var6 -> Var7                        { (Var3, Function1(Var2)), (Var6, Function1(Var3)) }
    Var3 -> Var5                        { (Var3, Function1(Var2)), (Var6, Function1(Var3)), (Var7, Function1(Var3)) }
    If Var5 = Triangle                  { (Var3, Function1(Var2)), (Var6, Function1(Var3)), (Var7, Function1(Var3)), (Var5, Function(Var2)) }
        -> Var4 Pentagone               { (Var3, Function1(Var2)), (Var6, Function1(Var3)), (Var7, Function1(Var3)), (Var5, Function(Var2)) }
        -> Var2 Triangle                { (Var3, Function1(Var2)), (Var6, Function1(Var3)), (Var7, Function1(Var3)), (Var5, Function(Var2)) }
    Else
        -> Var4 Function1(Var2)
    Var4 -> Var6
    -> Var5 Function1(Var3)
    -> Var4 Function1(Var2)
-->

## Autres Concept Intéressant

Il pourrait être intéressant de regarder des recettes ayant des instructions du
type `-> Var1 Function1(Var1)`. Ce la permettrai de montrer la nécessité de
prendre en compte ce qui est disponible à l'entré et ce qui ne l'est plus à la
sortie. Plutot que de s'intéresser à ce qui est disponible seulement à un seul
endroit (comme ça a probablement était fait dans le grand programme).
