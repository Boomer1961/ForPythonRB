if 5 > 2:
    print("5 größer 2")
    # Kommentare
    #.....
    #....
    
my_var = 10
my_var = "zehn"

# Eine Liste in Python ist eine geordnete, veränderbare Sammlung von Elementen, die unterschiedliche Datentypen enthalten kann. 
# Sie wird durch eckige Klammern [] dargestellt und ermöglicht den Zugriff auf Elemente über ihren Index. Listen unterstützen 
# verschiedene Operationen wie Hinzufügen, Entfernen und Sortieren von Elementen.
my_list = [1,2,3]

# Ein Tuple in Python ist eine geordnete, unveränderbare Sammlung von Elementen, die unterschiedliche Datentypen enthalten kann. 
# Es wird durch runde Klammern () dargestellt und ermöglicht den Zugriff auf Elemente über ihren Index. Aufgrund ihrer 
# Unveränderlichkeit sind Tuples oft schneller und können als Schlüssel in Dictionaries verwendet werden.
my_tuple = (1,2,3)

# Ein Set in Python ist eine ungeordnete Sammlung von einzigartigen Elementen, die keine Duplikate zulässt. Es wird durch geschweifte 
# Klammern {} oder die Funktion set() dargestellt und unterstützt verschiedene mathematische Operationen wie Vereinigung, Schnittmenge 
# und Differenz. Sets sind veränderbar, was bedeutet, dass Elemente hinzugefügt oder entfernt werden können, jedoch ist der Zugriff auf 
# Elemente nicht über einen Index möglich.
my_set = {1,2,3}

# Ein Dictionary in Python ist eine ungeordnete Sammlung von Schlüssel-Wert-Paaren, die es ermöglicht, Werte über eindeutige Schlüssel 
# zu speichern und abzurufen. Es wird durch geschweifte Klammern {} dargestellt, wobei jeder Schlüssel mit einem Doppelpunkt : vom 
# entsprechenden Wert getrennt ist. Dictionaries sind veränderbar, was bedeutet, dass neue Paare hinzugefügt, bestehende Paare geändert 
# oder entfernt werden können.
my_dictionary = {'eins':1,'zwei':2,'drei':'3'}  

# ABOUT print
print("Hallösche",100)
name = "Anna"
alter = 25
print(f"{name} ist {alter} alt")
print("{name} ist {alter} alt")

print("Inhalt der Liste ", my_list)

#About scopes
x = 5
name = "Max"

a,b,c = 5,4,"Tim"

alter = 30      # integer
gewicht = 14.5  # Float
name = "Alex"   # String
gewicht = 15

def my_funkt():
    lokal = "I'm local"
    print(lokal)

def set_global_var():
    global set_global_var
    global_var = "Global"
    print(global_var)

set_global_var()
# print(global_var) scope ier nicht definiert

# Anzahl Datentypen
anzahl = 5 # Integer Int
print("Anzahl:", anzahl)

preis = 19.99 # Float
print("Preis:", preis)

# String
gruss = "Hallo Welt"
print(gruss)

gruss2 = 'Hallo Welt 2'
print(gruss2)

#Booleans
ist_volljährig = True
print("volljährig:", ist_volljährig)

#Aritmetik

summe = 10+5 # Addition
print("Summe: ",summe)
differenz = 10-5 # Subtraktion
print("Differenz: ",differenz)
produkt = 10*5 # Multiplikation
print("Produkt: ",produkt)
quotient = 10/5 # Division
print("Quotient: ",quotient)
rest = 10%3 # Modulo
print("Rest: ",rest)
kombination = (10+5)*(4-2) # Kombination von Operatoren
print("Kombination ",kombination)

# String-Manipultaion

vorname = "Anna"
nachname = "Müller"
vollständiger_name = vorname + " " + nachname
print("Vollständiger Name: ", vollständiger_name)
# Slicing
text = "Python-Programmierung"
teil = text[7:15]
print("Slice Text", teil)
# Format
name = "Lara"
alter = 28
text = "Mein Name ist {} und ich bin {} Jahre alt.".format(name,alter)
text2 = f"Mein Name ist {name} und ich bin {alter} Jahre alt."
print(text)
print(text2)
#Bedingte Anweisungen
alter = 12
if alter < 13:
    print("Du bist ein Kind.")
elif alter < 18:
    print("Du bist ein Jugendlicher")
else:
    print("Du bist volljährig.")

alter = 19
hat_führerschein = False
if alter >= 19:
    if hat_führerschein:
        print("Du darfst Auto fahren!")
    else:
        print("Du darfst nicht Auto fahren,aber Du bist volljährig")
else:
    print("Du bist nicht volljährig")
    
# Logische Operatoren

alter = 20
Student = True
if alter >= 18 and Student:
    print("Du bist ein volljähriger Student.")
if alter >= 12 or Student:
    print("Du bist ein volljähriger Student.")
Student = False
if not Student:
    print("YOU NOT")
if (alter>18 and Student) or (alter<13):
   print("It works the or")  
#Vergleichsoperatoren
a = 5
b = 10
c = 9
print(a==b) # Gleichheitsoperator
print(a!=b)
print(a>b)
print(a<b)
if(a<b) and (b>c):
    print("(a<b) and (b>c)")

# Schleifenstrukturen
zahlen = [1,2,3,4,5]
for zahl in zahlen:
    print(zahl)
     
i = 1
while i <= 5:
    print(i)
    i += i
    
for zahl in zahlen:
    if zahl ==3:
        continue
    print(zahl)
    if zahl == 4:
        break
    
for i in range(1,3):
    for j in range(1,4):
        print(f"i={i}  j={j}",i,j)
for i in range(5):
    if i%2==0:
        for j in range(i):
            print(f"i={i} und j = {j}")  
# Funktionsdeklaration
def grüße(name):
    print(f"Hallo {name} !")
    
grüße("Max")

def addiere(a,b):
    return a+b

def drucke_list(meine_liste):
    for element in meine_liste:
        print(element)
        
def verabschiedung(name="Sehr geehrte Dame und Herren"):
    print(f"Auf Wiedersehen {name} !")
    
verabschiedung("Anna")
print(addiere(a=4,b=6))

# Lambda-Funktionen
quadrat = lambda x: x*x
minus = lambda y: 10-y
print(quadrat(5))
print(minus(4))

zahlen= [1,2,3,4,5]
quadrate = list(map(lambda x: x*x, zahlen))
print(quadrate)

ungerade_zahlen = list(filter(lambda x: x%2 != 0, zahlen))
print(ungerade_zahlen)

fruechte = ['Ananas','Banane','Apfel','Kirsche']
sortiert = sorted(fruechte,key= lambda x:len(x))
print(sortiert)

# Parameter, Rückgabeanweisungen und Funktionsdokumentation

def multipliziere(a,b):
    return a*b

def finde_maximum(x,y):
    if x>y:
        return x
    else:
        return y
    
maximum = finde_maximum(2,3)
print(maximum)

def addiere(a,b):
    """_summary_

    Parameter:
        a (int,float): _description_
        b (int,float): _description_
        
    Rückgabe:
    int, float: Die Summe von a und b
    """
    return a+b
    
# Funktionsargumente

def subtrahiere(a,b):
    return a-b

print(subtrahiere(5,3))
        
def gruesse(name,nachricht):
    print(f"Hallo {name}, {nachricht} !")
    
gruesse(nachricht="Schönen Tach",name="Anne")

def persona(name, alter,wohnort="unbekannt", beruf="unbekannt"):
    print(f"Name: {name}, Alter: {alter}, Wohnort: {wohnort}, Beruf: {beruf}")
    
persona("Laura",30,beruf="Variable",wohnort="Stuttgart")

# Rückgabe mehrer Werte

def berechne(a,b):
    summe = a+b
    differenz = a-b
    neu = 18
    return summe, differenz, neu

ergebnis = berechne(10,5)
print(ergebnis)
res1, res2, neu= berechne(10,5)
print(f"Res1: {res1}, Res2: {res2} Neu: {neu}") 

def finde_extreme(zahlen):
    return [min(zahlen),max(zahlen)]

extreme = finde_extreme([1,2,3,4,5])
print(extreme)

def analysiere(zahlen):
    return {
            'minimum':min(zahlen),
            'maximum':max(zahlen),
            'durchschnitt':sum(zahlen)/len(zahlen)
            }
    
ergebnis = analysiere([1,2,3,4,5])
print(ergebnis)

# Integrierte Module

import math
import datetime

print(math.sqrt(15))
print(math.pi)
print(datetime.datetime.now())

import os 
print(os.getcwd())

import random
print(random.randint(1,100))

# Benutzerdefinierte Module

import benutzerdefinierte_module as bn
# oder um eigenen Namespace zu bilden:
from benutzerdefinierte_module import grüße as hiesige_grüße

result1 = bn.addiere(4,8)
result2 = bn.grüße("Hermine")

print(f"Hallo {result2},addiere für {result1} ")
print(bn.grüße("Anna"))
print(hiesige_grüße("Hier"))

# Integrierte Funktionen

liste = [1,2,3,4,5]
print(len(liste))
print(type(liste))

liste = 1
print(type(liste))

name = input("Enter your name: ")
print(f"You are {name} !")

zahl = str(18)
print(type(zahl))

# Standardbibliotheken

import sys
print(sys.version_info)

import os
print(os.getcwd())

import json
json_string = json.dumps([1,2,3,"a","b","c"])
print(json_string)

from datetime import datetime
jetzt = datetime.now()
print(jetzt)

from collections import Counter
zähler = Counter(['a','b','c','d','a','b'])
print(zähler)

# Listen und Tuples

meine_liste = [1,2,3]
mein_tuple = (1,2,3)

print(meine_liste[0])
print(mein_tuple[0])

print(meine_liste[1:3])
print(mein_tuple[0:2])

meine_liste[0] = 100
print(meine_liste[0])

meine_liste.append(4)
print(meine_liste)

#mein_tuple[0] = 100
#print(mein_tuple[0])

#mein_tuple.append(4)
#print(mein_tuple)

# Manipulation von Listen

meine_liste = ['a','b','c','d','e',[1,2,3]]
print(meine_liste[0])
print(meine_liste[3])
print(meine_liste[5])
print(meine_liste[-1])

teil_liste = meine_liste[1:4:1]
print(teil_liste)

meine_liste.append('f')
print(meine_liste)

meine_liste.insert(1,'x')
print(meine_liste)

meine_liste.remove('c')
print(meine_liste)

entferntes_element = meine_liste.pop(2)
print(entferntes_element)

meine_liste.pop(2)
print(meine_liste)

del meine_liste[1:3:2]
print(meine_liste)

meine_liste[0] = 'Z'
print(meine_liste)

zweite_liste = ['g','h']
meine_liste.extend(zweite_liste)
print(meine_liste)

meine_liste.reverse()
print(meine_liste)

#meine_liste.sort()
#print(meine_liste)

# Listenabkürzungen

quadrate = [x**2 for x in range(5)]
print(quadrate)

gerade_zahlen = [x for x in range(10) if x%2 == 0]
print(gerade_zahlen)

kombination = [(a,b) for a in [1,2,3] for b in [4,5,6]]
print(kombination)

# Unveränderlichkeit von Tuples

mein_tuple = (1,2,3)
mein_tuple_ohne_klappern = 1,2,3
mein_tuple_ein_element = 1,
print(mein_tuple_ohne_klappern)
print(mein_tuple_ein_element)

#mein_neues_tuple = mein_tuple.append(4)
#print(mein_neues_tuple)

# Anwendungsfälle für Tuples

konfuguration = (1920,1080,60)

def berechne_statistiken(zahlen):
    mittelwert = sum(zahlen)/len(zahlen)
    varianz = sum((x - mittelwert)**2 for x in zahlen)/len(zahlen)
    standardabweichung = varianz**0.5
    return mittelwert, standardabweichung

statistiken = berechne_statistiken([1,2,3,4,5])
print(statistiken)


for x,y in [(1,2),(3,4),(5,6)]:
    print(x+y)

farben = {(255,0,0):"Rot",(0,255,0):"Grün",(0,0,255):"Blau"}
print(farben[(255,0,0)])

def position_berechnen(x,y,z):
    return(x**2+y**2+z**2)**0.5

position = (100,200,300)
entfernung = position_berechnen(*position)

print("Die Entfernung vom Mittelpunkt ist:",entfernung, "km")
 