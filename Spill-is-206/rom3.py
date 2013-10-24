# -*- coding: UTF-8 -*-
##
## STEINSAKSPAPIR
##
 
import random
import rom1
import rom2
def steinsaksogpapir():
    print """\nSTEIN SAKS OG PAPIR!
Klarer du aa vinne over Styggen? Beseir han og du kan vinne fine premier!

Lykke til..."""
    while True:
        try:
            maxpoeng = input("\nHvor mange poeng skal man ha for aa vinne? (tast inn et tall)\n > ")
            break
        except:
            print "Du maa skrive inn et tall er du grei..."
    poengspiller = 0
    poengstyggen = 0
    valg = ["Stein","Saks","Papir"]
    while poengspiller < maxpoeng and poengstyggen < maxpoeng:
        forsok = raw_input("Hva velger du? (stein, saks, eller papir)\n> ").lower()
        if forsok == "quit":
            quit()
        comp = random.choice(valg)
        if forsok == "stein":
            if comp == "Stein":
                pass
            elif comp == "Saks":
                poengspiller += 1
            elif comp == "Papir":
                poengstyggen += 1
        elif forsok == "saks":
            if comp == "Stein":
                poengstyggen += 1
            elif comp == "Saks":
                pass
            elif comp == "Papir":
                poengspiller += 1
        elif forsok == "papir":
            if comp == "Saks":
                poengstyggen += 1
            elif comp == "Stein":
                poengspiller += 1
            elif comp == "Papir":
                pass
        else:
            print "Du kan kun velge stein, saks eller papir...\n"
            continue
        print "\n"
        print "Du valgte: %s  -  Styggen valgte: %s" % (forsok.capitalize(),comp)
        print "\n Stilligen er:"
        print "\n   ",poengspiller,"            ",poengstyggen
        print "\n"
 
    if poengspiller < poengstyggen:
        res = "tapte,men du skal faa en troeste"
    else:
        res = "VANT! Gratulerer! Du skal faa en"
    if raw_input("Du "+res+" premie,\n vil du det? ( Skriv ja eller nei)").lower() in ("ja"):
        rom1.rom1()
    else:
        quit()

     