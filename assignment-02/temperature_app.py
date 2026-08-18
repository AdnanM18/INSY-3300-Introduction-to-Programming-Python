from TemperatureConverter import celsius_to_fahrenheit, fahrenheit_to_celsius


def main():
    try:
        temperature = float(input("Enter the temperature: "))
        unit = input(
            "Enter the unit of measurement (Celsius or Fahrenheit): "
        ).strip().lower()

        if unit == "celsius":
            converted_temp = celsius_to_fahrenheit(temperature)
            print(f"The temperature in Fahrenheit is: {converted_temp:.2f}°F")
        elif unit == "fahrenheit":
            converted_temp = fahrenheit_to_celsius(temperature)
            print(f"The temperature in Celsius is: {converted_temp:.2f}°C")
        else:
            print("Invalid unit entered. Please enter Celsius or Fahrenheit.")
    except ValueError:
        print("Invalid input. Please enter a valid temperature.")


if __name__ == "__main__":
    main()
