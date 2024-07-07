# Global conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
   return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main function to handle user interaction
def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")

    except ValueError as e:
        print(f"Error: {e}. Please enter a numeric value for temperature.")

if __name__ == "__main__":
    main()

