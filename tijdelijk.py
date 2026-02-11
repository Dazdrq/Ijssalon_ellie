#Opdracht 2
prijzen={
    "aarbei":3,
    "vanille":4,
    "chocolade":5
}
#Opdracht 3
aanbieding=prijzen["aarbei"]*0.8
#Opdracht 4
reclame_tekst= f"vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"
#Opdracht 5
reclame_tekst2=reclame_tekst[:62]
#Opdracht 6
reclame_tekst3=reclame_tekst2.upper()
#Opdracht 7
reclame_tekst4=reclame_tekst3.split(" ")
#Opdracht 8,9,10
for el in reclame_tekst4:
    if len(el)>4:
        print(el.upper())
    else: 
        print(el.lower())