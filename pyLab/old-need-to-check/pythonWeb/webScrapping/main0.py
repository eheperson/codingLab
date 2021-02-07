import requests
from bs4 import BeautifulSoup


base = "https://www.youtube.com/"

y_req = requests.get(base)

print(y_req.status_code)

y_text = y_req.text

y_soup = BeautifulSoup(y_text, 'html.parser')


#print(y_soup.prettify())

# find all <a> tags in html text
#print(y_soup.findAll('a'))

for link in y_soup.findAll('a'):
    print(link)

############################################################################################

muse = "muse"
acdc = "acdc"
metallica = "metallica"

muse_url = base + muse
acdc_url = base + acdc
metallica_url = base + metallica

#muse_req = requests.get(muse_url)
#acdc_req = requests.get(acdc_url)
#metallica_req = requests.get(metallica_url)

videos = "videos"
playlist = "playlist"
about = "about"

bandAbout = base + acdc + about

about_req = requests.get(bandAbout)

############################################################################################
 ## Parsing 

about_text = about_req.text
about_soup = BeautifulSoup(about_text, 'html.parser')

print(about_soup.findAll('meta', {'property' : 'og:title'}))
# print(about_soup.findAll('li', {'class' : 'regular-bla-bla-bla'}))
print("///--/")
for name in about_soup.findAll('div', {'id' : 'tabsContainer'}):
    print("////")
    print(name.text)
