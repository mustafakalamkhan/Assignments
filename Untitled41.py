#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q.1. Create two int type variables, apply addition, subtraction, division and multiplications
and store the results in variables. Then print the data in the following format by calling the
variables:
First variable is __ & second variable is __.
Addition: __ + __ = __
Subtraction: __ - __ = __
Multiplication: __ * __ = __
Division: __ / __ = __
A.1- Here is an example code that demonstrates the operations you requested:


# In[ ]:


# Create two int type variables
var1 = 10
var2 = 5

# Apply operations and store results in variables
add_result = var1 + var2
sub_result = var1 - var2
mul_result = var1 * var2
div_result = var1 / var2

# Print the results
print(f"First variable is {var1} & second variable is {var2}.")
print(f"Addition: {var1} + {var2} = {add_result}")
print(f"Subtraction: {var1} - {var2} = {sub_result}")
print(f"Multiplication: {var1} * {var2} = {mul_result}")
print(f"Division: {var1} / {var2} = {div_result}")


# In[ ]:


Output:


# In[ ]:


First variable is 10 & second variable is 5.
Addition: 10 + 5 = 15
Subtraction: 10 - 5 = 5
Multiplication: 10 * 5 = 50
Division: 10 / 5 = 2.0


# Q.2. What is the difference between the following operators:
# (i) ‘/’ & ‘//’
# (ii) ‘**’ & ‘^’
# A.2- Here are the differences between the operators:
# 
# (i) '/' and '//'
# 
# / is the division operator, which performs floating-point division. It returns a floating-point result, even if the operands are integers.
# // is the integer division operator, also known as floor division. It returns an integer result, discarding any fractional part.
# for example

# In[ ]:


a = 10
b = 3

print(a / b)  # Output: 3.3333333333333335
print(a // b)  # Output: 3


# In the first example, a / b returns a floating-point result, while in the second example, a // b returns an integer result, discarding the fractional part.
# 
# (ii) '' and '^'**
# 
# ** is the exponentiation operator, which raises the left operand to the power of the right operand.
# ^ is the bitwise XOR operator, which performs a binary operation on the bits of the operands.
# for example-

# In[ ]:


a = 2
b = 3

print(a ** b)  # Output: 8 (2 to the power of 3)
print(a ^ b)  # Output: 1 (binary XOR of 2 and 3)


# In the first example, a ** b raises 2 to the power of 3, resulting in 8. In the second example, a ^ b performs a bitwise XOR operation on the binary representations of 2 and 3, resulting in 1.
# 
# Note that in some programming languages, ^ is used for exponentiation, but in Python, ** is the standard exponentiation operator, and ^ is reserved for bitwise XOR.

# Q.3. List the logical operators.
# A.3- Here are the logical operators in programming:
# 
# 1. AND (Logical Conjunction) Represents true if both operands are true.
# 
# Symbol: && (in most programming languages)
# Example: a > 5 && b < 10
# 2. OR (Logical Disjunction) Represents true if at least one operand is true.
# 
# Symbol: || (in most programming languages)
# Example: a > 5 || b < 10
# 3. NOT (Logical Negation) Represents the opposite of the operand.
# 
# Symbol: ! (in most programming languages)
# Example: !(a > 5)
# Here's a summary in a Python code snippet

# In[ ]:


a = 6
b = 8

# AND (Logical Conjunction)
print(a > 5 and b < 10)  # Output: True

# OR (Logical Disjunction)
print(a > 5 or b < 5)  # Output: True

# NOT (Logical Negation)
print(not a > 5)  # Output: False


# Q.4. Explain right shift operator and left shift operator with examples.
# A.4- Bitwise Shift Operators:
# 
# In programming, bitwise shift operators are used to manipulate the bits of a binary number. There are two types of shift operators: Left Shift (<<) and Right Shift (>>).
# 
# Left Shift Operator (<<):
# 
# The left shift operator shifts the bits of a binary number to the left by a specified number of positions. This is equivalent to multiplying the number by 2 raised to the power of the number of positions shifted.
# Example:
# 
# a = 10 (binary: 1010)
# 
# a << 1 (shift left by 1 position)
# 
# Result: 20 (binary: 10100)
# 
# In this example, the bits of 10 are shifted one position to the left, effectively multiplying the number by 2.
# Left Shift Operator Rules:
# 
# Shifting left by n positions is equivalent to multiplying by 2^n.
# Filling the vacated bits on the right with zeros.
# Right Shift Operator (>>):
# 
# The right shift operator shifts the bits of a binary number to the right by a specified number of positions. This is equivalent to dividing the number by 2 raised to the power of the number of positions shifted.
# Example:
# 
# a = 20 (binary: 10100)
# 
# a >> 1 (shift right by 1 position)
# 
# Result: 10 (binary: 1010)
# 
# In this example, the bits of 20 are shifted one position to the right, effectively dividing the number by 2.
# Right Shift Operator Rules:
# 
# Shifting right by n positions is equivalent to dividing by 2^n.
# Filling the vacated bits on the left with zeros (for unsigned numbers) or with the sign bit (for signed numbers).
# Important Notes:
# 
# When shifting left, the most significant bit (MSB) is lost, and a new zero is added to the least significant bit (LSB).
# When shifting right, the LSB is lost, and a new bit is added to the MSB, which is a copy of the original MSB (for signed numbers) or a zero (for unsigned numbers).
# Here's an example in Python:

# In[ ]:


a = 10  # binary: 1010
print(a << 1)  # Output: 20 (binary: 10100)

b = 20  # binary: 10100
print(b >> 1)  # Output: 10 (binary: 1010)


# Q.5. Create a list containing int type data of length 15. Then write a code to check if 10 is
# present in the list or not.
# A.5- Here's an example:

# In[ ]:


# Create a list of 15 integers
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Check if 10 is present in the list
if 10 in my_list:
    print("10 is present in the list!")
else:
    print("10 is not present in the list.")


# Output:

# In[ ]:


10 is present in the list!


# In this example, we create a list my_list with 15 integers. Then, we use the in operator to check if the value 10 is present in the list. If it is, we print a success message; otherwise, we print a failure message.
# 
# Here's a breakdown of the code:
# 
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]: Creates a list of 15 integers.
# if 10 in my_list:: Checks if the value 10 is present in the list using the in operator.
# print("10 is present in the list!"): Prints a success message if 10 is found in the list.
# else: print("10 is not present in the list."): Prints a failure message if 10 is not found in the list.
# Note that the in operator is a membership test operator that returns True if the value
# is found in the list and False otherwise.
