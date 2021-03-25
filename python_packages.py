from random import random # generates random number
import math

#print(random.random())

num_float = 23.6

print("actual float value " + str(num_float))


print(math.floor(num_float)) # if number .5 round it up


print(math.ceil(num_float)) # if number .4 or less round down
# ceil() round up the value

# Python Modules

import os
import datetime, sys

# working_directory = os.getcwd() # it tells us the current directory location
# print(working_directory)

# print(os.uname()) # works on mac

#print(os.cpu.count())
print(datetime.datetime.today())
print(sys.path)
print(math.pi)

