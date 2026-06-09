list_fruit = ["grape", "orange", "tomatoes", "manago", "pawpaw", "lemon"]

# Implementing the comprehension to create a new list of fruits that have more than 5 characters in their name
# long_fruit_name = [fruit for fruit in list_fruit if len(fruit) <6]

new_fruit_list = []


def check_fruit_name(fruits):
    if len(fruits) < 6:
        new_fruit_list.append(fruits)
        return True


comp_test = list(filter(check_fruit_name, list_fruit))

print("New object created using comprehension")
print(new_fruit_list)


print("\n Second method using comprehension")
print(comp_test)
