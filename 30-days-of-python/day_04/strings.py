# Day 4

#concatenation
x = "thirty" + " " + "days" + " " + "of" + " " + "python"
y = "coding" + " " + "for" + " " + "all"

#functions
company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[7:])
print(company.find("Coding"))
print(company.replace("Coding", "Python"))

python = "Python for everyone"
print(python.replace("Everyone", "All"))

split = company.split(" ")
print(split)

split2 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split2 = split2.split(",")
print(split2)

print(company[0])
print(len(company) - 1)
print(company[10])

pyt = "PFE"
com = "CFA"

print(company.index("C"))
print(company.index("F"))
print("Coding For All People".rfind("l"))

sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))
print(sentence.rindex("because"))
print(sentence[ 31:54])

print(company.startswith("Coding"))
print(company.endswith("Coding"))

print("  Coding For All   ".strip(" "))

print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

print("# ".join(["Django", "Flask", "Bottle", "Pyramid", "Falcon"]))

print("I am enjoying this challenge.\n I just wonder what is next.")

print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square")
