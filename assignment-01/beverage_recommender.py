def suggest_beverage(meal_type):
    if meal_type.lower() == "breakfast":
        return "Consider having orange juice or coffee!"
    elif meal_type.lower() == "lunch":
        return "How about some lemonade or iced tea?"
    elif meal_type.lower() == "dinner":
        return "Red wine or sparkling water would be great!"
    elif meal_type.lower() == "snack":
        return "A smoothie or a soft drink fits well!"
    else:
        return "Sorry, I don't have a beverage recommendation for that meal type."


while True:
    meal = input("Enter the type of meal you are planning to have: ")
    print(suggest_beverage(meal))
    another_meal = input(
        "Do you want to get a beverage suggestion for another meal? (yes/no): "
    )
    if another_meal.lower() != "yes":
        print("Enjoy your meal and drink responsibly!")
        break
