# Day 13

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
no_positives = [i for i in numbers if i < 1]
print(no_positives)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [i for row in list_of_lists for i in row]
print(flattened)

tuple_list = [(i, 1, i, i * i, i ** 3, i ** 4, i ** 5) for i in range(11)]
print(tuple_list)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattened_countries = [[row[0][0].upper(), row[0][0][0:3].upper(), row[0][1].upper()] for row in countries]
print(flattened_countries)

dict_countries = [{"country" : row[0][0].upper(), "city" : row[0][1].upper()} for row in countries]
print(dict_countries)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concat_names = [f"{row[0][0]} {row[0][1]}" for row in names]
print(concat_names)

slope = lambda x1, x2, y1, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda m, x, y: y - m * x