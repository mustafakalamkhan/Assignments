#!/usr/bin/env python
# coding: utf-8

# Q1- What is a lambda function in Python, and how does it differ from a regular function?
# A1- In Python, a lambda function is a small, anonymous function that can be defined inline within a larger expression. It is a shorthand way to create a function without declaring a separate named function.
# 
# A lambda function is defined using the lambda keyword, followed by an input parameter list, and an expression that is evaluated and returned. The syntax is:

# In[ ]:


lambda arguments: expression


# Here's an example:

# In[ ]:


double = lambda x: x * 2
print(double(5))  # Output: 10


# In this example, the lambda function takes a single argument x and returns its double value.
# 
# Now, let's compare lambda functions with regular functions:
# 
# Differences:
# Syntax: Lambda functions use the lambda keyword, while regular functions use the def keyword.
# Anonymous: Lambda functions are anonymous, meaning they don't have a name, whereas regular functions have a name.
# Inline definition: Lambda functions are defined inline, within a larger expression, whereas regular functions are defined separately.
# Single expression: Lambda functions can only contain a single expression, whereas regular functions can have multiple statements.
# Return value: Lambda functions implicitly return the result of the expression, whereas regular functions require an explicit return statement.
# Similarities:
# 
# Functionality: Both lambda functions and regular functions can take arguments and return values.
# Scope: Both types of functions have their own scope, which means they can access variables from the surrounding scope.
# Use cases:
# 
# Lambda functions are useful when:
# 
# You need a quick, one-time function for a specific task.
# You want to pass a function as an argument to another function (e.g., map(), filter(), reduce()).
# You need to create a function on the fly, without polluting the namespace with a named function.
# In summary, lambda functions are concise, anonymous functions that are useful for quick, one-time tasks, while regular functions are more versatile and suitable for reusable, complex logic.

# Q2- Can a lambda function in Python have multiple arguments? If yes, how can you define and use
# them?
# A2-Yes, a lambda function in Python can have multiple arguments. You can define a lambda function with multiple arguments by separating them with commas in the input parameter list.
# 
# Here's the syntax:

# In[ ]:


lambda arg1, arg2,..., argN: expression


# Where arg1, arg2,..., argN are the input arguments, and expression is the code that will be executed when the lambda function is called.
# 
# Let's see an example

# In[ ]:


add_numbers = lambda x, y, z: x + y + z
result = add_numbers(2, 3, 4)
print(result)  # Output: 9


# In this example, the lambda function add_numbers takes three arguments x, y, and z, and returns their sum.
# 
# You can also use default values for arguments in a lambda function, just like in regular functions:

# In[ ]:


greet = lambda name, greeting='Hello': f"{greeting}, {name}!"
print(greet("John"))  # Output: Hello, John!
print(greet("Jane", "Hi"))  # Output: Hi, Jane!


# Here, the lambda function greet takes two arguments name and greeting, with a default value of "Hello" for greeting.
# 
# When calling a lambda function with multiple arguments, you need to pass the arguments in the correct order, just like with regular functions.
# 
# Note that, just like with regular functions, you can also use keyword arguments when calling a lambda function:

# In[ ]:


greet = lambda name, greeting: f"{greeting}, {name}!"
print(greet(name="John", greeting="Hi"))  # Output: Hi, John!


# In summary, lambda functions in Python can have multiple arguments, and you can define and use them just like regular functions, with the added convenience of being able to define them inline.

# Lambda functions are typically used in Python in situations where a small, one-time-use function is needed. They are often used as:
# 
# Event handlers: Lambda functions can be used as event handlers, such as button clicks or mouse movements.
# Data processing: Lambda functions can be used to perform simple data processing tasks, such as filtering, mapping, or reducing data.
# Higher-order functions: Lambda functions can be passed as arguments to higher-order functions, such as filter(), map(), or reduce().
# Sorting and ordering: Lambda functions can be used as key functions for sorting or ordering data.
# Here's an example use case:
# 
# Example: Sorting a list of dictionaries by a specific key
# 
# Suppose we have a list of dictionaries, and we want to sort them by the value of a specific key, say, "age".

# In[ ]:


people = [
    {"name": "John", "age": 25},
    {"name": "Jane", "age": 30},
    {"name": "Bob", "age": 20},
    {"name": "Alice", "age": 28}
]

# Use a lambda function as the key function for sorting
sorted_people = sorted(people, key=lambda x: x["age"])

print(sorted_people)


# Output:

# In[ ]:


[
    {"name": "Bob", "age": 20},
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 28},
    {"name": "Jane", "age": 30}
]


# In this example, the lambda function lambda x: x["age"] is used as the key function for sorting the list of dictionaries. The lambda function takes a dictionary x as input and returns the value of the "age" key. The sorted() function uses this lambda function to sort the list of dictionaries by the "age" key.
# 
# This is just one example of how lambda functions can be used in Python. They are a powerful tool that can simplify code and make it more concise and expressive

# Q4- What are the advantages and limitations of lambda functions compared to regular functions in
# Python?
# A4- Advantages of Lambda Functions:
# 
# Concise Code: Lambda functions allow you to define small, one-time-use functions in a concise and expressive way, making your code more readable and compact.
# Anonymous Functions: Lambda functions are anonymous, meaning they don't have a declared name, which can be useful when you need a quick, one-time-use function.
# Inline Definition: Lambda functions can be defined inline, within a larger expression, making your code more concise and easier to read.
# Higher-Order Functions: Lambda functions can be passed as arguments to higher-order functions, such as filter(), map(), or reduce(), making them a powerful tool for data processing.
# Flexibility: Lambda functions can be used as event handlers, data processing functions, or as key functions for sorting or ordering data.
# Limitations of Lambda Functions:
# Limited Readability: While lambda functions can make your code more concise, they can also make it less readable if overused or used for complex logic.
# Limited Debugging: Since lambda functions are anonymous, they can be difficult to debug, as they don't have a declared name or a clear call stack.
# Limited Reusability: Lambda functions are designed for one-time use, so they can't be reused like regular functions.
# Limited Complexity: Lambda functions are best suited for simple, one-line logic. Complex logic or multi-line code can be difficult to express using lambda functions.
# No Docstrings: Lambda functions can't have docstrings, which can make it harder for others (and yourself) to understand the purpose and behavior of the function.
# Comparison to Regular Functions:
# 
# Regular Functions:
# 
# More readable and maintainable code
# Easier debugging and testing
# Can be reused and imported from other modules
# Can have docstrings and type hints
# Suitable for complex logic and multi-line code
# Lambda Functions:
# 
# More concise and expressive code
# Anonymous and inline definition
# Suitable for simple, one-time-use logic
# Can be passed as arguments to higher-order functions
# In general, use lambda functions when you need a quick, one-time-use function for simple logic, and use regular functions when you need more complex logic, reusability, or better readability and maintainability.

# Q5- Are lambda functions in Python able to access variables defined outside of their own scope?
# Explain with an example.
# A5- Yes, lambda functions in Python can access variables defined outside of their own scope.
# 
# This is known as a closure, where a lambda function "remembers" the variables from its surrounding scope, even when it's called outside of that scope.
# 
# Here's an example:

# In[ ]:


x = 10  # global variable

def outer():
    y = 20  # local variable in outer scope

    # lambda function that accesses x and y
    lambda_func = lambda: x + y
    return lambda_func

# Create a lambda function by calling outer()
my_lambda = outer()

# Call the lambda function
result = my_lambda()
print(result)  # Output: 30


# In this example:
# 
# We define a global variable x with value 10.
# We define a function outer() that has a local variable y with value 20.
# Inside outer(), we define a lambda function lambda_func that accesses both x and y.
# We return the lambda function from outer().
# We call outer() to create a lambda function and assign it to my_lambda.
# We call my_lambda() to execute the lambda function, which accesses x and y from its surrounding scope.
# The lambda function has access to x and y because it's defined within the scope of outer(), which has access to both variables. Even though my_lambda is called outside of outer(), it still remembers the values of x and y from its surrounding scope.
# 
# This is a powerful feature of lambda functions in Python, allowing them to capture and use variables from their surrounding scope.

# Q6- Write a lambda function to calculate the square of a given number.
# A6- Here is a lambda function to calculate the square of a given number:

# In[ ]:


square = lambda x: x ** 2


# This lambda function takes a single argument x and returns its square, calculated using the exponentiation operator **.
# 
# You can use this lambda function like this:

# In[ ]:


print(square(5))  # Output: 25
print(square(3))  # Output: 9
print(square(10))  # Output: 100


# This lambda function is equivalent to a regular function defined like this:

# In[ ]:


def square(x):
    return x ** 2


# But the lambda function is more concise and can be defined inline, making it a great choice for simple, one-time-use functions.

# Q7- Create a lambda function to find the maximum value in a list of integers.
# A7- Here is a lambda function to find the maximum value in a list of integers:

# In[ ]:


max_value = lambda x: max(x)


# This lambda function takes a list x as input and returns the maximum value in the list using the built-in max() function.
# 
# You can use this lambda function like this:

# In[ ]:


numbers = [3, 1, 4, 1, 5, 9]
print(max_value(numbers))  # Output: 9


# Alternatively, you can also use the max() function directly without defining a lambda function:

# In[ ]:


numbers = [3, 1, 4, 1, 5, 9]
print(max(numbers))  # Output: 9


# Both approaches will give you the same result, which is the maximum value in the list.

# Q8- Implement a lambda function to filter out all the even numbers from a list of integers.
# A8- Here is a lambda function to filter out all the even numbers from a list of integers:

# In[ ]:


filter_even = lambda x: list(filter(lambda y: y % 2 != 0, x))


# This lambda function takes a list x as input and returns a new list containing only the odd numbers from the original list.
# 
# Here's how it works:
# 
# The filter() function is used to create an iterator that filters out the even numbers.
# The lambda function lambda y: y % 2 != 0 is used as the filtering criterion. It takes an integer y as input and returns True if y is odd (i.e., y % 2 != 0) and False otherwise.
# The list() function is used to convert the iterator returned by filter() into a list.
# You can use this lambda function like this:

# In[ ]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = filter_even(numbers)
print(odd_numbers)  # Output: [1, 3, 5, 7, 9]


# In[ ]:


Alternatively, you can also use a list comprehension to achieve the same result:


# In[ ]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = [x for x in numbers if x % 2 != 0]
print(odd_numbers)  # Output: [1, 3, 5, 7, 9]


# Both approaches will give you the same result, which is a list containing only the odd numbers from the original list.

# Q9- Write a lambda function to sort a list of strings in ascending order based on the length of each
# string.
# A9- Here is a lambda function to sort a list of strings in ascending order based on the length of each string

# In[ ]:


sort_by_length = lambda x: sorted(x, key=lambda y: len(y))


# This lambda function takes a list x of strings as input and returns a new list with the strings sorted in ascending order based on their length.
# 
# Here's how it works:
# 
# The sorted() function is used to sort the list of strings.
# The key argument of the sorted() function is set to a lambda function lambda y: len(y), which takes a string y as input and returns its length.
# The sorted() function uses this lambda function as the sorting criterion, sorting the strings based on their length in ascending order.
# You can use this lambda function like this:

# In[ ]:


strings = ["hello", "a", "world", "abc", "def", "ghi"]
sorted_strings = sort_by_length(strings)
print(sorted_strings)  # Output: ["a", "abc", "def", "ghi", "hello", "world"]


# Alternatively, you can also use the sorted() function directly without defining a lambda function:

# Q10- Create a lambda function that takes two lists as input and returns a new list containing the
# common elements between the two lists.
# A10- Here is a lambda function that takes two lists as input and returns a new list containing the common elements between the two lists:

# In[ ]:


common_elements = lambda x, y: list(set(x) & set(y))


# This lambda function takes two lists x and y as input and returns a new list containing the common elements between the two lists.
# Here's how it works:
# 
# The set() function is used to convert each list to a set, which is an unordered collection of unique elements.
# The & operator is used to compute the intersection of the two sets, which returns a new set containing only the elements that are common to both sets.
# The list() function is used to convert the resulting set back to a list.
# You can use this lambda function like this:

# In[ ]:


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = common_elements(list1, list2)
print(common)  # Output: [4, 5]


# In[ ]:


Alternatively, you can also use a list comprehension to achieve the same result:


# In[ ]:


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = [x for x in list1 if x in list2]
print(common)  # Output: [4, 5]


# Both approaches will give you the same result, which is a list containing the common elements between the two input lists.

# In[ ]:


Q11- Write a recursive function to calculate the factorial of a given positive integer.
A11-  Here is a recursive function to calculate the factorial of a given positive integer:


# In[ ]:


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


# This function takes a positive integer n as input and returns its factorial.
# 
# Here's how it works:
# 
# The base case is when n is 0 or 1, in which case the factorial is defined to be 1.
# For n greater than 1, the function calls itself with n-1 as input, and multiplies the result by n. This is the recursive step.
# The function continues to call itself until it reaches the base case, at which point it returns the final result.
# You can use this function like this:

# In[ ]:


print(factorial(5))  # Output: 120
print(factorial(3))  # Output: 6
print(factorial(1))  # Output: 1


# Note that this function will raise a RecursionError if you try to calculate the factorial of a very large number, since Python has a limit on the maximum recursion depth. For large numbers, it's better to use an iterative approach or a more efficient algorithm.
# 
# Also, it's worth noting that this function does not handle negative integers or non-integer inputs. If you want to add error handling for those cases, you can modify the function accordingly.

# In[ ]:


Q12- Implement a recursive function to compute the nth Fibonacci number.
A12- Here is a recursive function to compute the nth Fibonacci number:


# In[ ]:


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# This function takes an integer n as input and returns the n-th Fibonacci number.
# 
# Here's how it works:
# 
# The base cases are when n is 0 or 1, in which case the Fibonacci number is defined to be 0 and 1, respectively.
# For n greater than 1, the function calls itself with n-1 and n-2 as input, and returns the sum of the two results. This is the recursive step.
# The function continues to call itself until it reaches the base case, at which point it returns the final result.
# You can use this function like this:

# In[ ]:


print(fibonacci(5))  # Output: 5
print(fibonacci(8))  # Output: 21
print(fibonacci(13))  # Output: 233


# Note that this function has an exponential time complexity, which means it can be very slow for large values of n. This is because it performs a lot of repeated computations. For example, to compute fibonacci(5), it needs to compute fibonacci(4) and fibonacci(3), and to compute fibonacci(4), it needs to compute fibonacci(3) and fibonacci(2), and so on.
# 
# A more efficient approach would be to use an iterative algorithm or a memoized recursive function, which can compute the n-th Fibonacci number in linear time.

# In[ ]:


Q13- Create a recursive function to find the sum of all the elements in a given list.
A13- Here is a recursive function to find the sum of all the elements in a given list:


# In[2]:


def recursive_sum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])


# This function takes a list lst as input and returns the sum of all its elements.
# 
# Here's how it works:
# 
# The base case is when the list is empty, in which case the sum is defined to be 0.
# For a non-empty list, the function returns the sum of the first element lst[0] and the sum of the rest of the list lst[1:]. This is the recursive step.
# The function continues to call itself until it reaches the base case, at which point it returns the final result.
# You can use this function like this:
# 
# python

# In[ ]:


numbers = [1, 2, 3, 4, 5]
print(recursive_sum(numbers))  # Output: 15

letters = ['a', 'b', 'c']
print(recursive_sum(letters))  # Error: cannot sum strings

mixed = [1, 'a', 2, 'b', 3]
print(recursive_sum(mixed))  # Error: cannot sum mixed types


# Note that this function only works for lists of numbers. If you try to use it with a list of strings or mixed types, it will raise a TypeError.
# 
# Also, keep in mind that this function has a recursive depth equal to the length of the list, which means it can cause a RecursionError for very long lists. In practice, it's often better to use an iterative approach or a built-in function like sum() to compute the sum of a list.

# In[ ]:


Q14- Write a recursive function to determine whether a given string is a palindrome.
A14- Here is a recursive function to determine whether a given string is a palindrome:


# In[ ]:


def is_palindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False


# This function takes a string s as input and returns True if it is a palindrome, and False otherwise.
# 
# Here's how it works:
# 
# The base case is when the string has length 0 or 1, in which case it is trivially a palindrome.
# For a longer string, the function checks whether the first and last characters are the same. If they are, it recursively calls itself on the substring s[1:-1], which removes the first and last characters.
# If the first and last characters are not the same, the function returns False, indicating that the string is not a palindrome.
# The function continues to call itself until it reaches the base case, at which point it returns the final result.
# You can use this function like this:

# In[ ]:


print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("abcba"))  # Output: True


# Note that this function is case-sensitive and considers spaces and punctuation as part of the string. If you want to ignore case, spaces, and punctuation, you can modify the function to preprocess the input string accordingly.
# 
# Also, keep in mind that this function has a recursive depth equal to the length of the string, which means it can cause a RecursionError for very long strings. In practice, it's often better to use an iterative approach or a built-in function like s == s[::-1] to check whether a string is a palindrome.

# In[ ]:


Q15- Implement a recursive function to find the greatest common divisor (GCD) of two positive integers.
A15- Here is a recursive function to find the greatest common divisor (GCD) of two positive integers:


# In[ ]:


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# This function takes two positive integers a and b as input and returns their greatest common divisor.
# 
# Here's how it works:
# 
# The base case is when b is 0, in which case the GCD is simply a.
# For non-zero b, the function recursively calls itself with b as the new a and a % b as the new b. This is based on the Euclidean algorithm, which states that the GCD of a and b is the same as the GCD of b and the remainder of a divided by b.
# The function continues to call itself until it reaches the base case, at which point it returns the final result.
# You can use this function like this: 

# In[ ]:


print(gcd(12, 15))  # Output: 3
print(gcd(24, 30))  # Output: 6
print(gcd(48, 60))  # Output: 12
print(gcd(100, 75))  # Output: 25


# Note that this function only works for positive integers. If you want to extend it to work with negative integers or zero, you'll need to add some additional logic.
# 
# Also, keep in mind that this function has a recursive depth equal to the number of iterations required to reach the base case, which can be large for large inputs. In practice, it's often better to use an iterative approach or a built-in function like math.gcd() to compute the GCD.
# 
# Here's an example of an iterative approach:

# In[3]:


def gcd_iterative(a, b):
    while b!= 0:
        a, b = b, a % b
    return a


# This function uses a simple loop to iterate until b is 0, at which point it returns the final result. This approach is often more efficient and easier to understand than the recursive approach.
