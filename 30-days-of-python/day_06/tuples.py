# Day 6

tple = ()
sisters = ("Joy",)
brothers = ()
siblings = sisters + brothers
family_members = ("Dad", "Mom",) + siblings
print(len(siblings))
print(family_members)

Dad, Mom, *Sister = family_members
print(Dad)
print(Mom)
print(Sister)

fruits = ("strawberry", "apple", "peach")
vegetables = ("broccoli", "greenbean", "lettuce")
animal = ("eggs", "beef", "ham")
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
middle_item = food_stuff_lt[len(food_stuff_lt) // 2]
first_three = food_stuff_lt[0:3]
last_three = food_stuff_lt[len(food_stuff_lt) - 3:]
print(middle_item)
print(first_three)
print(last_three)

del(food_stuff_tp)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
