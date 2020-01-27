farm_animals = {"Sheep", "Cow", "Hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

print("*"*40)

wild_animals = set(["Lion", "Lion", "Panther", "Elephant", "Hare"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

farm_animals.add("Horse")
wild_animals.add("horse")

print(farm_animals)
print(wild_animals)

empty_set = set()
# empty_set2 = {}
# empty_set.add("a")
# empty_set2.add("b")

# even = set(range(0,40,2))
# print(even)
#
# squares_tuple = (4,6,9,16,25)
# print(squares_tuple)
# squares = set(squares_tuple)
# print(squares)

# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# squares_tuples = (4,6,9,16,25)
# squares = set(squares_tuples)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
# print(squares.union(even))
#
# print("*"* 40)
#
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)


even = set(range(0, 40, 2))
print((even))
squares_tuples = (4,6,9,16,25)
squares = set(squares_tuples)
print((squares_tuples))

print("Even minus squares")
print((even.difference(squares)))
print((even - squares))

print("Sqaures minus even")
print(squares.difference(even))
print(squares - even)

print("*" * 40)

# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))

squares.discard(4)
squares.remove(16)
squares.discard(8)
print(squares)
if 8 in squares:
    squares.remove(8)





















