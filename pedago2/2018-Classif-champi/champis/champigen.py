from random import random

to_write = ""
for k in range(25):
	to_write += "######### new champi ########\n"
	
	
	valchap = int(random()*4)
	to_write += "chapeau = "+ (valchap==0)*'bell shape' + (valchap==1)*'convexe' + (valchap==2)*'flat' + (valchap==3)*'conique' + '\n'

	valcol = int(random()*3)
	to_write +="couleur = "+ ['vert','rouge','bleu'][valcol] + '\n'
	print(valcol, ['vert','rouge','bleu'][valcol])
	print(to_write)
	valpoint = int(random()*2)
	to_write += (valpoint==0)*'pas de' + " points marrons" + '\n'

	valcoler = int(random()*3)
	to_write +="nombre de collerettes = "+ str(valcoler) + '\n'

	valmort = int(random()*2)
	to_write += (valmort==0)*'pas' + " mortel" + '\n\n'

fichier = open("data.txt", "w")
fichier.write(to_write)
fichier.close()

