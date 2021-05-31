import requests
from bs4 import BeautifulSoup

desc = "Restaurants"
loc = "Istanbul,+Turkey"
page = 120 #corresponds to page 13
url = f"https://www.yelp.com/search?find_desc={desc}s&find_loc={loc}&start={str(page)}"

yelp_r = requests.get(url)

yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')

print(yelp_soup.findAll('a',{'class':'biz-name'}))

businesses =yelp_soup.findAll('div',{'class':'lemon--div__09f24__1mboc arrange__09f24__AiSIM border-color--default__09f24__R1nRO'})

titles =[]
addresses = []
#phoneNums = []

#yelp_soup.findAll('a',{'class':'lemon--a__09f24__IEZFH link__09f24__1kwXV link-color--inherit__09f24__3PYlA link-size--inherit__09f24__2Uj95'})
for biz in businesses:
    #print(biz.name)
    for title in biz.findAll('a', {'class':'lemon--a__09f24__IEZFH link__09f24__1kwXV link-color--inherit__09f24__3PYlA link-size--inherit__09f24__2Uj95'}):
        titles.append(title.text)
    for address in biz.findAll('address'):
        addresses.append(address.text)
#    for tel in biz.findAll('div', {'class':'lemon--div__09f24__1mboc border-color--default__09f24__R1nRO'}):
#        phoneNums.append(tel.text)

for i in range(len(titles)):
    print(f"Restaurant : {titles[i]}, Adress : {addresses[i]}, Tel : ---")


file_path = 'yelp-{loc}.txt'.format(loc=loc)

with open(file_path, "a", encoding="utf-8") as textfile : 
    for i in range(len(titles)):
        page_line = "-----\n{title}\n{address}\n-----".format(
            title = titles[i],
            address = addresses[i]
        )
        textfile.write(page_line)