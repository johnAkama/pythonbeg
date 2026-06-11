def number_pattern(n):
    if n <= 0:
        return "Argument must be an integer greater than 0."

    if not isinstance(n, int):
        return "Argument must be an integer value."

    return  list(range(1, n + 1))#" ".join(str(num) for num in range(1, n + 1))


print(number_pattern(5))