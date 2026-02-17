#Opdracht 10.11 11
import csv
#Opdracht 10.11 4
from helper import *
#Opdracht 10.11 9
from presentatie import presenteer

#Opdracht 10.11 2
inkomsten = {
    "Aarbeien-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750
}
#Opdracht 10.11 5
totaal_inkomsten= som(inkomsten)

#Opdracht 10.11 10
presenteer(inkomsten,totaal_inkomsten)

#Opdracht 10.11 12
with open('boekhouding.csv', 'w',newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    for key, value in inkomsten.items():
        writer.writerow([key,value])
 
       