import json 
Ian = {
    "name":"mike",
    "gender":"male",
    "age":21
}
print(Ian)
Ian.update({"nationality":"ugandan"})
print(Ian)
Ian['location'] = "kawanda"
print(Ian)
Ian.setdefault("height","10 feet")
print(Ian)
Ian.setdefault("name", "isaac")
print(Ian)
del Ian['location']
print(Ian)
Ian.popitem()#deletes the last inserted key value
print(Ian)
Ian.pop("age")#deletes age from Ian
print(Ian)
print(Ian.keys)
print(Ian.values)
print(Ian.items())
print(Ian.get("name"))
print(Ian["name"])
print(json.dumps(Ian, indent=2))


name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")
details = {
    "name": name,
    "age":age,
    "gender":gender
}
print(json.dumps(details, indent=2))
