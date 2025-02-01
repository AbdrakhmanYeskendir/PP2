list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2

for x in list2:
  list1.append(x)

list1.extend(list2)#he purpose is to add elements from one list to another list

print(list3)