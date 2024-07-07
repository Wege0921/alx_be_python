

```markdown
# Python Tasks

This repository contains various Python tasks designed to practice and improve your programming skills. Each task is in its own script file within the `fns_and_dsa` directory.

## Tasks

### 0. Arithmetic Operations Function
Create `arithmetic_operations.py` with a function `perform_operation` to handle basic arithmetic operations: `add`, `subtract`, `multiply`, `divide`. Handle division by zero by returning a specific message.

**Example Usage in `main.py`:**
```python
from arithmetic_operations import perform_operation

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation: ").strip().lower()
    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
```
**Repo:**
- **Directory:** fns_and_dsa
- **File:** `arithmetic_operations.py`

### 1. Shopping List Manager
Create `shopping_list_manager.py` to manage a shopping list with add, remove, and view functionalities using Python lists.

**Skeleton Code:**
```python
def display_menu():
    print("1. Add Item\n2. Remove Item\n3. View List\n4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        # Implement functionality here

if __name__ == "__main__":
    main()
```
**Repo:**
- **Directory:** fns_and_dsa
- **File:** `shopping_list_manager.py`

### 2. Explore `datetime` Module
Create `explore_datetime.py` to use the `datetime` module for displaying the current date and time and calculating a future date based on user input.

**Example Functions:**
```python
from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date}")

def calculate_future_date(days):
    future_date = datetime.now() + timedelta(days=days)
    print(f"Future date: {future_date}")
```
**Repo:**
- **Directory:** fns_and_dsa
- **File:** `explore_datetime.py`

### 3. Temperature Conversion Tool
Create `temp_conversion_tool.py` to convert temperatures between Celsius and Fahrenheit using global variables for conversion factors.

**Example Functions:**
```python
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
```
**Repo:**
- **Directory:** fns_and_dsa
- **File:** `temp_conversion_tool.py`
```


