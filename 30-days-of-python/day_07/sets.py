# Day 7

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add("Twitter")
it_companies.update(["A", "B", "C"])
it_companies.pop()
print(it_companies)
#remove can raise errors when the item to remove isn't found, but discard won't

print(A | B)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
A.update(B)
B.update(A)
del(A)
del(B)

set_age = set(age)
print(len(set_age) >= len(age))
#string is basically a list of characters
#list is a changeable, ordered, index, grouping of objects (allows duplicates)
#tuple is an immutable, ordered, indexed grouping of objects (allows duplicates)
#set is a changeable, unorered, unindex grouping of objects (no duplicates)

print(len(set("I am a teacher and I love to inspire and teach people".split(" "))))
