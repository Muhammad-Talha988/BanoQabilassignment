# Temperature Converter
# Converts Celsius to Fahrenheit and Fahrenheit to Celsius

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

# Ask the user to choose a conversion type
choice = input("Enter your choice (1 or 2): ")

# Ask the user for the temperature
temperature = float(input("Enter the temperature: "))

# Perform the selected conversion
if choice == "1":
    # Celsius to Fahrenheit formula
    fahrenheit = (temperature * 9 / 5) + 32
    print(f"{temperature}°C = {fahrenheit:.2f}°F")

elif choice == "2":
    # Fahrenheit to Celsius formula
    celsius = (temperature - 32) * 5 / 9
    print(f"{temperature}°F = {celsius:.2f}°C")

else:
    # Handle an invalid choice
    print("Invalid choice. Please enter 1 or 2.")