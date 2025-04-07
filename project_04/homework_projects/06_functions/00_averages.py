# Write a function that takes two numbers and finds the average between the two.


def find_average(num1, num2):
    """Returns the average of two numbers."""
    return (num1 + num2) / 2

avg_1 = find_average(5, 12)
avg_2 = find_average(2, 10)

final_avg = find_average(avg_1, avg_2)

print("avg_1:", avg_1)
print("avg_2:", avg_2)
print("final_avg:", final_avg)
  

