import random


def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    question = f"What is {num1} times {num2}?"
    answer = num1 * num2
    return question, answer


def ask_user_to_continue():
    user_input = input("Do you want to continue playing? (yes/no): ").strip().lower()
    return user_input == "yes"


def check_answer(user_answer, correct_answer):
    try:
        user_answer = int(user_answer)
        return user_answer == correct_answer
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return False


def main():
    try:
        while True:
            question, correct_answer = generate_question()
            print(question)
            user_answer = input("Your answer: ")

            if check_answer(user_answer, correct_answer):
                print("Correct!")
            else:
                print("Incorrect!")

            if not ask_user_to_continue():
                print("Thanks for playing!")
                break
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
