# int
# bool
# list
# tuple
# float
# str
# dict
# Primitive data types - already pre-defined data structures within a programming language
# Abstract data types - conceptual data structures defining how data is structured and handled.

"""
    Multi-line comment
"""

# Duck Typing -> declaring variables without explicitly specifying the data type e.g. its not int num1 = 10 but num1 = 10, avoiding type annotations
num0 = 10 # without type annotations
num1:int = 10 # integer, with type annotations
name:str = 'Lawrence Muchiri' # string
avg:float = 7.6 # float
names:list = ["Mary","John"] # list
is_true:bool = True
cars:tuple = ("Volvo","Ferrari","") # Immutable
marks:set = [1,2,3,4,5,6,7,8,9]

print(f'Name: {names[0]}\n Age: {num1}\n GPA: {avg}')
names.append("Ruth")
# names.remove("John")
names.pop(0)
print(names)
# names.clear()
# Control structures
# Loops, iterations
# for i in range(10):
#     print(i)

# for name in names:
#     print(name)

x:int = 0
std:dict = {
    "Name:":"Alice",
    "Age":21
}
students:list = [
    {
        "Name:":"Alice",
        "Marks":[99,76,87]
    },
    {
        "Name:":"Mark",
        "Marks":[99,80,70]
    }
]
students2:list = [
    {
        "student_name":"Alice","Marks":[99,85,68],
        "student_name":"Bob","Marks":[99,90,56],
        "student_name":"Bob","Marks":[99,90,56]
    }
]
print(x if x == x else False)

# -> 
def func() -> None:
    print("Function declaration here")
    age = 20

    for j in "names":
        if age >= 20:
            print(age)

func()

for Student in students: 
    print(Student.Name)
    
def average(marks:list[int]) -> float:
    return sum(marks) / len(marks)

# Compute marks for every student and print it out on the terminal
# *args -> the method can take an unlimited amount of parameters
# **kargs -> creates a dictionary for you.