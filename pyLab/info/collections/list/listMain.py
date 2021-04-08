
# Lists are used to store multiple items in a single variable.
# List items are ordered, changeable, and allow duplicate values.
#
print("-- Basic List Example --")
thislist = ["apple", "banana", "cherry"]
print(thislist)
print("\n")
#
#
# Ordered          : List items are indexed, the first item has index [0], the second item has index [1] etc.
# Changeable       : The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# Allow Duplicates : Since lists are indexed, lists can have items with the same value.
# List Length : To determine how many items a list has, use the len() function.
# List Items - Data Types : List items can be of any data type.
#
#
#The list() Constructor : It is also possible to use the list() constructor when creating a new list.
print("-- List Constructor Example --")
thislist2 = list(("apple2", "banana2", "cherry2")) # note the double round-brackets
print(thislist2)
print("\n")
#
#
# Access Items : List items are indexed and you can access them by referring to the index number.
print("-- List Indexing Example --")
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print('\n')
#
#
# Range of Indexes : You can specify a range of indexes by specifying where to start and where to end the range.
#                    When specifying a range, the return value will be a new list with the specified items.
print("-- List, Range of Indexes Example --")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print('\n')
#
#
# Negative Indexing : Negative indexing means start from the end
#                     -1 refers to the last item, -2 refers to the second last item etc.
print("-- List Negative Indexing Example --")
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
print('\n')
#
#
# Range of Negative Indexes : Specify negative indexes if you want to start the search from the end of the list:
print("-- List, Range of Negative Indexes Example --")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
print('\n')
#
#
#Check if Item Exists : To determine if a specified item is present in a list use the in keyword:
print("-- List, 'in' keyword Example --")
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
print('\n')
#
#
# Change Item Value : To change the value of a specific item, refer to the index number:
print("-- List, Change Item Value Example --")
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
print('\n')
#
#
# Change a Range of Item Values : To change the value of items within a specific range, 
#                                 define a list with the new values, and refer to the 
#                                 range of index numbers where you want to insert the new values:
print("-- List, Change a Range of Item Value Example --")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
print('\n')
#
#
# Insert Items : To insert a new list item, without replacing any of the existing values, 
#                we can use the insert() method.
#                The insert() method inserts an item at the specified index:
print("-- List, Change a Range of Item Value Example --")
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
print('\n')
#
#
# Append Items : To add an item to the end of the list, use the append() method:
print("-- List, Change a Range of Item Value Example --")
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
print('\n')
#
#
# Insert Items : To insert a list item at a specified index, use the insert() method.
#                The insert() method inserts an item at the specified index:
print("-- List, Change a Range of Item Value Example --")
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
print('\n')
#
#
# Extend List : To append elements from another list to the current list, use the extend() method.
print("-- List, Change a Range of Item Value Example --")
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
print('\n')
#
#
# Add Any Iterable : The extend() method does not have to append lists, 
#                    you can add any iterable object (tuples, sets, dictionaries etc.).
print("-- List, Change a Range of Item Value Example --")
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
print('\n')
#
#
# Remove Specified Item : The remove() method removes the specified item.
print("-- List, Change a Range of Item Value Example --")
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
print('\n')
#
#
# Remove Specified Index : The pop() method removes the specified index.
print("-- List, Change a Range of Item Value Example --")
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
print('\n')
#
#
# Clear the List : The clear() method empties the list.
#                The list still remains, but it has no content.
print("-- List, Change a Range of Item Value Example --")
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
print('\n')
#
#
#