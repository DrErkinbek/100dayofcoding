import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6
print(logo)

# make the choosen word random
chosen_word = random.choice(word_list)

# words = ["alma", "banan", "mandarin"]
# chosen_word = random.choice(words)

# print(chosen_word)
# To do - 1
game_over = False
correct_letters = []

while not game_over:
	placeholder = ""
	word_length = len(chosen_word)

	for position in range(word_length):
		placeholder += "_"
	print(placeholder)

	guess = input("Guess a letter ").lower()
	print(guess)


	# TO DO - 2
	display = ""

	for letter in chosen_word:
		if letter == guess:
			display += letter
			correct_letters.append(guess)
		elif letter in correct_letters:
			display += letter
		else:
			display += "_"
	print("Word to guess: "+ display)
 
	if guess not in chosen_word:
		lives -= 1
		print("You guessed that's not in the word. You lose a life.")
  
		if lives == 0:
			game_over = True
			print("It was {chosen_word}. **************You lose***************")
   
	if "_" not in display:
		game_over = True
		print("You win")
		print(f"The chosen word is {chosen_word}")
 
 
	print(stages[lives])