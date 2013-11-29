# -*- coding: UTF-8 -*-

# STEIN SAKS OG PAPIR.

 
import random
import rom1
import rom2
def steinsaksogpapir(): #her starter definisjonen på spillet.
    print """\nSTEIN SAKS OG PAPIR!
Klarer du aa vinne over Styggen? Beseir han og du kan vinne fine premier!

Lykke til..."""
    while True:
        try:
            maxpoeng = input("\nHvor mange poeng skal man ha for aa vinne? (tast inn et tall)\n > ") #her velger spilleren hvor mange poeng spillet skal gå til før man er ferdig og vinner/taper.
            break
        except:
            print "Du maa skrive inn et tall er du grei..." #hvis ikke inputten er tall får man opp denne feilmeldingen.
    poengspiller = 0
    poengstyggen = 0
    valg = ["Stein","Saks","Papir"]
    while poengspiller < maxpoeng and poengstyggen < maxpoeng: #spillet kjører helt til maxpoeng er nådd. (maxpoeng=inputten fra spilleren når spillet starter)
        forsok = raw_input("Hva velger du? (stein, saks, eller papir)\n> ").lower() 
        if forsok == "quit": # man kan skrive quit og komme ut av spillet/fila
            quit()
        comp = random.choice(valg) # definerer hva som slår hva og legger til 1poeng/ikke legger til poeng hvis man velger likt.
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
            print "Du kan kun velge stein, saks eller papir...\n" #hvis spillerens input er annet enn stein,saks,papir kjøres print med denne "feilmld".
            continue
        print "\n"
        print "Du valgte: %s  -  Styggen valgte: %s" % (forsok.capitalize(),comp) # printer ut valgene man tok
        print "\n Stilligen er:"
        print "\n   ",poengspiller,"            ",poengstyggen #printer ut stillingen, 
        print "\n"
 
    if poengspiller < poengstyggen:
        res = "tapte,men du skal faa en troeste"
    else:
        res = "VANT! Gratulerer! Du skal faa en" #if løkken: kjører tap hvis styggen vinner, kjører vant hvis spilleren vinner, og hvis inputt fra spilleren er ja, kjøres fila rom1 og funksjonen rom1.
    if raw_input("Du "+res+" premie,\n vil du det? ( Skriv ja eller nei)").lower() in ("ja"): # hvis annet input, kjøres quit og man går ut av spillet/fila.
        rom1.rom1()
    else:
        quit()

     