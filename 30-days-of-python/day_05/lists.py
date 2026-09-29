# Day 5

lst = list()

friends = ["alvin", "charles", "kyle", "anthony", "eddie", "asher"]
length = len(friends)
print(length)
print(friends[0])
print(friends[length//2])
print(friends[length - 1])

mixed_data_types = ["max", 18, "5'10", "single", "idk"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
length = len(it_companies)
print(it_companies)
print(length)
print(it_companies[0])
print(it_companies[length//2])
print(it_companies[length - 1])
it_companies[0] = "Meta"
print(it_companies)
it_companies.append("Nvidia")
it_companies.insert(length//2, "Alibaba")
length += 2
it_companies[0] = it_companies[0].upper()
it_companies = ["#; "] + it_companies
print("Apple" in it_companies)
it_companies.sort()
it_companies.reverse()
first_three = it_companies[:3]
last_three = it_companies[length - 2:]
middle = it_companies[length//2]
it_companies.pop(0)
it_companies.pop(length//2)
it_companies.pop()
it_companies.clear()
del(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
insert = full_stack.index("Redux") + 1
full_stack.insert(insert, "Python")
full_stack.insert(insert, "SQL")
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
length = len(ages)
ages.sort()
print(ages[0])
print(ages[length - 1])
print(ages[length // 2])
print(sum(ages) / length)
print(ages[length -1] - ages[0])
