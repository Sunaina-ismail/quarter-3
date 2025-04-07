# Write a program that doubles each element in a list of numbers. For example, if you start with this list:
# numbers = [1, 2, 3, 4]
# You should end with this list:
# numbers = [2, 4, 6, 8]


def double_list_elements():
    values = [1, 2, 3, 4,5,6] 

    for index in range(len(values)):  
        values[index] *= 2  

    print(values)  


double_list_elements()
