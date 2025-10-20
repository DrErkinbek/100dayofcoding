# Local scope - when we create a
# variable inside of function

def drink_potion():
    position_strength = 2
    print(position_strength)

# drink_potion()

# block scope
# new enemy available only inside block code

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)

# create_enemy()

# Create global variable inside scope
def make_smothie(item1):
    global ingredients

    ingredients = ["apple", "avocado", "milk", "ice", "nuts", "orange"]

    if item1 in ingredients:
     print(f"Your {item1} smothie is ready to drink")
    else:
        print("Would you try another smothie?")

make_smothie("apple")
