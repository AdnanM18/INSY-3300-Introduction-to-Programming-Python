# INSY 3300 – Introduction to Programming (Python)

Coursework portfolio from **INSY 3300 – Introduction to Programming**.

The recovered assignments in this repository were written in **Python**, not Java.  
The original Jupyter notebooks identify the language as Python 3.

This repository organizes the recovered code into clean `.py` files so each program
can be opened and run directly.

## Repository Structure

```text
INSY-3300-Introduction-to-Programming-Python/
├── README.md
├── SOURCE_NOTES.md
├── .gitignore
├── assignment-01/
│   ├── subject_popularity.py
│   ├── temperature_validation.py
│   ├── beverage_recommender.py
│   └── even_odd_calculator.py
├── assignment-02/
│   ├── multiplication_quiz.py
│   ├── TemperatureConverter.py
│   ├── temperature_app.py
│   ├── list_processing.py
│   ├── file_statistics.py
│   └── calculations.txt
└── assignment-03/
    ├── fruit_color_quiz.py
    ├── library_set_analysis.py
    └── dice_roll_simulator.py
```

## Assignment 1

### Subject Popularity
Calculates the percentage of science and arts students and reports which subject is
more popular.

### Temperature Validation
Validates a Celsius temperature, converts it to Fahrenheit, and handles invalid input.

### Beverage Recommender
Uses functions and conditional logic to recommend beverages based on meal type.

### Even/Odd Calculator
Squares even numbers and cubes odd numbers within a specified range.

## Assignment 2

### Multiplication Quiz
Generates random multiplication questions, checks answers, and uses exception handling.

### Temperature Converter Module
Demonstrates modular programming by storing conversion functions in
`TemperatureConverter.py` and importing them into `temperature_app.py`.

### List Processing
Uses lists, slicing, insertion, list comprehensions, a prime-number helper function,
and nested data structures.

### File Statistics
Writes numeric data to a text file, reads it back, calculates summary statistics,
and appends the results.

## Assignment 3

### Fruit Color Quiz
Uses a dictionary to quiz the user on fruit colors and tracks correct/incorrect answers.

### Library Set Analysis
Uses Python set operations including intersection, difference, union, subset checks,
symmetric difference, and sorting.

### Dice Roll Simulator
Simulates 500 die rolls, stores frequencies in a dictionary, calculates totals, and
allows the user to query a die face.

## Skills Demonstrated

- Python 3
- Functions
- Conditional logic
- `for` and `while` loops
- Input validation
- Exception handling
- Modules and imports
- File input/output
- Lists and list comprehensions
- Dictionaries
- Sets and set operations
- Random-number generation
- Basic statistics and calculations
- String handling

## Running the Programs

Python 3 is required. No third-party packages are needed.

Example:

```bash
python assignment-02/multiplication_quiz.py
```

For the temperature module example, run:

```bash
cd assignment-02
python temperature_app.py
```

## Portfolio Note

These files are organized from recovered university coursework. The goal is to
preserve the submitted programming logic while presenting it in a clean GitHub layout.
Only minor portability/formatting changes were made, such as replacing a personal
Windows file path with a relative file path.
