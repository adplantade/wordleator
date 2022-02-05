f = open("ods6.txt","r")
lignes = f.readlines()
files = []
for i in range(20):
	tmp = open(f"{i}lettres.txt","w")
	files.append(tmp)

for mot in lignes:
	files[len(mot)-1].write(mot)

for fl in files:
	fl.close()