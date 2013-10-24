#-*- coding: utf-8 -*-
#et enkelt spill
from sys import exit

import rom1
import rom2
import rom3


                
def dead(why):

        print "Feil! Du maa skrive rom3! Begynn paa nytt!"
        exit(0)
        
def start():
        print """
			Velkommen til eventyrland. Bli med paa et kjempe morsomt spill!
                
			Trykk CTRL-C hvis du IKKE har lyst til aa bli med!
				
			Trykk ENTER for aa bli med! Kom igjen, ikke vaer kjip naa!
				
			Hva velger du?
                 """
        
        continiue = raw_input("> ")
        
        print """ Du er inne i det magiske slottet. 
		Du maa beseire den onde Styggen, klarer du det faar du premie.
        skriv inn rom3, og det magiske spillet vil starte.."""
        
        next = raw_input("> ")
        
	if next == "rom3":
					rom3.steinsaksogpapir()
	
        
        else:
                dead("Feil! Du maa skrive rom3! Begynn paa nytt!")
  
start()             
