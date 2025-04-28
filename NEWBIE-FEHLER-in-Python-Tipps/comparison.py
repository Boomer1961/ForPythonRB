# Vergleich mit x == None oder x ==True/False

x = None
y = True

# if x == None: Schelchter Python STIL
# == prüft ob zwei Variable den selben Wert haben.
# is prüft, ob 2 Objekte gleich sind

if x is None:
    print("Ist None")
else:
    print("Ist nicht None")

# if if y == True: Schelchter Python STIL

if y is True:
    print("Ist TRUE")
else:
    print("Ist nicht TRUE")
     