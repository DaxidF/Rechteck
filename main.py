#Imports
from colorama import Fore

#Color output
print(Fore.MAGENTA)

#Get length and width
Laenge = float(input('Bitte gib die Laenge in m an: '))
Breite = float(input('Bitte gib die Breite in m an: '))

#Calc.
Rechteck_Flaeche = Laenge * Breite
Rechteck_Umfang = (Breite * 2) + (Laenge * 2)

#Print
print('Flaecheninhalt: ', Rechteck_Flaeche, 'm²')
print('Umfang: ', Rechteck_Umfang, 'm\n')

#Wait befor closeing
input('\nDrücke Enter zum Schließen.')