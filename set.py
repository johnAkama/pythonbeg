# my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2}
"""print(my_set)

my_set.add(11)

print(my_set)"""

my_set = {1, 2, 3, 9, 5, 6}
your_set = {2, 3, 4, 6}

""" print(your_set.issubset(my_set)) # False
print(my_set.issuperset(your_set)) # False# """

# disjointset.
print("Disjoint set:")
print(my_set.isdisjoint(your_set))

# union
print("\nUnion:")
print(my_set | your_set)

# intersection
print("\nIntersection:")
print(my_set & your_set)

print("\nDifference:")
print(my_set - your_set)

print("\nSymmetric Difference:")
print(my_set ^ your_set)
