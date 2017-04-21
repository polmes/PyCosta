print "####################################################"
print "################# JOC DEL PENJAT ###################"
print "####################################################"
print " "
print " "
print " Comencem el joc "
penjat = [' ______________',
	  ' |	     |',
	  ' |	     |',
	  ' |	     O',
	  ' |	    /|\\',
	  ' |	     |',
	  ' |	    / \\',
	  '_|_		'
]
cont = 0
corr = 0
while (cont < 8 and corr < 4):
	print corr
	i = 0
	lletra = raw_input("Escull una lletra\n")
	if lletra not in "hola":
		cont = cont + 1
		if cont == 8:
			print "\n     PENJAT"
		while (i < cont):
			print penjat[i]
			i = i + 1
	
	else:
	  	corr = corr + 1

if cont == 7:
	print "Has perdut, final del joc!!"
elif corr == 4:
	print "Has guanyat, final del joc!!"

