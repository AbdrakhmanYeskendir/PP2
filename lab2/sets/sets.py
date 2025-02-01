#Set items are unordered, unchangeable, and do not allow duplicate values.
myset = {"apple", "banana", "cherry"}   

#Once a set is created, you cannot change its items, but you can remove items and add new items.
# The values True and 1 are considered the same value in sets, and are treated as duplicates

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets

thisset.add("orange")

#Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
# Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


# Remove Item
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
# If the item to remove does not exist, remove() will raise an error.
thisset.discard("banana")
#  If the item to remove does not exist, discard() will NOT raise an error.

print(thisset)


# Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


'''
Join Sets
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
'''

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2) #or set3 = set1 | set2
print(set3)

# Join multiple sets with the union() method:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4) #or myset = set1 | set2 | set3 |set4
print(myset)


#Join a set with a tuple:

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)  #The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

#The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
set3 = set1.intersection(set2)
set3 = set1.difference(set2)#or set3 = set1 - set2
print(set1)

#Use the difference_update() method to keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

#Keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)#or set3 = set1 ^ set2

print(set3)
