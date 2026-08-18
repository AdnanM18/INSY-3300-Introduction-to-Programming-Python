try:
    num_list = [100.7, 20.6, 7.6, 89.4, 93.9, 23, 47, 66, 12]

    # Relative path used so the project works on any computer.
    file_path = "calculations.txt"

    with open(file_path, "w") as file:
        for num in num_list:
            file.write(str(num) + "\n")

    with open(file_path, "r") as file:
        lines = file.readlines()
        num_list = [float(line.strip()) for line in lines]

    sum_nums = sum(num_list)
    avg_nums = sum_nums / len(num_list)
    max_num = max(num_list)
    min_num = min(num_list)

    with open(file_path, "a") as file:
        file.write(f"Sum: {sum_nums:.2f}\n")
        file.write(f"Average: {avg_nums:.2f}\n")
        file.write(f"Max: {max_num}\n")
        file.write(f"Min: {min_num}\n")

except FileNotFoundError:
    print("Error: File not found.")
except ValueError:
    print("Error: Non-numeric data found in the file.")
except Exception as e:
    print(f"An error occurred: {e}")
