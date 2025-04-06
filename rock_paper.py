import random
# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
print("What do you choose? Print 0 for rock 1 for paper or 2 for scissor",)
user_choice = int(input())
computer_choice = random.randint(0, 2)

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose")
elif computer_choice == user_choice:
    print("It's a draw")

print(user_choice)
print(computer_choice)