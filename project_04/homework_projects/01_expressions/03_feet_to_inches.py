# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

INCHES_PER_FOOT = 12  

def convert_feet_to_inches():
    feet= float(input("Enter length in feet: "))  
    inches: float = feet * INCHES_PER_FOOT  
    print(f"{feet} feet is equal to {inches} inches.")  

convert_feet_to_inches()
