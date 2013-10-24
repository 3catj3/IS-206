#-*- coding: utf-8 -*-
#et enkelt spill
from sys import exit

import rom1 #importert de andre filene som hører til i spillet for at de kan kjøres sammen
import rom2
import rom3


                
def dead(why):

        print "Feil! Du maa skrive rom3! Begynn paa nytt!"
        exit(0)                          #hvis annet input enn rom3, kjøres funksjonen exit og man går ut av fila.
  # Her starter funksjonen start
def start():
        print """
			Velkommen til eventyrland. Bli med paa et kjempe morsomt spill! 
                
			Trykk CTRL-C hvis du IKKE har lyst til aa bli med!
				
			Trykk ENTER for aa bli med! Kom igjen, ikke vaer kjip naa!
				
			Hva velger du?
                 """
        
        continiue = raw_input("> ")   #presenterer spørsmål til spilleren, får input fra spilleren og returnerer datainput.
        
        print """ Du er inne i det magiske slottet. 
		Du maa beseire den onde Styggen, klarer du det faar du premie.
        skriv inn rom3, og det magiske spillet vil starte.."""
                               
        next = raw_input("> ")
        
	if next == "rom3":
					rom3.steinsaksogpapir() #if løkka: kjører fila rom3 og funksjonen steinsaksogpapir. (hvis input er rom3)
	
        
        else:
                dead("Feil! Du maa skrive rom3! Begynn paa nytt!") #hvis annet input enn rom3, kjøres denne "feilmld" og exit (se toppen)
  
start()             
