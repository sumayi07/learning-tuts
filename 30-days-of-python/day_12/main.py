# Day 12

# import mymodule

# print(mymodule.generate_full_name('Max', 'Sun'))

# import mymodule as m

# print(m.generate_full_name('Max', 'Sun'))

# import sys
# #print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
# print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
# print(sys.path)

import string
import random

def random_user_id():

    id = ''
    rand_gen = string.ascii_letters + string.digits

    for i in range (6):

        id += random.choice(rand_gen)

    return id

def user_id_gen_by_user():

    digits = int(input('Enter number of digits in ID: '))
    num = int(input('Enter number of IDs: '))

    ids = list()
    rand_gen = string.ascii_letters + string.digits

    for i in range (num): 

        id = ''

        for j in range (digits):
            id += random.choice(rand_gen)

        ids.append(id)

    return ids

def rgb_color_gen():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return f'rgb({r},{g},{b})'

def list_of_hexa_colors (num):

    hexa = '0123456789abcdef'
    colors = list()

    for i in range (num):

        color = '#'

        for j in range (6):
            color += random.choice(hexa)

        colors.append(color)

    return colors

def list_of_rgb_colors (num):

    colors = list()

    for i in range (num):
        colors.append(rgb_color_gen())

    return colors

def generate_colors (color_type, num):

    if color_type == 'hexa':
        return list_of_hexa_colors(num)
    elif color_type == 'rgb':
        return list_of_rgb_colors(num)

    print("Invalid type - use 'hexa' or 'rgb'")
    return

def shuffle_list (to_shuffle):

    shuffled_list = list()
    length = len(to_shuffle)

    for i in range (length):

        to_remove = to_shuffle[(random.randint(0, length - 1))]
        shuffled_list.append(to_remove)
        to_shuffle.remove(to_remove)
        length -= 1

    return shuffled_list

def seven_unique():

    nums = set()

    while len(nums) < 7:

        nums.add(random.randint(0, 9))

    return nums

# print(random_user_id())
# print(user_id_gen_by_user())
# print(rgb_color_gen())
# print(list_of_hexa_colors(2))
# print(list_of_rgb_colors(3))
# print(generate_colors('hexa', 5))
print(shuffle_list([1, 2, 3, 4, 5]))
print(seven_unique())