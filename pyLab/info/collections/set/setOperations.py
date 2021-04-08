#
# Add Items
#   Once a set is created, you cannot change its items, but you can add new items.
#
# To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.add("orange")
print(thisset)
#
#
# Add Sets
#   To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#
#
# Add Any Iterable
#   The object in the update() method does not have be a set, 
#   it can be any iterable object (tuples, lists, dictionaries etc.).
#
# Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
#
#
# Remove Item
#   To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.remove("banana")
print(thisset)
#  !!!!! Note: If the item to remove does not exist, remove() will raise an error.   !!!!!   !!!!!   !!!!! 
#
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.discard("banana")
print(thisset)
#  !!!!! Note: If the item to remove does not exist, discard() will NOT raise an error.    !!!!!   !!!!!   !!!!! 
#
#
# You can also use the pop() method to remove an item, 
# but this method will remove the last item. 
# Remember that sets are unordered, so you will not 
# know what item that gets removed.
# 
# The return value of the pop() method is the removed item.
thisset = {"apple", "banana", "cherry"}
print(thisset)
x = thisset.pop()
print(x)
print(thisset)
#  !!!!! Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.     !!!!!   !!!!!   !!!!!
#
#
#   The clear() method empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
#
#
# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
print(thisset)
del thisset
print(thisset)
#
#