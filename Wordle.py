import sys
import random

    # read the word list
    # -------------------------------
with open("wordList.txt", "r") as f:
    list_of_words = [line.strip() for line in f]

    # -------------------------------
    # result output function
    # -------------------------------
def result_output(result_num):
    if result_num == 2:
        return "Green"
    elif result_num == 1:
        return "Yellow"
    else:
        return "Gray"

the_word = random.choice(list_of_words)  # secret word

    # -------------------------------
    #  main game loop
attempts = 0
while  attempts < 6:  # max. 6 tries
    print ("Attempts:" , 6 - attempts)
    guess = input("Please enter a 5-letter word: ")
    attempts += 1

     # -------------------------------
    if len(guess) != 5:     # word length check
        print("Word must be 5 letters!")
        attempts -= 1
        continue

    if guess not in list_of_words:     # is real worad check
        print("It's not a valid word.")
        attempts -= 1
        continue
    # -------------------------------

    # 1- letter counter in the secret word
    counter = {}
    for x in the_word:
        counter[x] = the_word.count(x)
    # -------------------------------

    # result 2 = green, 1 = yellow, 0 = gray
    results = [None] * 5

    # -------------------------------
    # 2- GREEN 
    # -------------------------------
    for i in range(5):
        if guess[i] == the_word[i]:
            results[i] = 2  # GREEN
            counter[guess[i]] -= 1

    # -------------------------------
    # 3- YELLOW / GRAY 
    # -------------------------------
    for i in range(5):
        # skip greens
        if results[i] == 2:
            continue

        letter = guess[i]

        # if there is remainings of this letter in secret word -> YELLOW
        if letter in counter and counter[letter] > 0:
            results[i] = 1  # YELLOW
            counter[letter] -= 1
        else:
          results[i] = 0  # GRAY

    # -------------------------------
    # 4- prtint the results in order
    # -------------------------------
    print("\nResult:")
    if results == [2, 2, 2, 2, 2]:
        for i in range(5):
            print(guess[i], "→", result_output(results[i]))
        print("Congratulations! You've guessed the word:", the_word)
        break
    
    for i in range(5):
        print(guess[i], "→", result_output(results[i]))
    # -------------------------------
if attempts == 6 and results != [2, 2, 2, 2, 2]:
    print("Sorry, you've used all attempts. The word was:", the_word)
