fruits_colors = {
    "apple": "red",
    "banana": "yellow",
    "orange": "orange",
    "grape": "purple",
    "strawberry": "red",
    "kiwi": "green",
    "blueberry": "blue",
    "watermelon": "green",
    "cherry": "red",
    "pineapple": "yellow"
}

correct_responses = 0
incorrect_responses = 0

for fruit in fruits_colors:
    user_input = input(f"What color is a {fruit}? ").strip().lower()

    if user_input == fruits_colors[fruit]:
        print("Correct!")
        correct_responses += 1
    else:
        print("Incorrect!")
        incorrect_responses += 1

print("\nQuiz Results:")
print(f"Correct Responses: {correct_responses}")
print(f"Incorrect Responses: {incorrect_responses}")
