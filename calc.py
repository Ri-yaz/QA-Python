"""
import modules
print(modules.add(2,3))
print(modules.sub(2,3))


from modules import add 
print (add(5,5))

import math
print(dir(math))
print(math.sqrt(16))

password generator : uppercase, lowercase, special character, numbers
otp generator : length user input
"""
import random
#print(dir(random))
print(random.randint(1,100))

car=['car','bike','bus','cycle']
print(random.choice(car))

length=int(input("Enter otp length: "))

otp=""

for i in range(length):
    otp +=str(random.randint(0,9))
    print("Generated otp:", otp)