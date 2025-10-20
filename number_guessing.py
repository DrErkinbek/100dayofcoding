from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# 1 Choosing a random number between 1 and 100
def check_answer(user_guess, actual_answer):
      if user_guess > actual_answer:
            print("Too high")
      elif user_guess < actual_answer:
            print("Too low")
      else:
            print(f"You got it! The answer was {actual_answer}")

# Function to check users guess against actual answer
def set_difficulty():
      level = input("Choose a difficulty. Type 'easy or hard: ")
      if level == "easy":
            return EASY_LEVEL_TURNS
      else:
            return HARD_LEVEL_TURNS


def game():
      print("Welcome to the Number Guessing Game")
      print("I am thinking of a number between 1 and 100")
      answer = randint(1, 100)

      turns = set_difficulty()
      print(f"You have {turns} attempts  remaining to guess the number")

      guess = int(input("Make a guess: "))
      while guess != answer:
            # Let the user guess a number
            guess = int(input("Make a guess: "))
            turns-=1
            print(f"You have {turns} attempts  remaining to guess the number")
            check_answer(guess, answer)
            if turns == 0:
                  break

game()
# Track the number of turns and reduce by 1 if they get it wrong
# Repeat the guessing functionality if they get wrong
