
def upper(text):  
    return text.upper()  
    
def lower(text):  
    return text.lower()  
    
def greet(mess, process):
    print( process(mess) )
  
greet('hElLo', upper)  
greet('hElLo', lower) 