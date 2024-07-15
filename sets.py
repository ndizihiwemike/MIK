#sets  method
fruits = {"apple", "banana", "cherry"}
print(fruits)
fruits.add("orange") #adds items to the set
print(fruits)



fruits = {"apple", "banana", "cherry"}
x = fruits.copy() #returns a copy of the set
print(x)



x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
#returns a set that contains the items that only exist in x but not y
z = x.difference(y)
print(z)
z = y.difference(x)
print(z)



x = {"apple","juice", "banana", "cherry"}
y = {"google","juice", "microsoft", "apple"}
x.difference_update(y)
print(x)
y.difference_update(x)
print(y)

x = {"apple", "banana", "cherry"}
fruits.discard("banana") #discard a banana from the list #discard is similar to remove
print(fruits)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y) #returns a set tht is the intersection of the two sets
print(z)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y) #modifies a new set and returns items tht a common in the two sets
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y) #returns whther the sets have an intersection or not
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.issubset(y) #checks for a subset whether a given set contains the other set
print(z)
x = {"apple", "banana", "cherry", "a", "b", "c", "d"}
y = {"c", "banana", "apple"}
z = y.issubset(x)
print(z)

x = {"apple", "banana", "cherry", "a", "b", "c", "d"}
y = {"c", "banana", "apple"}
z = y.issuperset(x) #checks whether a set contains another set
print(z)
x = {"apple", "banana", "cherry", "a", "b", "c", "d"}
y = {"c", "banana", "apple"}
z = x.issuperset(y)
print(z)


fruits = {"apple", "banana", "cherry"}
fruits.pop() #removes a random item from the list of the set
print(fruits)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y) #returns all the items in the set
print(z)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y) #returns all the items in the set minus the common or intersection
print(z)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
 #removes the items present in both or all sets and inserts the items that are not present in both or all sets
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
y.symmetric_difference_update(x)
 #removes the items present in both or all sets and inserts the items that are not present in both or all sets
print(y)