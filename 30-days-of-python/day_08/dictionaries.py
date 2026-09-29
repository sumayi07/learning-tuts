# Day 8

dog = {}
dog["name"] = "Nick"
dog["color"] = "gold"
dog["breed"] = "golden retriever"
dog["legs"] = 4
dog["age"] = 11

print(dog.keys())
print(dog.values())

student = {
    'first_name':'Max',
    'last_name':'Sun',
    'gender':'Male',
    'age':18,
    'country':'USA',
    'is_marred':False,
    'skills':['None'],
    'city':'no',
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

print(len(student))
print(student.get("skills"))
print(type(student.get("skills")))
student["skills"].append("hspu")
print(student.get("skills"))
print(student.keys())
print(student.values())
print(student.items())
student.popitem()
del(student)

