#look at this list of best-selling artists, particularly the table
#for those with more than 250m records sold:
#https://en.wikipedia.org/wiki/List_of_best-selling_music_artists

#1. Are we allowed to scrape the data from this page with a program?
#what two things should we check?

#2. Once verifying that we're allowed to, collect the 250m+ table
#into a csv document.

import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_best-selling_music_artists'
path = r'C:\Users\aosil\OneDrive\Documentos\wiki.csv'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml') #html.parser


tables = soup.find_all('table')
print(len(tables))
print('Madonna' in tables[0].text)

table = tables[0]
rows = table.find_all('tr')
cells = [r.find_all(lambda c: c.name in ['td', 'th']) for r in rows]

text = [[t.text.strip().replace('\n', ' ')  for t in c] for c  in cells ]
print(text[1])
text_rows = [','.join(t) for t in text]
text_body = '\n'.join(text_rows)

with open(path, 'w') as ofline:
    ofline.write(text_body)
    
