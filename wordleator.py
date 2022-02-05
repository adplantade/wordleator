import sys
from random import choice
from itertools import filterfalse

if(len(sys.argv)!=2):
	print("faut 1 argument !")
	quit()
lettres = int(sys.argv[1])
mots = open(f"{lettres}lettres.txt","r").read().splitlines()
for i in range(6):
	print(f"mot random : {choice(mots)}")
	motChoix = input("mot entré : ").upper()
	while(motChoix not in mots):
		print("Ce mot n'est pas possible")
		motChoix = input("mot entré : ").upper()
	res = input("couleurs (N/J/V) : ").upper()
	for ind in range(len(res)):
		if(res[ind]=="N"):
			mots[:] = filterfalse(lambda x: motChoix[ind] in x, mots)
		if(res[ind]=="J"):
			mots[:] = filterfalse(lambda x: motChoix[ind]==x[ind], mots)
		if(res[ind]=="V"):
			mots[:] = filterfalse(lambda x: motChoix[ind]!=x[ind], mots)

	print(f"{len(mots)} mots possibles")