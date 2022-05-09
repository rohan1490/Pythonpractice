# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 17:32:59 2022

@author: Rohan Koli
"""

import requests
from bs4 import BeautifulSoup

base_url = "https://www.worldometers.info/coronavirus/country/"
#query_parameter = "ireland" # i represents the page number
query_parameter =input("Enter the name of a country: ").lower()
url = base_url + query_parameter + "/"

#html_text = requests.get('https://www.worldometers.info/coronavirus/country/ireland').text

html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'html.parser')

"""
soup = BeautifulSoup(html_text, 'lxml')
"""

x=soup.find_all('span')

y=soup.find_all("div", class_="row")
y1=y[1].text.strip()

y1[28:69]

n1=y1.find("Last updated:")
n2=y1.find("GMT")

r=soup.find_all('li')

r[6].text

r[6].text.find("new")
r_latest_cases=r[6].text


r1=soup.find_all("div", class_="news_date")
r_fin = r_latest_cases[:r[6].text.find("new")].strip()


print(f"Corona Cases: {x[4].text.replace(' ','')}")
print(f"Deaths: {x[5].text}")
print(f"Recovered: {x[6].text}")
print(y1[n1:(n2+3)])
print(f"New Cases: {r_fin}")
print(f"Latest update on: {r1[0].text}")


