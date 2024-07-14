
---

# Python OOP and Unit Testing Projects

This repository contains three Python projects designed to reinforce basic Object-Oriented Programming (OOP) concepts and unit testing skills.

## Project 1: Simple Bank Account Class

### Overview

This project demonstrates basic OOP principles by implementing a `BankAccount` class that encapsulates banking operations. The class interacts with users through command line arguments.

### Files

- **bank_account.py**: Defines the `BankAccount` class with methods to deposit, withdraw, and display the balance.
- **main-0.py**: Interfaces with the `BankAccount` class through command line arguments.

### Usage

1. **Deposit**:
   ```sh
   python main-0.py deposit:50
   ```

2. **Withdraw with Sufficient Funds**:
   ```sh
   python main-0.py withdraw:20
   ```

3. **Withdraw with Insufficient Funds**:
   ```sh
   python main-0.py withdraw:150
   ```

4. **Display Balance**:
   ```sh
   python main-0.py display
   ```

---

## Project 2: Robust Division Calculator

### Overview

This project implements a division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.

### Files

- **robust_division_calculator.py**: Contains the `safe_divide` function to perform division with error handling.
- **main.py**: Interfaces with the `safe_divide` function through command line arguments.

### Usage

1. **Normal Division**:
   ```sh
   python main.py 10 5
   ```

2. **Division by Zero**:
   ```sh
   python main.py 10 0
   ```

3. **Invalid Input (Non-numeric)**:
   ```sh
   python main.py ten 5
   ```

---

## Project 3: Writing Unit Tests for a Simple Calculator Class

### Overview

This project focuses on writing unit tests for a provided `SimpleCalculator` class that supports basic arithmetic operations.

### Files

- **simple_calculator.py**: Defines the `SimpleCalculator` class.
- **test_simple_calculator.py**: Contains unit tests for the `SimpleCalculator` class.

### Running Tests

To run the unit tests, use the following command:
```sh
python -m unittest test_simple_calculator.py
```

---

## Project 4: Library Management System

### Overview

This project implements a basic library management system with a `Book` class and a `Library` class. It demonstrates the use of classes, object instantiation, and method invocation.

### Files

- **library_management.py**: Defines the `Book` and `Library` classes.
- **main.py**: Demonstrates how to interact with the `Book` and `Library` classes.

### Usage

1. **Initial Setup**:
   ```sh
   python main.py
   ```

2. **Check Out a Book**:
   Modify `main.py` to include `library.check_out_book("1984")` and run:
   ```sh
   python main.py
   ```

3. **Return a Book**:
   Modify `main.py` to include `library.return_book("1984")` and run:
   ```sh
   python main.py
   ```

---

## Notes

- Ensure Python is installed on your system.
- Clone the repository and navigate to the appropriate project directory to run the scripts.
- Each project includes detailed comments and error handling to ensure smooth operation and provide learning insights.

---



