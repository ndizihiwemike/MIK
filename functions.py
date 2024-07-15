#code that is executed upon request
#function perform a specific task
#functions allow argument or parameters
def addition_function(num1, num2):
    summed = num1 + num2
    return summed
print(addition_function(20, 30))
print(addition_function(-30, -40))
print(addition_function(-20, 50))

    #function allowing arguments
def function_two(*args):
    return args
print(function_two("santos", "becky", "liz", "mike"))
     #4,3,5,6,7,6,9,8,

def summed(*args):
    return sum(args)
print(summed(1,2,3,4,5,6,9))

#function allowing key word arguments
def computers(**kwargs):
    return kwargs
print(computers(computer_name="lenovo", brand="windows 12 pro", model="2023"))

def greeting(name):
    message = f"hello {name}, how are you doing bro"
    return message
print(greeting("mike"))
named = input("enter your name: ")
print(greeting(named))

def square_of_num(num):
    return num ** 2
print(square_of_num(5))

subtraction = lambda x, y : x - y
print(subtraction(30, 15))

def decorator(func):
    def wrapper(*args, **kwargs):
        print("before calling the function")
        func(*args, **kwargs)
        print(func(*args, **kwargs))
        print("after the call ofthe function")
    return wrapper

@decorator
def greet_sanny(name):
    return f"hello {name}"
greet_sanny("mike")