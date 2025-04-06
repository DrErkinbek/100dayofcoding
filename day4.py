import random

random_integer = random.randint(1, 12)
print(random_integer)

# random.random this function returns 
# floating point number in the range 
# 0.0 <= X <= 1.0
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

#random uniform(a, b) return a random floating point N such a <= N <= b
random_float = random.uniform(1, 10)
print("{:.2f}".format(random_float))

random_in = random.randint(1, 2)
if random_in == 2:
    print('Tails')
else:
    print('Heads')