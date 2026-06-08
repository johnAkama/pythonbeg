new_languages = [
    "Spain",
    "Cyprus",
    "Italy",
    "Germany",
    "France",
    "Portugal",
    "Greece",
    "Netherlands",
    "Belgium",
    "Denmark",
]

list_with_enum = list(enumerate(new_languages))

# print(list_with_enum)

for index, country in list_with_enum:

    if index >= 5:
        break
    else:
        print(f"first batch of coountry\n{index}: {country}")
