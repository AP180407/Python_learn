cube = lambda x: x ** 3

print(cube(3))
# lambda function is an anonymous function that can take any number of arguments, but can only have one expression. In this example, we define a lambda function that takes a single argument x and returns its cube (x raised to the power of 3). We then call this lambda function with the argument 3 and print the result, which is 27.
# lamda is use for small functions which is use ony once inthe code.

def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 4, 5))
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))
# *args is used for multiple arguments in function.

# Function with **kwargs

def print_name_key(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

user_input = input("Enter key=value pairs separated by space: ")

pairs = user_input.split()

data = {}

for pair in pairs:
    key, value = pair.split("=")
    data[key.strip()] = value.strip()

print_name_key(**data)

#9. Generator Function with yield

def even_genretor(limit):
    for i in range(2, limit +1,2):
        yield(i)

for num in even_genretor(10):
    print(num)  

#yield for memory storage and for loop for iterating the generator function.

#10. Recursive Function to Calculate Factorial

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)