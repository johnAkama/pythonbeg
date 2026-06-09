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
        #print(f"first batch of coountry\n{index}: {country}")
        continue;


developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]


new_list = list(zip(developers,ids))
#print(new_list)


even_num = []

for num in range(21):
    if num%2 == 0:
       even_num.push(num)
    else:
        print(f'{num} is not an even number \n')