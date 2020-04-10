#! python 3
# Using of breakpoint
import random

heads = 0

for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads = heads + 1
    if i == 500:
        print('Halfway done!') # right click here and set breakpoint - And click Go on debugger
print('Heads came up ' + str(heads) + ' times.')
