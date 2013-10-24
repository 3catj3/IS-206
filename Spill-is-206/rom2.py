# -*- coding: utf-8 -*-
from sys import exit

import rom1


def dead (grunn):
		print "Du skriver feil, du kan kun velge mellom kake eller kaffe eller rom1! (skriv inn kake,kaffe eller rom1)"
		rom2()


def rom2():
        print """\n  				Velkommen til rom2.
				Her kan du velge kake eller kaffe!
				Liker du ikke kake eler kaffe, gaa til rom1 da!
				Hva velger du?
                 
				 """
        
	next = raw_input("> ") 	#presenterer spørsmål til spilleren, får input fra spilleren og returnerer datainput.
        
        
        if next == "kake":
			          print "Takk for at du spilte, her har du kaka" #hvis input= kake, printes: takk for at du spilte, her har du kaka..
        elif next == "kaffe":
					print "Takk for at du spilte, her har du en kopp kaffe"	
			
        elif next == "rom1": #hvis input er rom1 vil rom1 filen og funksjon rom1 kalles.
                   rom1.rom1()	          
        else:
              dead  ("Du skriver feil, du kan kun velge mellom kake eller kaffe eller rom1! (skriv inn kake,kaffe eller rom1)") 
			  #hvis input er annet enn kake,kaffe,rom1 blir denne mld printet.
              

