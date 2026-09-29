# Day 14

# map takes in a function and iterable and applies the function to each iteration
# filter takes in a function and iterable and returns an iterable with only the iterations that satisfy the functions condition
# reduce takes in a function and iterable and applies the function to all iterations, returning a single value
 
# hof is a function that takes in other functions as a parameter or returns a function
# closure is when a function is nested within another function
# decorators are wrapper functions that can be used to modify other functions without changing their code

# squared = list(map(square, numbers))
# evens = list(filter(is_even, numbers))
# total = reduce(add, numbers)

from functools import reduce
from countries import countries
from countries_data import countries_data

# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in range (len(countries)): 
#     print(countries[i])

# for i in range (len(names)):
#     print(names[i])

# for i in range (len(numbers)):
#     print(numbers[i])

# upper_countries = list(map(lambda c: c.upper(), countries))
# print(upper_countries)

# squares = list(map(lambda x: x ** 2, numbers))
# print(squares)

# upper_names = list(map(lambda n: n.upper(), names))
# print(upper_names)

# landless_countries = list(filter(lambda c: "land" not in c, countries))
# print(landless_countries)

# no_six_countries = list(filter(lambda c: len(c) != 6, countries))
# print(no_six_countries)

# less_six_countries = list(filter(lambda c: len(c) < 6, countries))
# print(less_six_countries)

# not_e_countries = list(filter(lambda c: c[0] != "E", countries))
# print(not_e_countries)

# upper_landless_countries = list(map(lambda c: c.upper(), filter(lambda c: "land" not in c, countries)))
# print(upper_landless_countries)

# def get_string_lists (lst):

#     return list(filter(lambda s: type(s) == str, lst))

# total = reduce(lambda x, y: x + y, numbers)
# print(total)

# concat_countries = reduce(lambda x, y: f"{x}, {y}", countries)
# print(f"{concat_countries} are north European countries")

# def categorize_countries (countries, pattern):
#     return list(filter(lambda c: pattern in c, countries))

# print(categorize_countries(countries, "land"))

# def countries_dict (countries):

#     alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     dict = {}

#     for i in range (len(alphabet)):

#         dict[alphabet[i]] = len(list(filter(lambda c: c[0] == alphabet[i], countries)))

#     return dict

# better way to do previous

# def improved_countries_dict (countries):

#     dict = {}

#     for c in countries:

#         letter = c[0]

#         if letter not in dict:
#             dict[letter] = 1
#         else: 
#             dict[letter] += 1

#     return dict

# print(countries_dict(countries))
# print(improved_countries_dict(countries))

# def get_first_ten_countries (countries):
#     return countries[:10]

# print(get_first_ten_countries(countries))

# def get_last_ten_countries (countries):
#     return countries[-10:]

# print(get_last_ten_countries(countries))

by_name = sorted(countries_data, key=lambda c: c['name'])
by_capital = sorted(countries_data, key=lambda c: c['capital'])
by_population = sorted(countries_data, key=lambda c: c['population'], reverse=True)

languages = {}
for c in countries_data:
    for lang in c['languages']:
        if lang not in languages:
            languages[lang] = 1
        else:
            languages[lang] += 1

top_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:10]
print(top_languages)

# ten most populated
top_populated = sorted(countries_data, key=lambda c: c['population'], reverse=True)[:10]
print([c['name'] for c in top_populated])