import requests

#requesting test

# adding items
resp = requests.post("http://127.0.0.1:5000/main")
print(resp.text)
# print(resp.content)

payload = {
   'DropDownListCurrency': 'SGD'
}
r = requests.post("http://127.0.0.1:5000", data=payload)

print(r.text)