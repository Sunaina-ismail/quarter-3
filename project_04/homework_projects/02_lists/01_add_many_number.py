# Write a function that takes a list of numbers and returns the sum of those numbers.



def calculate_sum(numbers_list):  
    total_sum = 0  
    for number in numbers_list:
        total_sum += number  
    return total_sum  

numbers = [1, 2, 3, 4, 5, 6, 7, 8]  
result = calculate_sum(numbers)  

print(result)  






    

