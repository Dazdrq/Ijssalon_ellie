#Opdracht 12
from algemene_functies import mijn_functie_2

#Opdracht 5
def aanbieding_1(smaak, prijs, korting):
    korting=prijs-(prijs*korting)
    aanbieding_tekst= f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak van {smaak}, van {prijs} euro voor {korting} euro."
    print(aanbieding_tekst)

aanbieding_1("aardbei",4, 0.1)

#Opdracht 6 , 7
def inkomsten_totaal(inkomsten,btw):
    totaal= sum(inkomsten)
    bedrag=btw/100
    print(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag*totaal} euro btw betaald dient te worden.")

inkomsten_totaal([200, 430, 125, 160, 205, 90, 345],9)

#Opdracht 8
def laag_en_hoog(mijn_lijst):
    laagste=min(mijn_lijst)
    hoogste=max(mijn_lijst)
    return laagste,hoogste
    

laag_en_hoog([220, 430, 125, 160, 205, 90, 345])

#Opdracht 9, 10
def gemiddelde(mijn_lijst):
    totaal=sum(mijn_lijst)
    gemiddelde=totaal/len(mijn_lijst)
    print(f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro.")

gemiddelde([220, 430, 125, 160, 205, 90, 345])

#Opdracht 11
def meervoudig(invoer_lijst):
    laagste = min(invoer_lijst)
    hoogste = max(invoer_lijst)
    return laagste, hoogste


meervoudig([10, 5, 3, 2, 7, 2, 9])

#Opdracht 12
def combinatie(invoer_lijst_2):
    laagste=min(invoer_lijst_2)
    hoogste=max(invoer_lijst_2)
    korte_lijst = (laagste,hoogste)
    return korte_lijst

mijn_functie_2(combinatie([10, 5, 3, 2, 7, 2, 9]))
