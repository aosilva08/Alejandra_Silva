import pandas as pd
import requests
from bs4 import BeautifulSoup

with open(r'test_page.html', 'r') as page:
    text = page.read()
    
soup = BeautifulSoup(text, 'lxml')

soup.find_all('p')

soup.find('a')

tag = soup.find('a')
tag.attrs
tag.contents
tag.has_attr('href')
tag.parent

soup.find_all('a', href="https://harris.uchicago.edu/")

soup.find_all('a', href=lambda h: 'uchicago' in h)

#slide 33
url = 'http://maktaba.tetea.org/exam-results/FTNA2015/S0206.htm'
path = r'c:\users\jeff levy\desktop\grades.csv'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml') #html.parser

'NHENDE' in soup.text
soup.text[0:300]

#slide 37
table = soup.find('table')
table.find_all('tr')[24].find_all('td')

#slide 42
unparsed_rows = []
for row in table.find_all('tr'):
    td_tags = row.find_all('td')
    unparsed_rows.append([val.text for val in td_tags])
    
unparsed_rows[25]

def row_parser(row):
    if row[4] == 'Absent':
        row = row[:4] + ['Absent']*17
    return ','.join(row)
parsed_rows = [row_parser(row) for row in unparsed_rows[24:152]]
parsed_rows

header = 'CNO,Repeat,Name,Sex,CIV,HIST,GEO,EDK,KIS,ENG,FRN,PHY,CHEM,BIO,COMP,MATH,FOOD,COMM,BKEEPING,GPA,CLASS'
parsed_rows.insert(0, header)

document = '\n'.join(parsed_rows)

with open(path, 'w') as ofile:
    ofile.write(document)
    
    