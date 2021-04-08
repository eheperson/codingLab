import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes":10, "name":"sadbuttruehq1", "views":21},
        {"likes":45, "name":"sadbuttruehq2", "views":22},
        {"likes":56, "name":"sadbuttruehq3", "views":23},
        {"likes":32, "name":"sadbuttruehq4", "views":24},
        {"likes":65, "name":"sadbuttruehq5", "views":25},
        {"likes":12, "name":"sadbuttruehq6", "views":25},
        {"likes":16, "name":"sadbuttruehq7", "views":26}]


for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())
  
input()

response = requests.delete(BASE + "video/0")
print(response)

input()

response = requests.get(BASE + "video/2")
print(response.json())

print("enivicivokki")