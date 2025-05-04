# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.


class TemperatureConverter:
    
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
c_temp = 30
f_temp = TemperatureConverter.celsius_to_fahrenheit(c_temp)
print(f"{c_temp}C is {f_temp}F")
        