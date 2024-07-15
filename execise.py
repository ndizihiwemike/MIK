my_list = (2, 3, 4, 6, 44, 90, 2, 400)
list_number = (8, 2, 3, 0, 7)
def highest_number(number_list):
    return max(number_list)

def sum_number(number_list):
    return sum(number_list)

def multiple(list_number):
    start_number = 1
    for num in list_number:
        multiple = start_number * num

        print(highest_number(my_list))
        print(sum_number(my_list))
        print(multiple(list_number))

my_string = "123abcd"
def reverse_string(my_string):
    new_string = ""
    length = len(my_string)
    while length > 0:
        charactor = my_string[length -1]
        new_string += charactor
        length -= 1
    return new_string

print(reverse_string(my_string))

def check(num, start, end):
    return num in range(start, end)
print(check(4, 0, 10))

target_string = "The Quick Blow Fox"
def count_upper_lower(string):
    lower_count = 0
    upper_count = 0
    for charactor in target_string:
        if charactor.islower():
            lower_count += 1
        elif charactor.isupper():
            upper_count += 1
    return f"lowercases{lower_count}, uppercases{upper_count}"
print(count_upper_lower(target_string))
course = 'the quick blow fox'