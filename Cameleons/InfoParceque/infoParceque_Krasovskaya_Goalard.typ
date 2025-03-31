#set text(font: "Fira Sans")
#set page(margin: 3.6em)

#let block = [
	#align(center)[
		#text("Caméléons", weight: "bold", size: 2em)
	]
	C'est de l'informatique parce qu'on a fait de la *logique*. Malheureusement, les ordinateurs ne fonctionnent pas avec des Caméléons mais avec des $0$ et des $1$ que l'on appelle *bits*. Si on considère que les caméléons rouges sont des $0$ et les caméléons verts des $1$ alors les nids de Caméléon sont ce qu'un ordinateur utilise pour faire des opérations basiques: ce sont des *portes logiques* qui permettent de faire des opérations sur ces *bits*.

	#align(center)[
		#grid(
			columns: (1fr, 1fr, 1fr),
			column-gutter: 5em,
			[Porte *OU*], [Porte *ET*], [Porte *NON*],
			
			image("ou.png", height: 5em),
			image("and.png", height: 5em),
			image("non.png", height: 5em),
			[
				Il faut pour que le caméléon du bas soit vert que celui de gauche *OU* celui de droite soit vert.
			],
			[
				Il faut pour que le caméléon du bas soit vert que celui de gauche *ET* celui de droite soit vert.
			],
			[
				Quand les caméléons rencontrent un oiseau, ils changent de couleur.
			]
		)
	]
]

#block
#block
#block