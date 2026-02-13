#Opdracht 2
def mijn_functie_1(a, b, c, d ):
    getallen =[a**2, b**2, c**2, d**2]
    for g in getallen:
        print(g)

mijn_functie_1(2, 4, 10, 12)

#Opdracht 3
def mijn_functie_2(invoergetallen):
    a,b = invoergetallen
    resultaten = [a+b, a-b, a*b, int(a/b)]
    print(resultaten)
    return resultaten
 
mijn_functie_2([12,3])


