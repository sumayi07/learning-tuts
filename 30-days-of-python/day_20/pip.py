# Day 20

import urllib.request
import re
from bs4 import BeautifulSoup
import json
import statistics

url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = urllib.request.urlopen(url)
text = response.read().decode('utf-8')

words = re.findall(r"[a-zA-Z']+", text.lower())

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

top_10 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]
print(top_10)

url = 'https://api.thecatapi.com/v1/breeds'
response = urllib.request.urlopen(url)
data = json.loads(response.read())

def parse_range_avg(range_str):
    # e.g. "3 - 5" -> average of 3 and 5 -> 4.0
    parts = range_str.split(" - ")
    low, high = float(parts[0]), float(parts[1])
    return (low + high) / 2

weights = [parse_range_avg(breed["weight"]["metric"]) for breed in data]
lifespans = [parse_range_avg(breed["life_span"]) for breed in data]

print("Weight (kg):")
print("  min:", min(weights))
print("  max:", max(weights))
print("  mean:", statistics.mean(weights))
print("  median:", statistics.median(weights))
print("  stdev:", statistics.stdev(weights))

print("Lifespan (years):")
print("  min:", min(lifespans))
print("  max:", max(lifespans))
print("  mean:", statistics.mean(lifespans))
print("  median:", statistics.median(lifespans))
print("  stdev:", statistics.stdev(lifespans))

# Frequency tables
country_counts = {}
breed_counts = {}

for breed in data:
    country = breed.get("origin", "Unknown")
    name = breed.get("name", "Unknown")
    country_counts[country] = country_counts.get(country, 0) + 1
    breed_counts[name] = breed_counts.get(name, 0) + 1

print("Country frequency:", country_counts)
print("Breed frequency:", breed_counts)

url = 'https://restcountries.eu/rest/v2/all'
response = urllib.request.urlopen(url)
countries = json.loads(response.read())

# 10 largest countries by population
largest = sorted(countries, key=lambda c: c["population"], reverse=True)[:10]
print([c["name"] for c in largest])

# 10 most spoken languages
lang_counts = {}
for country in countries:
    for lang in country["languages"]:
        name = lang["name"]
        lang_counts[name] = lang_counts.get(name, 0) + 1

top_languages = sorted(lang_counts.items(), key=lambda x: x[1], reverse=True)[:10]
print(top_languages)

# total number of unique languages
print("Total unique languages:", len(lang_counts))

url = 'https://archive.ics.uci.edu/ml/datasets.php'
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response.read(), 'html.parser')

# Grab all links - dataset names are typically inside <a> tags
links = soup.find_all('a')
dataset_names = [link.text.strip() for link in links if link.text.strip()]

print(dataset_names[:20])  # preview first 20