import random

rolls = [random.randint(1, 6) for _ in range(500)]

frequency = {i: rolls.count(i) for i in range(1, 7)}

total_sum = sum(rolls)

most_common_face = max(frequency, key=frequency.get)

print("Total sum of 500 die faces:", total_sum)

print("The most common die face:", most_common_face)

user_input = int(input("Enter a die face (1-6): "))
if user_input in frequency:
    print(f"Frequency of face {user_input}: {frequency[user_input]}")
else:
    print("Invalid die face. Please enter a number between 1 and 6.")
