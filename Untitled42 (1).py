#!/usr/bin/env python
# coding: utf-8

# Q1- In Python, what is the difference between a built-in function and a user-defined function? Provide an
# example of each.
# A1- In Python, a built-in function is a function that is already defined and available for use in the Python interpreter. These functions are part of the Python language and are always available, without the need to import any modules or define them yourself. Examples of built-in functions include print(), len(), type(), and sum().
# 
# On the other hand, a user-defined function is a function that is defined by the user, typically in a Python script or module. These functions are created by the programmer to perform a specific task or set of tasks.
# Here are examples of each:
# 
# Built-in function:

# In[ ]:


# Using the built-in function `len()` to get the length of a string
my_string = "Hello, World!"
print(len(my_string))  # Output: 13


# In this example, we're using the built-in len() function to get the length of the string my_string.
# 
# User-defined function:

# In[ ]:


# Defining a user-defined function `greet()` to print a greeting message
def greet(name):
    print(f"Hello, {name}!")

# Calling the user-defined function
greet("John")  # Output: Hello, John!


# In this example, we're defining a user-defined function greet() that takes a name parameter and prints a greeting message. We then call the function by passing the argument "John".
# 
# Key differences between built-in and user-defined functions:
# 
# Availability: Built-in functions are always available, while user-defined functions need to be defined before they can be used.
# Scope: Built-in functions have global scope, while user-defined functions have local scope (unless they're defined in a module or package).
# Customizability: User-defined functions can be tailored to perform specific tasks or calculations, while built-in functions are general-purpose and may not always fit the exact needs of a particular problem.
# I hope this helps

# Q2- How can you pass arguments to a function in Python? Explain the difference between positional
# arguments and keyword arguments.
# A2- In Python, you can pass arguments to a function using parentheses () after the function name. There are two ways to pass arguments: positional arguments and keyword arguments.
# 
# Positional Arguments: Positional arguments are passed to a function in the order they are defined in the function's parameter list. The function assigns the arguments to the parameters based on their position.
# 
# Example:

# In[ ]:


def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("John", 30)  # Output: Hello, John! You are 30 years old.


# In this example, "John" is assigned to the name parameter, and 30 is assigned to the age parameter, based on their position in the function call.
# 
# Keyword Arguments: Keyword arguments are passed to a function using the parameter name followed by an equal sign = and the value. This allows you to pass arguments in any order, as long as the parameter names match.

# In[ ]:


def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet(age=30, name="John")  # Output: Hello, John! You are 30 years old.


# In this example, we pass the age argument with the value 30 and the name argument with the value "John", using keyword arguments. The order of the arguments doesn't matter, as long as the parameter names match.
# 
# Mixing Positional and Keyword Arguments: You can also mix positional and keyword arguments, but positional arguments must come before keyword arguments.
# 
# Example:

# In[ ]:


def greet(name, age, country):
    print(f"Hello, {name}! You are {age} years old from {country}.")

greet("John", age=30, country="USA")  # Output: Hello, John! You are 30 years old from USA.


# In this example, we pass the name argument positionally, and the age and country arguments using keyword arguments.
# 
# Default Values: You can also specify default values for function parameters, which are used if the argument is not provided.
# 
# Example:

# In[ ]:


def greet(name, age=25, country="USA"):
    print(f"Hello, {name}! You are {age} years old from {country}.")

greet("John")  # Output: Hello, John! You are 25 years old from USA.


# In this example, we define default values for age and country, which are used if the arguments are not provided.
# 
# I hope this helps you understand how to pass arguments to functions in Python!

# Q3- What is the purpose of the return statement in a function? Can a function have multiple return
# statements? Explain with an example.
# A3- In Python, the return statement is used to exit a function and return a value to the caller. The purpose of the return statement is to:
# 
# Terminate the function: When a return statement is encountered, the function execution stops, and the function returns control to the caller.
# Return a value: The return statement can also return a value to the caller, which can be assigned to a variable or used in an expression.
# A function can have multiple return statements, but only one of them will be executed, depending on the flow of the program. Here's an example:

# In[ ]:


def greet(name):
    if name == "John":
        return "Hello, John!"
    elif name == "Jane":
        return "Hi, Jane!"
    else:
        return "Hello, stranger!"

print(greet("John"))  # Output: Hello, John!
print(greet("Jane"))  # Output: Hi, Jane!
print(greet("Bob"))   # Output: Hello, stranger!


# In this example, the greet function has three return statements, but only one of them is executed, depending on the value of the name parameter.
# 
# Here's what happens:
# 
# When name is "John", the first return statement is executed, and the function returns "Hello, John!".
# When name is "Jane", the second return statement is executed, and the function returns "Hi, Jane!".
# When name is anything else, the third return statement is executed, and the function returns "Hello, stranger!".
# Note that once a return statement is executed, the function terminates, and any code after the return statement is not executed.
# 
# In summary, the return statement is used to exit a function and return a value to the caller. A function can have multiple return statements, but only one of them will be executed, depending on the flow of the program.

# Q4- What are lambda functions in Python? How are they different from regular functions? Provide an
# example where a lambda function can be useful.
# A4- Lambda Functions in Python
# 
# In Python, a lambda function is a small, anonymous function that can be defined inline within a larger expression. It's a shorthand way to create a function without a declared name. Lambda functions are often used when you need a short, one-time-use function.
# 
# Syntax

# In[ ]:


lambda arguments: expression


# Here, arguments is a comma-separated list of variables, and expression is the code that will be executed when the lambda function is called.
# 
# Differences from Regular Functions
# 
# Here are the key differences between lambda functions and regular functions:
# 
# Anonymous: Lambda functions don't have a declared name.
# Inline definition: Lambda functions are defined directly within an expression, whereas regular functions are defined separately.
# Single expression: Lambda functions can only contain a single expression, whereas regular functions can have multiple statements.
# No return statement: Lambda functions implicitly return the result of the expression, whereas regular functions require an explicit return statement.
# Example: Sorting a List of Tuples
# 
# Here's an example where a lambda function can be useful:

# In[ ]:


students = [('John', 20), ('Alice', 22), ('Bob', 19)]

# Sort the list of tuples by the second element (age) in descending order
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

print(sorted_students)  # Output: [('Alice', 22), ('John', 20), ('Bob', 19)]


# In this example, we use a lambda function as the key function for the sorted function. The lambda function takes a tuple x as input and returns its second element x[1], which is the age. The sorted function then uses this lambda function to sort the list of tuples by age in descending order.
# 
# Why lambda functions are useful here
# 
# In this example, we only need a simple, one-time-use function to extract the age from each tuple. A lambda function is perfect for this task, as it's concise and doesn't clutter the code with a separate function definition.

# Q5- How does the concept of "scope" apply to functions in Python? Explain the difference between local
# scope and global scope.
# A5- Scope in Python Functions
# 
# In Python, the scope of a variable or function refers to the region of the code where it is accessible and can be used. In the context of functions, scope determines which variables are available within a function and how they can be modified.
# 
# Local Scope
# 
# A local scope refers to the region within a function where variables are defined and can be accessed. Variables defined within a function have local scope and are only accessible within that function. When a function is called, a new local scope is created, and variables defined within the function are stored in this scope.
# for example

# In[ ]:


def greet(name):
    message = f"Hello, {name}!"  # message has local scope
    print(message)

greet("John")  # Output: Hello, John!
print(message)  # Error: message is not defined (outside local scope)


# In this example, the message variable is defined within the greet function and has local scope. It can only be accessed within the function, and attempting to access it outside the function results in an error.
# 
# Global Scope
# 
# A global scope refers to the region of the code that is accessible from anywhere in the program. Variables defined outside of any function have global scope and can be accessed from anywhere in the program.
# for example

# In[ ]:


global_message = "Hello, World!"  # global_message has global scope

def greet(name):
    print(global_message)  # Accessing global_message from within a function
    print(f"Hello, {name}!")

greet("John")  # Output: Hello, World! Hello, John!
print(global_message)  # Output: Hello, World! (accessible from anywhere)


# In this example, the global_message variable is defined outside of any function and has global scope. It can be accessed from anywhere in the program, including within functions.
# 
# Key differences between local and global scope
# 
# Here are the key differences between local and global scope:
# 
# Accessibility: Local variables are only accessible within the function where they are defined, while global variables are accessible from anywhere in the program.
# Lifetime: Local variables are created and destroyed when the function is called and returns, while global variables exist throughout the program's execution.
# Modifiability: Local variables can be modified within the function, while global variables can be modified from anywhere in the program (although this is generally discouraged for maintainability and readability reasons).
# By understanding the concept of scope in Python, you can write more effective andmodular code, and avoid common pitfalls like variable name collisions and unintended side effects.

# Q6- How can you use the "return" statement in a Python function to return multiple values?
# A6- Returning Multiple Values in Python Functions
# 
# In Python, the return statement is used to exit a function and return a value to the caller. By default, a function can only return a single value. However, there are several ways to return multiple values from a function:
# 
# 1. Returning a Tuple
# 
# One way to return multiple values is to return a tuple, which is an immutable collection of values. You can create a tuple by separating values with commas and enclosing them in parentheses.
# Here's an example:

# In[ ]:


def calculate_area_and_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter  # Return a tuple of two values

area, perimeter = calculate_area_and_perimeter(4, 5)
print(f"Area: {area}, Perimeter: {perimeter}")  # Output: Area: 20, Perimeter: 18


# In this example, the calculate_area_and_perimeter function returns a tuple containing two values: area and perimeter. The caller can then unpack these values into separate variables using tuple unpacking.
# 
# 2. Returning a List
# 
# Another way to return multiple values is to return a list, which is a mutable collection of values. You can create a list by enclosing values in square brackets.
# 
# Here's an example:

# In[ ]:


def get_user_info():
    name = "John Doe"
    age = 30
    occupation = "Software Engineer"
    return [name, age, occupation]  # Return a list of three values

user_info = get_user_info()
print(f"Name: {user_info[0]}, Age: {user_info[1]}, Occupation: {user_info[2]}")


# In this example, the get_user_info function returns a list containing three values: name, age, and occupation. The caller can then access these values using indexing.
# 
# 3. Returning a Dictionary
# 
# You can also return multiple values as a dictionary, which is an unordered collection of key-value pairs. You can create a dictionary by enclosing key-value pairs in curly braces.
# 
# Here's an example:

# In[ ]:


def get_user_profile():
    name = "Jane Doe"
    age = 25
    occupation = "Data Scientist"
    return {"name": name, "age": age, "occupation": occupation}  # Return a dictionary

user_profile = get_user_profile()
print(f"Name: {user_profile['name']}, Age: {user_profile['age']}, Occupation: {user_profile['occupation']}")


# In this example, the get_user_profile function returns a dictionary containing three key-value pairs: name, age, and occupation. The caller can then access these values using dictionary keys.
# 
# Conclusion
# 
# In Python, you can return multiple values from a function using tuples, lists, or dictionaries. Each approach has its own advantages and disadvantages, and the choice of which one to use depends on the specific use case and personal preference.

# Q7-  What is the difference between the "pass by value" and "pass by reference" concepts when it
# comes to function arguments in Python?
# A7-  Pass by Value vs Pass by Reference in Python
# 
# When you pass arguments to a function in Python, you might wonder what happens to those arguments behind the scenes. Do they get copied, or do they get modified in place? This is where the concepts of "pass by value" and "pass by reference" come in.
# 
# Pass by Value
# 
# In pass by value, a copy of the original value is passed to the function. This means that any changes made to the argument within the function do not affect the original value outside the function.
# for example- 

# In[ ]:


def increment(x):
    x += 1
    print(f"Inside function: x = {x}")

x = 5
increment(x)
print(f"Outside function: x = {x}")  # Output: x = 5 (unchanged)


# In this example, the increment function takes an integer x as an argument. When we call the function, a copy of the original value 5 is passed to the function. The function increments the copy, but the original value x outside the function remains unchanged.
# 
# Pass by Reference
# 
# In pass by reference, a reference to the original value is passed to the function. This means that any changes made to the argument within the function affect the original value outside the function.
# 
# for example:

# In[ ]:


def append_to_list(lst):
    lst.append(4)
    print(f"Inside function: lst = {lst}")

lst = [1, 2, 3]
append_to_list(lst)
print(f"Outside function: lst = {lst}")  # Output: lst = [1, 2, 3, 4] (modified)


# In this example, the append_to_list function takes a list lst as an argument. When we call the function, a reference to the original list is passed to the function. The function appends a new element to the list, and the original list outside the function is modified.
# 
# The Twist: Python's "Pass by Object Reference"
# 
# Now, here's the important part: Python doesn't exactly follow the traditional "pass by value" or "pass by reference" approach. Instead, it uses a hybrid approach called pass by object reference.
# In Python, when you pass an argument to a function, a reference to the original object is passed. However, if the object is immutable (like an integer or a string), any changes made to the argument within the function create a new object, leaving the original object unchanged. If the object is mutable (like a list or a dictionary), changes made to the argument within the function affect the original object.
# 
# Here's an example that demonstrates this:

# In[ ]:


def modify_string(s):
    s += " world"
    print(f"Inside function: s = {s}")

s = "hello"
modify_string(s)
print(f"Outside function: s = {s}")  # Output: s = hello (unchanged)

def modify_list(lst):
    lst.append(4)
    print(f"Inside function: lst = {lst}")

lst = [1, 2, 3]
modify_list(lst)
print(f"Outside function: lst = {lst}")  # Output: lst = [1, 2, 3, 4] (modified)


# In the first example, the modify_string function takes a string s as an argument. When we call the function, a reference to the original string is passed. However, since strings are immutable, the function creates a new string object when we try to modify it, leaving the original string unchanged.
# 
# In the second example, the modify_list function takes a list lst as an argument. When we call the function, a reference to the original list is passed. Since lists are mutable, the function can modify the original list.

# Conclusion
# 
# In Python, the "pass by value" and "pass by reference" concepts are not strictly followed. Instead, Python uses a "pass by object reference" approach, where a reference to the original object is passed to the function. The behavior of the function depends on whether the object is immutable or mutable. Understanding this nuance is essential to writing effective and predictable code in Python.

# In[ ]:


Q8- Create a function that can intake integer or decimal value and do following operations:
a. Logarithmic function (log x)
b. Exponential function (exp(x))
c. Power function with base 2 (2
x
)

d. Square root
A8- Here is a Python function that performs the operations you specified:


# In[3]:


import math

def math_operations(x):
    """
    Perform various mathematical operations on a given value x.

    Args:
        x (int or float): The input value.

    Returns:
        A dictionary with the results of each operation.
    """
    results = {}

    # a. Logarithmic function (log x)
    results['log'] = math.log(x)

    # b. Exponential function (exp(x))
    results['exp'] = math.exp(x)

    # c. Power function with base 2 (2^x)
    results['power_2'] = 2 ** x

    # d. Square root
    results['sqrt'] = math.sqrt(x)

    return results


# In[ ]:


Here's an explanation of the code:

We import the math module, which provides functions for mathematical operations.
The math_operations function takes a single argument x, which can be an integer or a float.
We create an empty dictionary results to store the results of each operation.
We perform each operation and store the result in the results dictionary:
math.log(x) calculates the natural logarithm of x.
math.exp(x) calculates the exponential function of x.
2 ** x calculates the power function with base 2.
math.sqrt(x) calculates the square root of x.
Finally, we return the results dictionary, which contains the results of each operation.
You can call the function with an integer or float value, like this:


# In[ ]:


x = 4
results = math_operations(x)
print(results)
# Output: {'log': 1.3862943611198906, 'exp': 54.598150033144236, 'power_2': 16, 'sqrt': 2.0}

x = 3.5
results = math_operations(x)
print(results)
# Output: {'log': 1.252762968495368, 'exp': 33.11545195869231, 'power_2': 11.31370849898476, 'sqrt': 1.8708286933869707}


# Note that the math.log function raises a ValueError if x is negative, and the math.sqrt function raises a ValueError if x is negative. You may want to add error handling to the function to handle these cases.

# In[ ]:


Q9- Create a function that takes a full name as an argument and returns first name and last name.
A9- Here is a Python function that takes a full name as an argument and returns the first name and last name:


# In[ ]:


def split_full_name(full_name):
    """
    Split a full name into first name and last name.

    Args:
        full_name (str): The full name, e.g. "John Doe"

    Returns:
        A tuple containing the first name and last name, e.g. ("John", "Doe")
    """
    names = full_name.split()
    if len(names) == 1:
        return names[0], ""  # Return the full name as first name if no space is found
    elif len(names) == 2:
        return names[0], names[1]
    else:
        # Handle cases with multiple middle names
        first_name = names[0]
        last_name = " ".join(names[1:])
        return first_name, last_name


# Here's an explanation of the code:
# 
# The function takes a full_name string as an argument.
# We split the full_name string into a list of names using the split() method, which splits on whitespace characters.
# We check the length of the names list:
# If it's 1, we return the full name as the first name, and an empty string as the last name (in case the input is a single name).
# If it's 2, we return the first element as the first name, and the second element as the last name.
# If it's more than 2, we assume there are multiple middle names, and we join the remaining elements (except the first one) into a single string using the join() method, and return it as the last name.
# You can call the function with a full name string, like this:

# In[ ]:


full_name = "John Doe"
first_name, last_name = split_full_name(full_name)
print(first_name, last_name)  # Output: John Doe

full_name = "John Michael Doe"
first_name, last_name = split_full_name(full_name)
print(first_name, last_name)  # Output: John Michael Doe

full_name = "John"
first_name, last_name = split_full_name(full_name)
print(first_name, last_name)  # Output: John 


# Note that this implementation assumes that the full name is separated by spaces, and that the first name is the first word, and the last name is the remaining words. You may want to add more sophisticated logic to handle edge cases, such as names with apostrophes or non-English characters.
