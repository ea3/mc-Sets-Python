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

even = set(range(0,40,2))
print(even)

squares_tuple = (4,6,9,16,25)
print(squares_tuple)
squares = set(squares_tuple)
print(squares)
