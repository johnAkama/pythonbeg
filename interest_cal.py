# Practical Exercise 2: Interest Calculator

principal = 1000
rate = 0.05
time = 5


def calculate_interest(principal, rate, time):
    return principal * (1 + rate) ** time - principal


interest = calculate_interest(principal, rate, time)
# print( f"The interest earned on a principal of ${principal} at an annual rate of {rate} over {time} years is ${interest:.2f}.")


# Pratical Exercise 3: Odd and Even Checker
def odd_even_checker(num):
    if isinstance(num, int) and num > 0:
        if num % 2 == 0:
            return f"{num} is an even number."
        else:
            return f"{num} is an odd number."
    else:
        return "Please enter a positive integer."


# print(odd_even_checker(-2))


# Practical Exercise 4: Temprature Converter
def celsius_to_fahrenheit(celsius):

    if isinstance(celsius, int) and celsius >= -273.15:
        f = celsius * 9 / 5 + 32
        return f"The temperature in Fahrenheit is {f:.1f}"


# print(celsius_to_fahrenheit(32))


# Practical Exercise 5: Shooping Total Calculator:
prices = [10, 25, 30]
total_price = sum(prices)
# print(f"The total price of the items is {total_price}")


# Practical Excercise 6: Find Maximum in a List
def largest_num(num_list):
    largest = 0
    for num in num_list:
        if largest > num:
            continue
        else:
            largest = num
    return largest


larg_num = largest_num([90, 23, 12, 40, 10])
# print(larg_num)


# Practical Exercise 7: Count Event Numbers in a List
""" def count_even_num(num_list2):
    count = 0
    for num in num_list2:
        if num % 2 == 0:
            count = count + 1
    count = sum(1 for num in num_list2 if num % 2 == 0)
    return count """


def count_event_second(num):
    return num % 2 == 0


# print(len(list(filter(count_event_second, [12, 8, 4, 6, 10]))))
# print(count_even_num([9, 3, 5, 7, 10]))

# Practical Exercise 8: Remove Duplicates
list_duplicate = [90, 23, 12, 40, 10, 10, 10, 10, 23, 90, 90, 90, 90, 12]


def duplicate_remover(dup_list):

    new_list = []
    for index, num in enumerate(dup_list):
        if num in dup_list[:index]:
            continue
        else:
            new_list.append(num)
            # new_list.append(num)
    return new_list


# print(duplicate_remover(list_duplicate))


# Practical Exercise 9: Tuples unpacking


def tuple_unpacker(tup):
    if len(tup) != 3:
        return "The tuple has to have 3 elements"
    else:
        name, age, location = tup
        return (name, age, location)


# print(tuple_unpacker(("John Le Grand", 20, "Kumasi")))


# Practical Exercse 10: List Comprehension


def square(val):
    return val**2


list_val = [90, 23, 12, 40, 10]
square_val = list(map(square, list_val))  # Using map function

comp_square = [num**2 for num in list_val]  # List comprehension

print(comp_square)
