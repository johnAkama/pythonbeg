#Learning aout list types

cities = ["Accra", "Lagos", "Abidjan", "Dakar", "Cotonou"]
""" print(cities[-2])
school_name = "University of Ghana";
list_from_school = list(school_name)

del cities[2]
Ghana, Nigeria,*rest  = cities

print(rest) """

cities.pop(2)

#print(cities)

student_list = ["John", "Jane", "Doe", "Smith", "Emily"]
student_sores = [85, 92, 78, 90, 88]

student_list_2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
student_sores_2 = [80, 95, 82, 88, 91]


print("Zipping the student lists and scores:")
student_details = list(zip(student_list, student_sores))
print(student_details[0])

print("\n")

print("Merging the student lists and scores:")
student_list.extend(student_list_2)
student_sores.extend(student_sores_2)

print(student_list)

print("\n")

print("Sorting the student list and scores in ascending order:")
student_list.sort()
student_sores.sort()

print(student_list)
print(student_sores)


print(student_list.index("Jane"))


