#Learning aout list types

cities = ["Accra", "Lagos", "Abidjan", "Dakar", "Cotonou"]
print(cities[-2])
print("\n")
school_name = "University of Ghana";
list_from_school = list(school_name)

del cities[2]
Ghana, Nigeria,*rest  = cities

print(rest)