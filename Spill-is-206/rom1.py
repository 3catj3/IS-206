# -*- coding: utf-8 -*-
from sys import exit


import rom2

def dead (grunn):
		print "Du skriver feil, du kan kun velge mellom brus eller is eller rom2!(skriv inn brus,is eller rom2)"
		rom1() #hvis annet input enn brus,is,rom2 vil denne funksjonen kjøre og funksjon rom1 kjører på nytt.


def rom1():
        print """\n	WOOHOOO!!!
        Du kan velge brus eller is!
	Liker du ikke brus eller is, gaa til rom2 og velg mellom andre premier!
        Hva velger du?
                 
				 """
        
        next = raw_input("> ")
        
        
                             #If løkka: hvis input er rom2 vil rom2 filen og funksjon rom2 kalles. 
        if next == "brus":   # hvist spillerens input er feks brus, kjøres print: takk for at du spilte, her har du ei brus.
					print "Takk for at du spilte, her har du ei brus" 
        elif next == "is":
					print "Takk for at du spilte, her har du en is"	
			
        elif next == "rom2":
                   rom2.rom2()	          
        else:
              dead ("Du skriver feil, du kan kun velge mellom brus eller is eller rom2!(skriv inn brus,is eller rom2") 
			  
              
