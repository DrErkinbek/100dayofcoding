import random
friends = ["Alice", "Bob", "Charlie", "David", "Manuel"]
#1 choice
print(random.choice(friends))

#2
random_index = random.randint(0, len(friends)-1)
print(friends[random_index])