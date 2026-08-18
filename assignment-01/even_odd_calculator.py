def calculate_number(number):
    if number % 2 == 0:
        return number ** 2
    else:
        return number ** 3


while True:
    user_input = input("Enter a number between 10 and 100 (both included): ")
    if user_input.isdigit():
        user_input = int(user_input)
        if 10 <= user_input <= 100:
            result = calculate_number(user_input)
            print(f"The result is: {result}")
        else:
            print("Invalid input, please enter a number between 10 and 100.")
    else:
        print("Invalid input, please enter a valid integer.")

    another_calculation = input(
        "Do you wish to perform another calculation? (yes/no): "
    )
    if another_calculation.lower() != "yes":
        print("Thank you for using the calculator. Goodbye!")
        break
