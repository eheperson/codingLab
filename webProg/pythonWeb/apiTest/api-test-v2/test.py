#
import requests
#
BASE = "http://127.0.0.1:5000/"
#
TEST = BASE + "test/"
#
response = requests.get(TEST + "p2", {"info":"ehhe"})
print(response.json())
#
input()
#
response = requests.get(TEST + "p2")
print(response.json())
#
input()
#
response = requests.delete(TEST + "p2")
print(response.json())