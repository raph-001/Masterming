from random import randint

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


print("\nIl y a six couleurs (bleu, blanc, noir, rouge, vert, jaune) et il suffit juste de les ecrire en entier avec un espace ex: bleu rouge rouge vert\n")
bon_mais_mal_place = 0
bom_et_bien_place = 0
Serie_de_couleur_a_trouver = ("")
compteur_de_coups = 0
couleur_possible = ("bleu","rouge","jaune","vert","noir","blanc")
continuer = ""
couleur_1 = [(couleur_possible)[randint(0, 5)],0]

couleur_2 = [(couleur_possible)[randint(0, 5)],0]

couleur_3 = [(couleur_possible)[randint(0, 5)],0]

couleur_4 = [(couleur_possible)[randint(0, 5)],0]


while compteur_de_coups != 10 and bom_et_bien_place != 4 :
	continuer = ""
	compteur_de_coups += 1
	couleur_1[1] = 0
	couleur_2[1] = 0
	couleur_3[1] = 0
	couleur_4[1] = 0
	bom_et_bien_place = 0
	bon_mais_mal_place = 0
	while continuer != "correct":
		try:
			serie_4_demandee = input("D'apres vous, quelle est la serie choisie aleatoirement ? \n")
			print()

			serie_4_demandee = serie_4_demandee.split()

			liste = [serie_4_demandee, [0, 0, 0, 0]]
				

			if couleur_1[0] == liste[0][0]:
				bom_et_bien_place += 1
				liste[1][0] = 1
				couleur_1[1] = 1

			if couleur_2[0] == liste[0][1]:
				bom_et_bien_place += 1
				liste[1][1] = 1
				couleur_2[1] = 1

			if couleur_3[0] == liste[0][2]:
				bom_et_bien_place += 1
				liste[1][2] = 1
				couleur_3[1] = 1

			if couleur_4[0] == liste[0][3]:
				bom_et_bien_place += 1
				liste[1][3] = 1
				couleur_4[1] = 1
				
			continuer = "correct"
		except IndexError:
			print("Oups... Ceci n'est pas correct reessayer avec bien 4 couleurs...\n")
	compteur = 1

	for i in "abc":
		if liste[1][compteur] == 0 :
			if couleur_1[1] == 0 :
				if couleur_1[0] == liste[0][compteur]:
					bon_mais_mal_place += 1
					liste[1][compteur] = 1
					couleur_1[1] = 1
		compteur += 1

	compteur = 0

	for i in "abc" :
		if liste[1][compteur] == 0 :
			if couleur_2[1] == 0:
				if couleur_2[0] == liste[0][compteur] :
					bon_mais_mal_place += 1
					liste[1][compteur] = 1
					couleur_2[1] = 1
		compteur -= 1

	compteur = 1

	for i in "abc":
		if liste[1][compteur] == 0 :
			if couleur_3[1] == 0:
				if couleur_3[0] == liste[0][compteur] :
					bon_mais_mal_place += 1
					liste[1][compteur] = 1
					couleur_3[1] = 1
		compteur -= 1

	compteur == 2

	for i in "abc":
		if liste[1][compteur] == 0 :
			if couleur_4[1] == 0:
				if couleur_4[0] == liste[0][compteur] :
					bon_mais_mal_place += 1
					liste[1][compteur] = 1
					couleur_4[1] = 1
		compteur -= 1

	print("Il y a {0} couleur(s) bien placee(s) et {1} couleur(s) mal(s) placee(s)\n".format(bom_et_bien_place, bon_mais_mal_place))

if bom_et_bien_place == 4 :
	print("bravo vous avez gagne ! ")

else:
	print("Malheureusement vous n'avez pas trouve la bonne combinaison en moins de 10 coups, vous avez perdu. La bonne combinaison etait \n: {0} {1} {2} {3}".format(couleur_1[0], couleur_2[0], couleur_3[0], couleur_4[0]))


	