# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
  """Converts temperature from Fahrenheit to Celsius.

  Args:
      fahrenheit: Temperature value in Fahrenheit.

  Returns:
      Temperature value in Celsius.
  """
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
  """Converts temperature from Celsius to Fahrenheit.

  Args:
      celsius: Temperature value in Celsius.

  Returns:
      Temperature value in Fahrenheit.
  """
  return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
  """Prompts user for temperature conversion and displays result."""
  while True:
    try:
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

      if unit == "C":
        converted_temp = convert_to_fahrenheit(temperature)
        unit_out = "F"
      elif unit == "F":
        converted_temp = convert_to_celsius(temperature)
        unit_out = "C"
      else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

      print(f"{temperature:.1f}°{unit} is {converted_temp:.1f}°{unit_out}")
      break

    except ValueError as e:
      print(f"Error: {e}")


if __name__ == "__main__":
  main()
