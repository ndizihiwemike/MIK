import json
name = input("enter your name ")
age = input("enter your age ")
gender = input("enter your gender ")
occupation = input("enter your occupation ")
country = input("enter your country ")
details = {
    "name":name,
    "age":age,
    "gender":gender,
    "occupation":occupation,
    "country":country,
}
print(json.dumpfp(details, indent= 2))


