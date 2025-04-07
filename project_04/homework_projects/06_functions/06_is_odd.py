# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd



def start():
    for num in range(10):
        if check_odd(num):
            print(f"{num} is odd")
        else:
            print(f"{num} is even")
            
def check_odd(n: int):
    """
    Determines if a number is odd. Returns True if it is.
    """
    return n % 2 != 0

start()
