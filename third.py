#data structures
my_string = "  I am going to school  "
print(len(my_string))#the length of the string 
print(my_string.upper())#transforms to upper case
print(my_string.lower())#transforms to lower case
print(my_string.replace("am","was"))#replaces words
print(my_string.strip())#removes whitespace
print(len(my_string.strip()))#length of the string after whitespace rem
print(my_string.swapcase())#changes the case of the string
print(my_string.title())#returns a capitalised format
print(my_string.find("am"))#returns index of am
print(my_string[0:15])#returns a sliced string
print(my_string.rfind("g"))#last occurance of g
print(my_string.capitalize())#changes the case of the 1st charater
print("was" in my_string)#returns a boolean
print(my_string.split(" "))#splits the string, returns a list
print(my_string.endswith("Ian"))
print(my_string.startswith(" "))
print(my_string.islower())
print(my_string.isupper())
print(my_string.isdigit())