#Smart Temperature Converter
temp_celsius = float(input("Enter temperature in Celsius: "))
temp_fahrenheit = (temp_celsius * 9/5) + 32
print(f"{temp_celsius} degrees Celsius is equal to {temp_fahrenheit} degrees Fahrenheit.")  
temp_kelvin = temp_celsius + 273.15
print(f"{temp_celsius} degrees Celsius is equal to {temp_kelvin} Kelvin.")
