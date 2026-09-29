# Day 22

import requests
import json
from bs4 import BeautifulSoup

url1 = "https://www.bu.edu/president/boston-university-facts-stats/"
url2 = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

response = requests.get(url1)
soup = BeautifulSoup(response.content, "html.parser")
stat_items = soup.find_all("ul", class_ = "custom-stat-list")

facts = {}

for stat_list in stat_items:

    items = stat_list.find_all("li")

    for item in items:
        label = item.find("span", class_ = "stat-label")
        figure = item.find("span", class_ = "stat-figure")

        if label and figure:
            facts[label.text.strip()] = figure.text.strip()

print(facts)

response = requests.get(url2)
soup = BeautifulSoup(response.content, "html.parser")

#yeah nah parsing this wiki table is too hard
