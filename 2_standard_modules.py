from helper import d # Best practice: All imports should always go at the top of any file

# library, package, module : these words are generally interchangeable and usually all reference what is technichally a module

import math
# https://docs.python.org/3/library/math.html

# square root
root = math.sqrt(30)
print(root)

# round the root up
up = math.ceil(root)
print(up)

# round root down
down = math.floor(root)
print(down)

d()

# Import using an alias
import datetime as dt
# https://docs.python.org/3/library/datetime.html

now = dt.datetime.now()
print(now)

start_time = dt.datetime.now() # Testing how fast looping through a list is compared to a tuple
for _ in list(range(1000000)):
    pass
finish = dt.datetime.now()
print(f"The time it took to loop through 1 mil numbers in a list: {finish - start_time}")

start_time = dt.datetime.now() # Testing how fast looping through a list is compared to a tuple
for _ in tuple(range(1000000)):
    pass
finish = dt.datetime.now()
print(f"The time it took to loop through 1 mil numbers in a tuple: {finish - start_time}")

# Create a datetime object from a specific date
my_birthday = dt.date(1991, 10, 9)
print(f"My birthday is: {my_birthday}")

birthday = dt.date(day= 9, month=10, year = 2024)

days_until = birthday - my_birthday
print(days_until)

d()

# from module import functiom/class
from collections import Counter
# https://docs.python.org/3/library/collections.html

colors = ['red', 'blue', 'black', 'blue', 'white', 'green', 'blue', 'orange', 'blue', 'yellow', 'red']

color_counts = Counter(colors)
print(color_counts.most_common(2))
print(color_counts['blue'])