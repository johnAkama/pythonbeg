# Pratical Exercise 10: Sum method practice
student_score = [10, 23, 44, 5, 3, 64, 64, 21, 53, 635, 74, 74, 90]


def average_cal(scores):
    total_score = sum(scores)
    total_values = len(scores)
    average_score = total_score / total_values

    return average_score


# print(f"{average_cal(student_score):.2f}")


# Practical Exercise 11: List comprehension- squares

numbers = [num for num in range(1, 21)]


def squares_num(num):
    return num**2


square_list = list(map(squares_num, numbers))

# print(square_list)


# Practical Exercise 12: Filter Odd Numbers.

odd_number = [odd for odd in numbers if odd % 2 != 0]

# print(odd_number)


# Practical Exercise 13: ord Leg counter:

word_list = ["apple", "banana", "Kodjo", "Daniel", "George"]
# length_w = [len(word) for word in word_list]


def word_count(word_list):
    word_lengh = []
    for word in word_list:
        word_lengh.append(len(word))
    return word_lengh


# print(length_w)
# print(word_count(word_list))


# Practical Exercise 14: Function Greetin Generator
def greeting(name):
    return f"Hello, {name}"


# print(greeting("John"))


# Practical Exercise 15: Password Checker
password = "asadfcae5vae"


def password_checker(passw):
    if len(passw) < 8:
        return "Password should be at least 8 charactes"

    passw_list = list(passw)
    for pass_char in passw_list:
        print(f" System test for integer on {pass_char}")
        if pass_char.isdigit():
            break
    else:
        return "Password should contain at least one digit"

    return True


# print(password_checker(password))


# Practical Exercise 17: Combine Two List

list_source = [1, 2, 3, 4, 5]
list_target = [4, 3, 8, 9, 10]


def combine_list(list1, list2):
    for num in list2:
        if num in list1:
            continue
        else:
            list1.append(num)
    return list1


print(combine_list(list_source, list_target))
