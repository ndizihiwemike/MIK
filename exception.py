#exception handling 
try:
    print(name)
except NameError as e:
     print("there was an error, {e}")
else:
     pass
finally:
     print("this always excecuted")
"""
4 modes while working with files
1. create mode -> x
2. read mode -> r
3, write mode -> w
4. append mode -> a
"""

try:
    open("mylog.txt", "x")
except FileExistsError as e:
      print(e)
import json
txt = open("mylog.txt", "w")
massage = {
     "error id": 1,
     "process":"creation of the user",
     "error":"user already defined"
}
txt.writelines(f"\n{json.dumps(massage, indent=2)}")
txt.close()
text = open("mylog.txt","r")
read_content = text.read()
print(read_content)
text.close()