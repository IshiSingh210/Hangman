import random

# lets set some variables

wordList = ["lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",

"laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat","friend","computer","world",

"school", "mango","apple","car","train","plane","tree","water","Stop","Nation","Time"]

word = []

secretWord = random.choice(wordList) # lets randomize single word from the list

length_word = len(secretWord)

alphabet = "abcdefghijklmnopqrstuvwxyz"

letter_storage = []

 

print("Hello!\n")

while True:

    name = input("Please enter Your name\n").strip()

    if name == '':

        print("You can't do that! No blank lines")

    else:

         break

 

while True:

    Choice = input("Would You like to play?\n").upper()

    if Choice == "YES" or Choice == "Y":

        break

    elif Choice == "NO" or Choice == "N":

        print("Maybe some other time")

        break

    else:

        print("Please Answer only Yes or No")

        continue

for character in secretWord: # printing blanks for each letter in secret word

    word.append("-")

print("Ok, so the word You need to guess has", length_word, "characters")

print("Be aware that You can enter only 1 letter from a-z\n\n")

print(word)

   

guess_taken = 1

while guess_taken <= 7:

    guess = input("Pick a letter\n").lower()

    if not guess in alphabet: #checking input

        print("Enter a letter from a-z alphabet")

    elif guess in letter_storage: #checking if letter has been already used

        print("You have already guessed that letter!")

    else:

        letter_storage.append(guess)

        if guess in secretWord:

            print("You guessed correctly!")

            for x in range(0, length_word): #replacing blanks with correct guesses

                if secretWord[x] == guess:

                    word[x] = guess

                    print(word)       

        else:

            print("The letter is not in the word. Try Again!")

            guess_taken += 1

        if '-' not in word:

            print("You won!")

            break

        if guess_taken == 7:

            print(" Sorry Mate, You lost ! The secret word was",secretWord)

            print("Game Over!")

            break

