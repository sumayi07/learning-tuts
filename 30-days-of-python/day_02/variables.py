# Day 2
#variables
first_name = "Max"
last_name = "Sun"
full_name = first_name + " " + last_name
country = "USA"
city = "North Potomac"
age = 18
year = 2026
is_married = False
is_true = True
is_light_on = True
elementary_school, middle_school, high_school, college = "Travilah", "Robert Frost", "Wootton", "UCLA"

#checking data types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#checking length
print(len(first_name))
print("First name is ", len(first_name), "characters long, while last name is ", len(last_name))

#number arithmetic
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
print(num_one)
print(num_two)
print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

#circle
r = 30
area = 3.14 * r ** 2
circumference = 2 * 3.14 * r
print(r)
print(area)
print(circumference)

r = input("Enter circle radius: ")
print(r)
print(3.14 * float(r) ** 2)
