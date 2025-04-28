#   ht# string -->   Hall/123/user123
# integer int -->  123,5
# floats  ->  10.3,  0.0
# Boolean  bool  ->   True/False
#........



def draw_values(values):

    print(values[0],"|",values[1],"|",values[2])
    print("--|---|--")
    print(values[3],"|",values[4],"|",values[5])
    print("--|---|--")
    print(values[6],"|",values[7],"|",values[8])


# draw_values(values)
# current_pos = int(input('HGallo Spieler 1 wo möchtest Du Deine Figur platzieren (0 bis 8) ? '))
# values[current_pos] = 'X'
# draw_values(values)

def check_if_valid(values, current_pos):
    # Verifiziert, ob ein Zug innerhalb vom Spielfeld ist
    if current_pos > 8 or current_pos < 0:
        print("Figur ausserhalb des Spielfelds positioniert !")
        return False
    
    elif values[current_pos] != ' ':
        print("Der Platz ist bereits belegt, probier es bitte nochmal :")
        return False
    
    else:
        return True
    
def check_win_condition(values):
    #Horizontal
    if(values[0] == values[1] == values[2] and values[0] != ' '):
        return True
    elif(values[3] == values[4] == values[5] and values[3] != ' '):
        return True
    elif(values[6] == values[7] == values[9] and values[6] != ' '):
        return True
    
    #Vertikale
    if(values[0] == values[3] == values[6] and values[0] != ' '):
        return True
    elif(values[1] == values[4] == values[7] and values[1] != ' '):
        return True
    elif(values[2] == values[5] == values[8] and values[2] != ' '):
        return True
    
    #Diagonale
    if(values[0] == values[4] == values[8] and values[0] != ' '):
        return True
    elif(values[2] == values[4] == values[6] and values[1] != ' '):
        return True
    
    else:
        return False
    
        


    
def new_game():
   # Listen
    values = [" "]*9
    
    while True:
    
        draw_values(values)
        
        #Spieler 1
        current_pos = int(input("Hallo Spieler 1, wo möchtest Du Deine Figur platzieren [0-8] ?"  ))
        
        while check_if_valid(values, current_pos) == False:
            current_pos = int(input("Hallo Spieler 1, wo möchtest Du Deine Figur platzieren [0-8] ?"  ))
            
        values[current_pos] = 'X'
        draw_values(values)
        
        #Check, ob Spieler 1 gewonnen hat
        if check_win_condition(values) == True:
            print("Spieler 1, Du hast gewonnen !")
            break

                
        
        #Spieler 2
        current_pos = int(input("Hallo Spieler 2, wo möchtest Du Deine Figur platzieren [0-8] ?"  ))
        
        while check_if_valid(values, current_pos) == False:
            current_pos = int(input("Hallo Spieler 2, wo möchtest Du Deine Figur platzieren [0-8] ?"  ))
            
        values[current_pos] = 'O'
        
        if check_win_condition(values) == True:
            print("Spieler 2, Du hast gewonnen !")
            draw_values(values)
            break
    
new_game()
