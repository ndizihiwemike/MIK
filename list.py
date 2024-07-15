fruits = ["oranges", "mangoes", "passions"]
names = ["Hope", "David", "MIKE", "Ian"]
#list methods
print(fruits)
fruits.append("guava")
print(fruits)
print(len(fruits))
print(fruits.count("oranges"))
print(names.count("MIKE"))
fruits.insert(1, "pineapple")
print(fruits)
fruits.pop()#removes the last item from the list
print(fruits)
fruits.remove("mangoes")
print(fruits)
fruits.extend(names)
print(fruits)
print(sorted(fruits))#returns a sorted list
print(sorted(fruits, reverse=True))#returns sorted
copied = fruits.copy()
print(copied)
fruits.clear()#deletes all the items in fruits
print(fruits)