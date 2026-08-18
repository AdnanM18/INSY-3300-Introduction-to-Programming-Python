def calculate_percentage(num_students_science, num_students_arts):
    total_students = num_students_science + num_students_arts
    percentage_science = (num_students_science / total_students) * 100
    percentage_arts = (num_students_arts / total_students) * 100
    return percentage_science, percentage_arts


num_students_science = int(input("Enter number of students studying science: "))
num_students_arts = int(input("Enter number of students studying arts: "))

percentage_science, percentage_arts = calculate_percentage(
    num_students_science, num_students_arts
)

if percentage_science > percentage_arts:
    print("Science is the more popular subject")
elif percentage_arts > percentage_science:
    print("Arts is the more popular subject")
else:
    print("Both subjects are equally popular")
