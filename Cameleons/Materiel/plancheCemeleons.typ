// Les marges ont étés calculées pour que les caméléons soient bien alignés.
// Il faut imprimer sur un seul coté et coller les deux feuilles dos à dos avec un
// carton entre les deux pour que les caméléons soient bien alignés. Il suffit
// ensuite de découper les caméléons pour avoir de nouveaux pions pour le jeu.
#set page(margin: 1.5em)

#grid(
	columns: 9,
	column-gutter: 2.5em,
	row-gutter: 1.7em,
	..range(0,117).map(_ =>
		image("camaleonVert.png", width: 4em)
	)
)

#pagebreak()

#grid(
	columns: 9,
	column-gutter: 2.5em,
	row-gutter: 1.7em,
	..range(0,117).map(_ =>
		image("camaleonRouge.png", width: 4em)
	)
)