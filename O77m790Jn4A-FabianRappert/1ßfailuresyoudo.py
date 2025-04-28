
# Failure 1
# NAMING COMNVENTION

class HelloWorldClass():
    
    MEINE_KONSTANTE = 'Hello world'
    
    def __init__(self, variable):
        
        self.meine_lange_variable = variable
        
    def hello_world_funktion():
        return "Hello world"
    
    
# Failure 2
# NNO CONSTANT STYLE

def funktionA():
    first_name = "Fabian"
    last_name = "Rappert"
    a1 = 142
    place = 'Berlin'

# Failure 3
# print instead return


# Failure 4
# List iterations

avengers = ['Hulk','Spiderman','Ironman']

for index in range(len(avengers)):
    print(avengers[index])
    
for avenger in avengers:
    print(avenger) 
    
    
# Failure 5
# Manuelle Verkettung von Strings

vorname = 'Mike'
alter = '25'

# Mit dem + muß man viel manuell arbeiten z.B. casten von alter, gewünscht, f-string
print(f"Hallo {vorname}, ist Dein Alter mit {alter} korrekt ?")

#Fehler 6 - if Bedingungen kürzen

if len (avengers) != 0:
    print("Die Liste ist nicht leer.")
    
if avengers:
    print("Die Liste ist nicht leer.")
    
end = True

if end == True or bool(end):  # Nicht gut end ist sowieso true
    print("ciao")
    
if end:                            # Nicht gut end ist sowieso true
    print("ciao")
    
#Fehler7 pep8.org   Codierrichtlinie 
#Fehler8 Nicht zu viele Tutorials 
#Fehler9 Python 2 verwenden
#Fehler10 Fehlermeldungen nicht beachten
