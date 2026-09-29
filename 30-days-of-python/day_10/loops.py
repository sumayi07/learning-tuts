# Day 10

from countries import countries
from countries_data import countries_data

for i in range(11):
    print(i)

count = 0
while count < 11:
    print(count)
    count += 1

for i in range(10, -1, -1):
    print(i)

count = 10
while count > -1:
    print(count)
    count -= 1

string = "#"
for i in range(7):
    print(string)
    string += "#"

for i in range(8):
    for j in range(8):
        print("#", end = " ")
    print()

for i in range(11):
    print(i, "x", i, "=", i*i)

lst = ['Python', 'Numpy','Pandas','Django', 'Flask']

for item in lst:
    print(item)

for i in range(0, 101, 2):
    print(i)

for i in range(1, 100, 2):
    print(i)

sum = 0

for i in range(101):
    sum += i

print(sum)

even_sum = 0
odd_sum = 0

for i in range(101):

    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(even_sum)
print(odd_sum)

countries_with_land = []

for country in countries:

    if "land" in country:
        countries_with_land.append(country)

print(countries_with_land)

fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruits = []

for fruit in fruits:
    new_fruits.insert(0, fruit)

print(new_fruits)

languages = {}
all_countries = {}

for dct in countries_data:

    lang_list = dct.get("languages")

    for lang in lang_list:

        if lang not in languages:
            languages[lang] = 1
        else:
            languages[lang] += 1

    all_countries[dct.get("name")] = dct.get("population")

print("Total number of languages in data", len(languages.keys()))

sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
print(sorted_languages[:10])

sorted_countries = sorted(all_countries.items(), key=lambda x: x[1], reverse=True)
print(sorted_countries[:10])

