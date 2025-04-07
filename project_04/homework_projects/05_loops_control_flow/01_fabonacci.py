MAX_VALUE = 10000  

def fibonacci_sequence():
    a, b = 0, 1  
    while a < MAX_VALUE:
        print(a, end=" ")
        a, b = b, a + b 


fibonacci_sequence()
