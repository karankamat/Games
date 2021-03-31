import random, hangman_art as ha, hangman_words as hw

chosen_word = random.choice(hw.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#display the logo
print(ha.logo)

#create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f"You have already guessed the letter {guess}.")
    else:
      #Check guessed letter
      for position in range(word_length):
          letter = chosen_word[position]
          #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
          if letter == guess:
              display[position] = letter

      #Check if user is wrong.
      if guess not in chosen_word:
          print(f"You guessed a wrong letter {guess}.")
          lives -= 1
          if lives == 0:
              end_of_game = True
              print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
     
    print(ha.stages[lives])
