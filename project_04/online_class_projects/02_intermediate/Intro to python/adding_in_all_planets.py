# MERCURY_GRAVITY = 0.376
# VENUS_GRAVITY = 0.889
# MARS_GRAVITY = 0.378
# JUPITER_GRAVITY = 2.36
# SATURN_GRAVITY = 1.081
# URANUS_GRAVITY = 0.815
# NEPTUNE_GRAVITY = 1.14
# EARTH_GRAVITY = 1.0


# def calculate_planetary_weight(earth_weight, planet):
 
#     if planet == "Mercury":
#         gravity_constant = MERCURY_GRAVITY
#     elif planet == "Venus":
#         gravity_constant = VENUS_GRAVITY
#     elif planet == "Mars":
#         gravity_constant = MARS_GRAVITY
#     elif planet == "Jupiter":
#         gravity_constant = JUPITER_GRAVITY
#     elif planet == "Saturn":
#         gravity_constant = SATURN_GRAVITY
#     elif planet == "Uranus":
#         gravity_constant = URANUS_GRAVITY
#     elif planet == "Neptune":
#         gravity_constant = NEPTUNE_GRAVITY
#     else:
#         gravity_constant = EARTH_GRAVITY  


#     planetary_weight = earth_weight * gravity_constant
#     return round(planetary_weight, 2)

# def main():
  
#     earth_weight = float(input("Enter a weight on Earth: "))
    
   
#     planet = input("Enter a planet (e.g., Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune): ")

  
#     planetary_weight = calculate_planetary_weight(earth_weight, planet)
    
  
#     print(f"The equivalent weight on {planet}: {planetary_weight}")

# main()


# my_set = {1, 2, 3}
# print(hash(my_set))

# my_list = [1, 2, 3]
# print(hash(my_list))

my_set2 = {1, 2, "hi"}
# print(my_set2[0])
for i in my_set2:
    print(i)

my_list2 = [1, 2, "hi"]
for i in my_list2:
    print(hash(i))


# try:
#     print(hash(my_list))  # This will raise an error
# except TypeError as e:
#     print(e) 