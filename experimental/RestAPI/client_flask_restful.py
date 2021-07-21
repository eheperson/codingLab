import requests

#requesting test

# adding items
resp = requests.post("http://127.0.0.1:5000/item/item1",data = {'name':'testdata1', 'price':3.5})
print(resp.json())
resp = requests.post("http://127.0.0.1:5000/item/item2",data = {'name':'testdata2', 'price':3})
print(resp.json())
resp = requests.post("http://127.0.0.1:5000/item/item3",data = {'name':'testdata3', 'price':5})
print(resp.json())
resp = requests.post("http://127.0.0.1:5000/item/item4",data = {'price':5})
print(resp.json())
print()
#
# get all items
resp = requests.get("http://127.0.0.1:5000/items")
print(resp.json())
print()
#
# update item
resp = requests.put("http://127.0.0.1:5000/item/item1",data = {'name':'enivicivokki','price':5})
print(resp.json())
print()
#
# get all items
resp = requests.get("http://127.0.0.1:5000/items")
print(resp.json())

