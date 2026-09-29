# Day 11

def add_two_numbers (x, y):
    return x + y

def circle(r):
    return 3.14 * r * r

def add_all_nums (*nums):

    sum = 0;

    for num in nums:

        if type(num) != int and type(num) != float:
            return "All args must be nums"
        else: 
            sum += num

    return sum

def celsius_to_fahrenheit (c):
    return (c * 9/5) + 32

def check_season (month):

    if (month < 4):
        return "Winter"
    elif (month < 7):
        return "Spring"
    elif (month < 10):
        return "Summer"
    else:
        return "Fall"

def calculate_slope (x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def solve_quadratic_eqn (a, b, c):
    return  ((-b + (b**2 - 4*a*c)**0.5)/(2*a), (-b - (b**2 - 4*a*c)**0.5)/(2*a))

def print_list (lst):
    for item in lst:
        print(item)

def reverse_list (lst):

    new_lst = []

    for item in lst:
        new_lst.insert(0, item)

    return new_lst

def capitalize_list_items (lst):
    
    for i in range (len(lst)):
        lst[i] = lst[i].capitalize()

    return lst

def add_item (lst, item):

    lst.append(item)

    return lst

def remove_item (lst, item):

    lst.remove(item)

    return lst

def sum_of_numbers (num):

    sum = 0

    for i in range (num + 1):
        sum += i

    return sum

def sum_of_odds (num):

    sum = 0

    for i in range (1, num + 1, 2):
        sum += i

    return sum

def sum_of_evens (num):

    sum = 0

    for i in range (0, num + 1, 2):
        sum += i

    return sum

def evens_and_odds (num):

    evens = 0
    odds = 0

    for i in range (num + 1):

        if i % 2 == 0:
            evens += 1
        else:
            odds += 1

    print("Num evens =", evens)
    print("Num odds =", odds)

def factorial (num):

    factorial = 1

    for i in range (1, num + 1):
        factorial *= i

    return factorial

def is_empty (lst):
    return len(lst) == 0

def calculate_mean (lst):

    sum = 0

    for num in lst:
        sum += num

    return sum/len(lst)

def calculate_median (lst):

    lst.sort()
    n = len(lst)

    if n % 2 == 0:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    
    return lst[len(lst) // 2]

def calculate_mode(lst):
    counts = {}
    for item in lst:
        if item not in counts:
            counts[item] = 1
        else:
            counts[item] += 1
    
    max_count = 0
    for count in counts.values():
        if count > max_count:
            max_count = count
    
    modes = []
    for k, v in counts.items():
        if v == max_count:
            modes.append(k)
    
    return modes

def calculate_range (lst):

    lst.sort()

    return lst[len(lst) - 1] - lst[0]

def calculate_variance (lst):

    v = 0
    u = calculate_mean(lst)

    for num in lst:
        v += (num - u)**2

    return v/len(lst)

def calculate_std (lst):
    return calculate_variance(lst)**0.5

def greet (name = "Guest"):
    print(f"Hello, {name}!")

def show_args (**args):
    pairs = [f"{k}: {v}" for k, v in args.items()]
    print("Received:", ", ".join(pairs))
    
def is_prime (num):

    if num < 2:
        return False

    for i in range (2, num):
        if num % i == 0:
            return False

    return True

def is_unique (lst):
    return len(set(lst)) == len(lst)

def is_same (lst):

    check = type(lst[0])

    for item in lst:
        if type(item) != check:
            return False

    return True

def is_valid (x):
    return x.isidentifier()