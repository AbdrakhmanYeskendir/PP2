'''
    Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
    
'''

#You can get the data type of any object by using the type() function:
#Print the data type of the variable x:
x = 5
print(type(x)) 


#EXAMPLE 1 STR
x = "Hello World"
x = str("Hello World")
#display x:
print(x)
#display the data type of x:
print(type(x)) 


#EXAMPLE 2 INT
x = 20
x = int(20)
#display x:
print(x)
#display the data type of x:
print(type(x)) 


#EXAMPLE 3 FLOAT
x = 20.5
x = float(20.5)
#display x:
print(x)
#display the data type of x:
print(type(x)) 


#EXAMPLE 4 COMPLEX
x = 1j
x = complex(1j)
#display x:
print(x)
#display the data type of x:
print(type(x)) 


#EXAMPLE 5 LIST
x = ["apple", "banana", "cherry"]
x = list(("apple", "banana", "cherry"))
#display x:
print(x)
#display the data type of x:
print(type(x)) 


#EXAMPLE 6 TUPLE
x = ("apple", "banana", "cherry")
x = tuple(("apple", "banana", "cherry"))
#display x:
print(x)
#display the data type of x:
print(type(x)) 


#EXAMPLE 7 RANGE
x = range(6)
#display x:
print(x)
#display the data type of x:
print(type(x)) 


#EXAMPLE 8 DICT
x = {"name" : "John", "age" : 36}
x = dict(name="John", age=36)
#display x:
print(x)
#display the data type of x:
print(type(x)) 


#EXAMPLE 9 SET
x = {"apple", "banana", "cherry"}
x = set(("apple", "banana", "cherry"))
#display x:
print(x)
#display the data type of x:
print(type(x)) 


#EXAMPLE 10 FROZENSET
x = frozenset({"apple", "banana", "cherry"})
x = frozenset(("apple", "banana", "cherry"))
#display x:
print(x)
#display the data type of x:
print(type(x)) 


#EXAMPLE 11 BOOL
x = True
x = bool(5)
#display x:
print(x)
#display the data type of x:
print(type(x)) 


#EXAMPLE 12 BYTES
x = b"Hello"
x = bytes(5)
#display x:
print(x)
#display the data type of x:
print(type(x)) 


#EXAMPLE 13 BYTEARRAY
x = bytearray(5)
#display x:
print(x)
#display the data type of x:
print(type(x)) 


#EXAMPLE 14 MEMORYVIEW
x = memoryview(bytes(5))
#display x:
print(x)
#display the data type of x:
print(type(x)) 


#EXAMPLE 15 NONETYPE
x = None
#display x:
print(x)
#display the data type of x:
print(type(x)) 


#EXAMPLE 16
