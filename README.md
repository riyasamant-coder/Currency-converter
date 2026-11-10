
# Currency Converter

A Python 3 console-based currency converter that converts amounts between four supported currencies using fixed exchange rates stored in a dictionary.

## Project Details

- **Project Title:** Currency Converter
- **Problem Statement Number:** 25
- **Programming Language:** Python 3
- **Concepts Used:** Functions, Conditional Statements, Operators, Dictionaries and Exception Handling.

## Features

- Converts between INR, USD, EUR and GBP.
- Uses INR as the base currency for every conversion.
- Stores exchange rates in a Python dictionary.
- Accepts decimal and whole-number amounts.
- Validates currency codes and user input.
- Handles invalid and negative amounts.
- Displays converted results rounded to two decimal places.

## Supported Currencies and Exchange Rates

The following fixed exchange rates are used:

| Currency | Value in INR |
|---|---:|
| INR | 1 |
| USD | 83 |
| EUR | 90 |
| GBP | 105 |

**Note:** These are fixed rates provided in the project statement, not live exchange rates.

## How It Works

Every conversion takes place through INR.

1. The entered amount is converted into INR.
2. The INR amount is converted into the target currency.
3. The final result is rounded to two decimal places.

## Python Concepts Used

- **Dictionaries:** To store currency exchange rates.
- **Functions:** To organise the conversion operations.
- **Conditional Statements:** To validate currencies and amounts.
- **Operators:** To perform currency calculations.
- **Exception Handling:** To handle invalid numerical input.

## How to Run the Program

1. Make sure Python 3 is installed on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code or a terminal.
4. Run the following command:

```bash
python Currency_Converter.py
```

## Test Cases

The program was tested using the following cases:

| Test Case | Input | Expected Result |
|---|---|---|
| 1 | 166 INR to USD | 2.00 USD |
| 2 | 0 USD to INR | 0.00 INR |
| 3(a) | Unsupported currency JPY | Error message |
| 3(b) | Invalid amount `abc` | Invalid amount message |
| 3(c) | Negative amount -50 | Negative amount message |
| 4(a) | 100 USD to EUR | 92.22 EUR |
| 4(b) | 2 GBP to INR | 210.00 INR |
| 4(c) | 45 EUR to USD | 48.80 USD |

## Project Structure

```text
Currency-converter/
│
├── Currency_Converter.py
├── README.md
└── screenshots/
    ├── TC1_INR_to_USD.png
    ├── TC2_Zero_Amount.png
    ├── TC3a_Invalid_Currency.png
    ├── TC3b_Invalid_Amount.png
    ├── TC3c_Negative_Amount.png
    ├── TC4a_USD_to_EUR.png
    ├── TC4b_GBP_to_INR.png
    └── TC4c_EUR_to_USD.png
```

## Conclusion

This project demonstrates the use of fundamental Python programming concepts to develop a functional currency converter. It helped in understanding dictionaries, functions, conditional statements, operators, input validation and exception handling.

The program successfully performs conversions between the supported currencies and handles common invalid inputs.

