# Day 16

from datetime import datetime

now = datetime.now()

print(now.day)
print(now.month)
print(now.year)
print(now.hour)
print(now.minute)
print(now.timestamp)

print(now.strftime("%m/%d/%Y, %H:%M:%S"))

day = "5 December, 2019"
date_obj = datetime.strptime(day, "%d %B, %Y")
print(date_obj)

new_year = datetime(2027, 1, 1)
print(new_year - now)

old_date = datetime(1970, 1, 1)
print(now - old_date)

# datetime is really useful for data analysis among other things
# eg. helps document growth of plants, tracks amount of sleep gotten, etc.