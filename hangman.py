import random
from word import words
import string


def get_valid_word(words_data):
    word = random.choice(words_data)
    while '-' in word or ' ' in word:
        word = random.choice(words_data)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # store letters in a word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed so far

    lives = int(input("How many lives you want? "))
    score = 0

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # showing letters used
        # ' '.join(['a', 'b', 'cd']) ---> 'a b cd'
        if lives == 1:
            if len(used_letters) != 0:
                print(f"You have {lives} live left and you have used these letters so far: ", ' '.join(used_letters))
            else:
                print(f"You have {lives} live left and you haven't used any letters so far")

        elif len(used_letters) != 0:
            print(f"You have {lives} lives left and you have used these letters so far: ", ' '.join(used_letters))
        else:
            print(f"You have {lives} lives left and you haven't used any letters so far")

        # what current word is (i.e. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        # for letter in word:
        #     if letter in used_letters:
        #         word_list.append(letter)
        #     else:
        #         word_list.append('-')
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                score += 1
                word_letters.remove(user_letter)
            else:
                lives -= 1  # takes out a life

        elif user_letter in used_letters:
            print("You already guessed that letter! Try again")

        else:
            print("Invalid Character!")

    # gets here when word_letters == 0 OR lives == 0

    if lives == 0:
        print("You died. Sorry! The word was", word)
        print("Your score:", score)
    else:
        print("Yay!!! You've guessed the word", word, "correctly!!")
        print("Here's your score:", score)

    return


hangman()
