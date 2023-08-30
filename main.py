import random

print("Welcome to the popular game HANGMAN: In this game, there is a\nsecret word and you must guess the characters or the whole word \nitself before you run out of tries. When you guess wrong, you get \none less try. If you guess correctly, your number of tries stays \nthe same. The computer will randomly choose a word from the magical list! Good luck!! ") 

print()
print()
print()

#word bank
possiblewords = ['retreat', 'swindle', 'bonfire' , 'dearest', 'brick', 'potency', 'trespasser , ·endeavor', 'zipper', 'jazz', 'galaxy' , 'onyx', 'equip', 'burger']

#shows letters when correct
def showLetters(word, dashes, guess): 
  result = "" 
  for i in range(len(word)):
    if word[i] == guess: 
      result = result + guess 
    else:
      result = result + dashes[i]
  return result

#randomizing words
word = random.choice(possiblewords)

#outputting the number of letters and dashes
dashes = "-" * len(word) 
print ( "This word has " + str(len(word)) + " letters in it.")
print (dashes)

#keeping track of attempts
attempts = 5;
print("You have 5 guesses available. Good luck!")

#User guess
while attempts > 0 and dashes != word:
  
  guess = input("What is your guess? Can be a letter or a complete word. : ")

  if guess == word:
    print()
    print("You guessed the whole word!!")
    break
  
  elif guess in word:
    print()
    print("The character is in the word")
    dashes = showLetters(word, dashes, guess)
    print(dashes)
    print()
  
  elif guess not in word:
    print()
    print("The character is not in the word")
    print()
    dashes = showLetters(word, dashes, guess)
    print(dashes)
    print()
    attempts -= 1
    print("You have " + str(attempts) + " guesses left.")

if attempts == 0:
  print("You are out of guesses!")
  print("The word is " + word)

else:
  print("You won!")

