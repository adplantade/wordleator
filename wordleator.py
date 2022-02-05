import sys
from random import choice
from itertools import filterfalse

if(len(sys.argv)!=2):
	print("faut 1 argument !")
	quit()
lettres = int(sys.argv[1])
mots = open(f"{lettres}lettres.txt","r").read().splitlines()
motChoix = ""
tmp = open(f"{lettres}lettres.txt","r").read().splitlines()
for i in range(6):
	for ind in motChoix:
		tmp[:] = filterfalse(lambda x: ind in x, mots)
	print(f"mot random : {choice(mots)}, mot couvrant : {choice(tmp) if(len(tmp)>10) else tmp}" if(len(mots)>30) else mots)
	motChoix = input("mot entré : ").upper()
	while(motChoix not in mots):
		print("Ce mot n'est pas possible")
		motChoix = input("mot entré : ").upper()
	res = input("couleurs (N/J/V) : ").upper()
	if(res=="V"*lettres):
		print("Eh, marche pas si mal ce prog'")
		quit()
	for ind in range(len(res)):
		if(res[ind]=="N"):
			mots[:] = filterfalse(lambda x: motChoix[ind] in x, mots)
		if(res[ind]=="J"):
			mots[:] = filterfalse(lambda x: motChoix[ind]==x[ind], mots)
		if(res[ind]=="V"):
			mots[:] = filterfalse(lambda x: motChoix[ind]!=x[ind], mots)

	print(f"{len(mots)} mots possibles")