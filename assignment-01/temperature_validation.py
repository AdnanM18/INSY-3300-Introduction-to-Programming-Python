while True:
    celsius_input = input("Enter a temperature in Celsius: ")
    if celsius_input.replace(".", "", 1).lstrip("-").isdigit():
        celsius = float(celsius_input)
        if -273.15 <= celsius <= 100:
            fahrenheit = round(celsius * 1.8 + 32, 1)
            print(f"The converted temperature in Fahrenheit is {fahrenheit}")
            break
        else:
            print("Error! The temperature is not in the valid range. Please try again.")
    else:
        print("Invalid input. Please enter a valid temperature.")
