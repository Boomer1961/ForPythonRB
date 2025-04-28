# https://www.youtube.com/watch?v=i1uQgU7NOCw
# Objektorientierte Programmierung mit Python - Klassen & Instanzen
# Coding Crashkurse
#

from datetime import date


class Kunde:
    def __init__(self, vorname="No prename entered", 
                 nachname="No surname entered", 
                 guthaben=0):

        self.vorname = vorname
        self.nachname = nachname
        self.guthaben = guthaben
        self.reg_time = date.today() # soll automatisiert und nicht manuell 
        #vom Kunden engetragen werden, daher nicht in init 
    
    def einzahlen(self,amount):
        self.guthaben = self.guthaben+amount
        
    def abheben(self,amount):
        if amount > self.guthaben:
            raise ValueError("Nicht genug Geld auf dem Konto")
        self.guthaben = self.guthaben-amount
        
    

kunde1 = Kunde("Max","Küller",2000)
kunde2 = Kunde("Martin","Müller",5000)


kunde1.abheben(1400)
kunde1.abheben(1400)


print(kunde1.__dict__)





