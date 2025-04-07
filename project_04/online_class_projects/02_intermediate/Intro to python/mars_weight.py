MARS_MULTIPLE = 0.378

def calculate_mars_weight(earth_weight):
    mars_weight = earth_weight * MARS_MULTIPLE
    return round(mars_weight, 2)

def main():
 
    earth_weight = float(input("Enter a weight on Earth: "))
    
    
    mars_weight = calculate_mars_weight(earth_weight)
    print(f"The equivalent weight on Mars: {mars_weight}")

main()
