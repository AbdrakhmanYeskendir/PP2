# List Items
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
thislist = ["apple", "banana", "cherry"]
thislist = list(("apple", "banana", "cherry"))
print(thislist)
print(len(thislist))
print(type(thislist))
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
thislist[1] = "blackcurrant"
thislist.insert(2, "watermelon")
thislist.append("orange")

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# Add elements of a tuple to a list:
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thislist.remove("banana")
thislist.pop(1) #If you do not specify the index, the pop() method removes the last item.
del thislist[0] 
thislist.clear()

# loops with lists
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.
#simple loop
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#list comprhension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# The condition is like a filter that only accepts the items that evaluate to True.
# Example
# Only accept items that are not "apple":

newlist = [x for x in fruits if x != "apple"]


newlist = [x for x in range(10)]
newlist = [x for x in range(10) if x < 5]


#Expression
# The expression is the current item in the iteration, but it is also the outcome, 
# which you can manipulate before it ends up like a list item in the new list:
newlist = [x.upper() for x in fruits]   

# Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]


# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
# Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]
#The expression in the example above says:
# "Return the item if it is not banana, if it is banana return orange".



