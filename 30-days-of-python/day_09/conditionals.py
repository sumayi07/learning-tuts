# Day 9

my_age = 18
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn how to drive")
else:
    print("You need", 18 - age, "more years to learn to drive")

age_diff = 0

if my_age == age:

    print("We are the same age")

elif my_age > age:

    age_diff = my_age - age

    if age_diff == 1:
        print("I am 1 year older than you")
    else:
        print("I am", age_diff, "years older than you")
else:

    age_diff = age - my_age

    if age_diff == 1:
        print("You are 1 year older than me")
    else:
        print("You are", age_diff, "years older than me")

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(a, "is greater than", b)
elif b > a:
    print(b, "is greater than", a)
else:
    print(a, "is equal to", b)

grade = int(input("Enter your grade: "))

if grade > 89:
    print("A")
elif grade > 79:
    print("B")
elif grade > 69:
    print("C")
elif grade > 59:
    print("D")
else:
    print("F")

month = input("Enter your month: ")

if month == "September" or month == "October" or month == "November":
    print("Autumn")
elif month == "December" or month == "January" or month == "February":
    print("Winter")
elif month == "March" or month == "April" or month == "May":
    print("Spring")
elif month == "June" or month == "July" or month == "August":
    print("Summer")

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit")

if fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(fruit)
    print(fruits)

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if "skills" in person:

    lst = person["skills"]
    print(lst[len(lst) // 2])
    print("Python" in lst)

    if "React" in lst and "Node" in lst and "MongoDB" in lst:
        print("Fullstack developer")
    elif "Node" in lst and "Python" in lst and "MongoDB" in lst:
        print("Backend developer")
    elif "JavaScript" in lst and "React" in lst:
        print("Front end developer")
    else: 
        print("Title unknown")

if person.get("is_married") == True and person.get("country") == "Finland":
    print(person.get("first_name"), person.get("last_name"), "lives in Finland. They are married.")