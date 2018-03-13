import math
import random
import sys

for i in range(5):
    randNumber = random.randint(1, 10)
    print('Random number: ' + str(randNumber))
    if randNumber == 1:
        print('Your number is 1 so I\'ll close your program')
        sys.exit()
    print('Square: ') + str(math.sqrt(randNumber))

