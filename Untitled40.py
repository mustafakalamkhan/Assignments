#!/usr/bin/env python
# coding: utf-8

# Q.1. What are keywords in python? Using the keyword library, print all the python keywords.
# 
# A1-  In Python, keywords are special words that have a specific meaning and are used to define the structure and syntax of the language. They cannot be used as variable names or identifiers.
# 
# To print all the Python keywords, you can use the keyword library. Here's an example:

# In[ ]:


import keyword
print(keyword.kwlist)


# This will output:

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# These are all the keywords in Python. You can also use the help() function to get more information about a specific keyword. For example:

# In[ ]:


help("pass")


# This will output:

# In[ ]:


The "pass" statement
*******************

   pass_stmt ::= "pass"

"pass" is a null operation — when it is executed, nothing happens. It
is useful as a placeholder when a statement is required syntactically,
but no code needs to be executed, for example:

   def f(arg): pass    # a function that does nothing (yet)

   class C: pass       # a class with no methods (yet)


# Q.2. What are the rules to create variables in python?
# 
# A2-  In Python, the rules to create variables are as follows:
# 
# Variable names can only contain letters (a-z or A-Z), digits (0-9), and underscores (_): You can use any combination of these characters to create a variable name.
# 
# Variable names cannot start with a digit: You cannot start a variable name with a number. For example, 1var is not a valid variable name.
# 
# Variable names are case-sensitive: Python is case-sensitive, which means that var and Var are considered two different variable names.
# 
# Variable names cannot be Python keywords: You cannot use Python keywords (such as if, else, for, while, etc.) as variable names.
# 
# Variable names should be descriptive and follow a consistent naming convention: While not a strict rule, it's a good practice to use descriptive variable names that indicate what the variable represents. Python's PEP 8 style guide recommends using lowercase letters with words separated by underscores (e.g., hello_world).
# 
# Here are some examples of valid and invalid variable names in Python:
# 
# Valid variable names:
# 
# hello
# hello_world
# x
# my_variable
# _private_var
# 
# Invalid variable names:
# 
# 1st_variable (starts with a digit)
# if (Python keyword)
# hello world (contains a space)
# hello-world (contains a hyphen)
# hello@world (contains a special character)
# Remember, following these rules will help you create valid and readable variable names in Python!

# Q.3. What are the standards and conventions followed for the nomenclature of variables in
# python to improve code readability and maintainability?
# 
# A3-  In Python, there are several naming conventions and standards that are commonly followed to improve code readability and maintainability. These conventions are not strictly enforced by the language, but they are widely accepted and recommended by the Python community. Here are some of the most important conventions for naming variables:
# 
# Use lowercase letters with words separated by underscores: This convention is known as "snake_case" and is commonly used for naming variables in Python. For example, my_variable_name.
# 
# Do not use underscores at the beginning of a variable name: Variable names that start with an underscore are often used for special purposes in Python, such as indicating private variables. Therefore, it's best to avoid using underscores at the beginning of a variable name.
# 
# Do not use camelCase: CamelCase is a naming convention commonly used in other programming languages, but it's not typically used in Python. Instead, use snake_case for variable names.
# 
# Use descriptive variable names: Variable names should be descriptive and indicate what the variable represents. Avoid using vague or ambiguous variable names.
# 
# Avoid using single-letter variable names: While single-letter variable names can be convenient, they can also be confusing and hard to read. Use descriptive variable names instead.
# 
# Use consistent naming conventions: Once you've chosen a naming convention for your variables, stick with it throughout your code. Consistency is key to readability and maintainability.
# 
# 

# Q.4- What will happen if a keyword is used as a variable name?
# A4-  In Python, keywords are reserved words that have special meanings and are used to define the syntax and structure of the language. Therefore, you cannot use a keyword as a variable name. If you try to do so, you will get a syntax error.

# Q.5. For what purpose def keyword is used?
# A5-  In Python, the def keyword is used to define a function. It is used to declare a function, which is a block of code that can be executed multiple times from different parts of your program.
# 
# The basic syntax of a function definition using the def keyword is as follows:

# In[ ]:


def function_name(parameters):
    # function body
    pass


# Here, function_name is the name of the function, parameters are the input values that the function accepts, and function body is the code that is executed when the function is called.
# 
# For example:

# In[ ]:


def greet(name):
    print("Hello, " + name + "!")

greet("John")  # Output: Hello, John!


# In this example, greet is a function that takes a name parameter and prints a greeting message. The def keyword is used to define the function, and the function can be called multiple times with different input values.
# 
# The def keyword is an essential part of Python's syntax, and it allows you to create reusable code blocks that can be used throughout your program.

# Q.6- What is the operation of this special character ‘\’?
# A6-  In Python, the special character '' is called the escape character or backslash. It is used to escape special characters in strings, which means it allows you to use characters that have a special meaning in Python in a string.
# 
# Here are some examples of how the '' character is used:
# 
# To include a quote in a string: If you want to include a quote in a string, you can use the '' character to escape it. For example:

# In[ ]:


print("It\'s a beautiful day")  # Output: It's a beautiful day


# In this example, the '' character is used to escape the single quote in the string.
# 
# To include a backslash in a string: If you want to include a backslash in a string, you can use another backslash to escape it. For example:

# In[ ]:


print("C:\\Users\\username\\Documents")  # Output: C:\Users\username\Documents


# In this example, the '\' characters are used to include a backslash in the string.
# 
# To include special characters in a string: The '' character can be used to include special characters in a string, such as newline ('\n'), tab ('\t'), and more. For example:

# In[ ]:


print("Hello\nWorld")  # Output: Hello
                         #        World


# In this example, the '\n' character is used to include a newline in the string.
# 
# To include Unicode characters in a string: The '' character can be used to include Unicode characters in a string. For example:

# In[ ]:


print("\u2665")  # Output: 


# In this example, the '\u2665' character is used to include a Unicode heart symbol in the string.
# 
# Overall, the '' character is an important part of Python's syntax, and it allows you to include special characters in strings.

# Q.7. Give an example of the following conditions:
# (i) Homogeneous list
# (ii) Heterogeneous set
# (iii) Homogeneous tuple
# A7- (i) Homogeneous list
# 
# A homogeneous list is a list that contains elements of the same data type. Here's an example

# In[ ]:


fruits = ['apple', 'banana', 'orange', 'grape']


# In this example, the list fruits contains only strings, making it a homogeneous list.
# 
# (ii) Heterogeneous set
# 
# A heterogeneous set is a set that contains elements of different data types. Here's an example:

# In[ ]:


mixed_set = {1, 'hello', 3.14, True, [1, 2, 3]}


# In this example, the set mixed_set contains elements of different data types: integer, string, float, boolean, and list. This makes it a heterogeneous set.
# 
# (iii) Homogeneous tuple
# 
# A homogeneous tuple is a tuple that contains elements of the same data type. Here's an example:

# In[ ]:


numbers = (1, 2, 3, 4, 5)


# In this example, the tuple numbers contains only integers, making it a homogeneous tuple.
# 
# Note that in Python, sets are unordered collections of unique elements, while lists and tuples are ordered collections of elements.

# Q.8. Explain the mutable and immutable data types with proper explanation & examples.
# A8-  In Python, data types can be classified into two categories: mutable and immutable.
# 
# Mutable Data Types
# 
# Mutable data types are those that can be modified or changed after they are created. In other words, their values can be altered or updated.
# 
# Here are some examples of mutable data types in Python:
# 
# Lists: Lists are a collection of items that can be modified after they are created.

# In[ ]:


my_list = [1, 2, 3, 4, 5]
my_list.append(6)  # adds 6 to the end of the list
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]


# In[ ]:


Dictionaries: Dictionaries are a collection of key-value pairs that can be modified after they are created.


# In[ ]:


my_dict = {'name': 'John', 'age': 30}
my_dict['city'] = 'New York'  # adds a new key-value pair
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}


# In[ ]:


Sets: Sets are an unordered collection of unique elements that can be modified after they are created.


# In[ ]:


my_set = {1, 2, 3, 4, 5}
my_set.add(6)  # adds 6 to the set
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}


# In[ ]:


User-defined objects: User-defined objects, such as instances of classes, can also be mutable.


# Immutable Data Types
# 
# Immutable data types are those that cannot be modified or changed after they are created. In other words, their values cannot be altered or updated.
# 
# Here are some examples of immutable data types in Python:
# 
# Integers: Integers are whole numbers that cannot be modified after they are created.

# In[ ]:


x = 5
x = x + 1  # creates a new integer object, does not modify the original
print(x)  # Output: 6


# In[ ]:


Floats: Floats are decimal numbers that cannot be modified after they are created.


# In[ ]:


x = 3.14
x = x + 1.0  # creates a new float object, does not modify the original
print(x)  # Output: 4.14


# In[ ]:


Strings: Strings are sequences of characters that cannot be modified after they are created.


# In[ ]:


my_string = "hello"
my_string += " world"  # creates a new string object, does not modify the original
print(my_string)  # Output: "hello world"


# In[ ]:


Tuples: Tuples are ordered collections of elements that cannot be modified after they are created.


# In[ ]:


my_tuple = (1, 2, 3, 4, 5)
# my_tuple[0] = 10  # this would raise a TypeError
print(my_tuple)  # Output: (1, 2, 3, 4, 5)


# Note that while immutable objects cannot be modified, they can be reassigned to a new value. For example, x = 5 and then x = 6 reassigns the variable x to a new integer object, but it does not modify the original integer object.
# 
# I hope this helps

# Q.9. Write a code to create the given structure using only for loop.
# *
# ***
# *****
# *******
# *********
# A9- Here's an example code to create the given structure using only a for loop:

# In[ ]:


for i in range(1, 7):
    print('*' * (2*i - 1))


# Output:

# *
# ***
# *****
# *******
# *********
# Explanation:
# 
# We use a for loop to iterate over the range of values from 1 to 6 (inclusive).
# For each iteration, we calculate the number of asterisks to print using the formula (2*i - 1), where i is the current iteration number.
# We print the calculated number of asterisks using the print() function.
# The print() function automatically adds a newline character at the end of the output, so we don't need to add it explicitly.
# The resulting output is the desired structure of asterisks.

# Q.10. Write a code to create the given structure using while loop.
# |||||||||
# |||||||
# |||||
# |||
# |
# A10- Here's an example code to create the given structure using a while loop:

# In[ ]:


i = 7
while i > 0:
    print('|' * i)
    i -= 1


# In[ ]:


Output:


# In[ ]:


|||||||||
|||||||
|||||
|||
|
Explanation:

*We initialize a variable i to 7, which represents the number of pipes (|) to print in the first line.
*We use a while loop to iterate until i becomes 0.
*Inside the loop, we print the pipes using the print() function, with the number of pipes determined by the current value of i.
*We decrement i by 1 at the end of each iteration, so that the number of pipes decreases by 1 in each subsequent line.
*The loop continues until i becomes 0, at which point the loop exits and the program terminates.
*The resulting output is the desired structure of pipes.

