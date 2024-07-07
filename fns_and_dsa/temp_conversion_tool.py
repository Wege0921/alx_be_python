# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
def convert_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius."""
    celsius = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit."""
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
    return fahrenheit
try:
    # Prompting the user for input
    temperature_input = float(input("Enter the temperature to convert: "))
    unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

    if unit_input == "F":
        result = convert_to_celsius(temperature_input)
        print(f"{temperature_input}°F is {result:.2f}°C")
    elif unit_input == "C":
        result = convert_to_fahrenheit(temperature_input)
        print(f"{temperature_input}°C is {result:.2f}°F")
    else:
        raise ValueError("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
except ValueError as e:
    print("Invalid temperature. Please enter a numeric value.", str(e))

