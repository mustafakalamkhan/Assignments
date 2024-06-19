#!/usr/bin/env python
# coding: utf-8

# Q1- What does an empty dictionary's code look like?
# A1- An empty dictionary in Python can be represented using curly braces {} or by calling the dict() constructor with no     arguments. Here are some examples:

# In[ ]:


# Example 1: Empty dictionary using curly braces
empty_dict1 = {}

# Example 2: Empty dictionary using dict() constructor
empty_dict2 = dict()

# Both examples create an empty dictionary
print(type(empty_dict1))  # Output: <class 'dict'>
print(type(empty_dict2))  # Output: <class 'dict'>


# Both examples create an empty dictionary, which you can later populate with key-value pairs as needed.
# 
# Keep in mind that an empty dictionary is not the same as a dictionary with no keys or values. An empty dictionary has no key-value pairs, but it still exists as a dictionary object with its own methods and attributes.

# Q2- What is the value of a dictionary value with the key & 'foo' and the value 42?
# A2- The value associated with the key 'foo'.
# Here's the dictionary:

# In[ ]:


d = {&: 42}  # Note: & is not a valid key in Python, I'll assume you meant a string "&"


# However, since & is not a valid key in Python (it's a bitwise AND operator), I'll assume you meant to use a string "&" as the key.
# 
# In this case, the dictionary d has only one key-value pair: {"&": 42}.
# 
# Now, when you ask about the value associated with the key 'foo', the answer is: there is no such key. The dictionary d only has the key "&", not 'foo'.
# 
# If you try to access the value associated with the key 'foo', you'll get a KeyError:

# In[ ]:


print(d['foo'])  # Raises KeyError: 'foo'


# To avoid this error, you can use the get() method, which returns None if the key is not present in the dictionary:

# In[ ]:


print(d.get('foo'))  # Output: None


# Q3- What is the most significant distinction between a dictionary and a list?
# A3- The most significant distinction between a dictionary and a list in Python is how they store and access their elements.
#     List:
# 
# A list is an ordered collection of elements, which means that the order of the elements matters.
# Each element in a list is identified by an index, which is an integer that starts from 0.
# You access elements in a list using their index, like my_list[0] to get the first element.
# Lists are useful when you need to maintain a specific order or iterate over a sequence of elements.
#     Dictionary:
# 
# A dictionary is an unordered collection of key-value pairs, which means that the order of the elements doesn't matter.
# Each element in a dictionary is identified by a unique key, which can be any immutable type (like strings, integers, or tuples).
# You access elements in a dictionary using their key, like my_dict['name'] to get the value associated with the key 'name'.
# Dictionaries are useful when you need to store and look up data using a specific identifier or label.
# 
# In summary, the main distinction between a dictionary and a list is that a list uses indices to access elements, while a dictionary uses keys to access values. This fundamental difference in how they store and access data makes them suitable for different use cases in programming.

# Q4- What happens if you try to access spam['foo&'] if spam is {'bar': 100}?
# A4- If you try to access spam['foo&'] when spam is {'bar': 100}, you'll get a KeyError.
# 
# Here's what happens:

# In[ ]:


spam = {'bar': 100}
print(spam['foo&'])  # Raises KeyError: 'foo&'


# The error message will be KeyError: 'foo&', indicating that the key 'foo&' is not present in the dictionary spam.
# 
# This is because the dictionary spam only has one key-value pair: {'bar': 100}, and 'foo&' is not one of its keys. When you try to access a key that doesn't exist in the dictionary, Python raises a KeyError.
# 
# To avoid this error, you can use the get() method, which returns None if the key is not present in the dictionary:

# In[ ]:


print(spam.get('foo&'))  # Output: None


# Alternatively, you can use the in operator to check if the key exists in the dictionary before trying to access it:

# In[ ]:


if 'foo&' in spam:
    print(spam['foo&'])
else:
    print("Key 'foo&' not found in spam")


# Q5- If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
# A5- If a dictionary is stored in spam, the expressions 'cat' in spam and 'cat' in spam.keys() are similar, but not exactly the same.
# 
# 'cat' in spam:
# 
# This expression checks if the key 'cat' exists in the dictionary spam. It returns True if the key is present, and False otherwise.
# 
# In other words, it checks if 'cat' is a key in the dictionary, regardless of its associated value.
# 
# 'cat' in spam.keys():
# 
# This expression is similar, but it explicitly checks if the key 'cat' is present in the keys() view of the dictionary spam.
# 
# The keys() method returns a view object that displays a list of all the keys available in the dictionary. So, 'cat' in spam.keys() checks if the key 'cat' is present in this list of keys.
# 
# In practice, both expressions will give you the same result: True if the key 'cat' is in the dictionary, and False otherwise.
# 
# However, there is a subtle difference:
# 
# 'cat' in spam is more efficient and Pythonic, as it directly checks the dictionary's keys without creating an intermediate list of keys.
# 'cat' in spam.keys() creates a keys() view object, which can be slower and more memory-intensive for large dictionaries.
# So, in general, it's recommended to use the simpler and more efficient 'cat' in spam expression to check if a key is present in a dictionary.

# Q6- If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and'cat' in spam.values()?
# A6- If a dictionary is stored in spam, the expressions 'cat' in spam and 'cat' in spam.values() are quite different.
# 
# 'cat' in spam:
# 
# As I mentioned earlier, this expression checks if the key 'cat' exists in the dictionary spam. It returns True if the key is present, and False otherwise.
# 
# 'cat' in spam.values():
# This expression checks if the value 'cat' is present in the dictionary spam. It returns True if the value is associated with any key in the dictionary, and False otherwise.
# 
# In other words, 'cat' in spam.values() checks if 'cat' is a value in the dictionary, not a key.
# 
# Here's an example to illustrate the difference:

# In[ ]:


spam = {'dog': 'cat', 'bird': 'mouse'}

print('cat' in spam)  # False, because 'cat' is not a key
print('cat' in spam.values())  # True, because 'cat' is a value


# As you can see, 'cat' in spam returns False because 'cat' is not a key in the dictionary. However, 'cat' in spam.values() returns True because 'cat' is a value associated with the key 'dog'.
# 
# So, to summarize:
# 'cat' in spam checks if 'cat' is a key in the dictionary.
# 'cat' in spam.values() checks if 'cat' is a value in the dictionary.
# Use the first expression to check for keys, and the second expression to check for values!

# Q7- What is a shortcut for the following code?
#     if 'color' not in spam:
#         spam['color'] = 'black'
# A7- The shortcut for the following code:        

# In[ ]:


if 'color' not in spam:
    spam['color'] = 'black'


# is:

# In[ ]:


spam.setdefault('color', 'black')


# The setdefault() method returns the value of the item with the specified key. If the key does not exist, it inserts the key with the specified value, and then returns the value.
# 
# In this case, spam.setdefault('color', 'black') returns the value of the 'color' key if it exists, or sets the key to 'black' and returns 'black' if the key does not exist.
# 
# This is a more concise way to write the original code, and it can be useful when you want to ensure that a dictionary has a certain key with a default value, without having to check if the key exists first.

# Q8- How do you "pretty print" dictionary values using which module and function?
# A8- You can "pretty print" dictionary values using the pprint module and the pprint() function.
# 
# Here's an example:

# In[ ]:


import pprint

spam = {'name': 'John', 'age': 30, 'address': {'street': '123 Main St', 'city': 'Anytown', 'tate': 'CA'}}

pprint.pprint(spam)


# This will output:

# In[ ]:


{'address': {'city': 'Anytown', 'tate': 'CA', 'treet': '123 Main St'},
 'age': 30,
 'name': 'John'}


# The pprint() function formats the dictionary in a more readable way, with indentation and line breaks, making it easier to visualize the structure of the dictionary.
# 
# You can also use the pformat() function from the pprint module to format the dictionary as a string, which can be useful for logging or displaying the dictionary in a GUI application.
# 
# For example:

# In[ ]:


formatted_spam = pprint.pformat(spam)
print(formatted_spam)


# This will output the same formatted string as above.
# 
# The pprint module is part of the Python Standard Library, so you don't need to install anything extra to use it!
