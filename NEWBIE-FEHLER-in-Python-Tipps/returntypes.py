class NumberTooLargeException(Exception):
    pass 


def larger_than_10(a):
    if a > 10:
        return a
    else:
        raise NumberTooLargeException("Nur Nummern größer als 10 erlaubt.")
    
    
try:
    larger_than_10() 
except:
    print("Error")
    
    
    
print(larger_than_10(11))
print(larger_than_10(5))