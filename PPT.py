import sys
import random

print "####################################################"
print "############# JOC PEDRA PAPER I TISORA #############"
print "####################################################"
print " "
print " "
print "Polsa la combinacio PE per la PEDRA"
print "Polsa la combinacio PA pel PAPER"
print "Polsa la combinacio TI per la TISORA"
print "Polsa la combinacio SO per SORTIR"
opcio = raw_input("Quina vols escollir?")
print " "
opcions = ["pedra", "paper", "tisora"]
randomop = random.randint(0,2)
random = opcions[randomop]
print "Ordinador ha triat: " + random + "\n"
print "El resultat es:"
if opcio == random:
	print "Empat"
if opcio == "PE" and random == "tisora":
	print "Guanya Jugador"
if opcio == "PA" and random == "pedra":
	print "Guanya Jugador"
if opcio == "TI" and random == "paper":
	print "Guanya Jugador"
else: 
	print "Guanya Ordinador"

print "FINAL"

