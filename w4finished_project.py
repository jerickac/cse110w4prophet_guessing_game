#I added a list of some prophets and each time someone plays it it's usually with a different secret word

import random

list_of_prophets = ['Lehi', 'Nephi', 'Moses', 'Isaiah', 'Joseph Smith', 'Russel M Nelson']

random_number = random.randint(0, 5)
secret_word = list_of_prophets[random_number]

print('Welcome to the prophet guessing game!')
print(f'Your hint is: {(len(secret_word)) * ' _ '}')

guess = " "
secret_word = secret_word.lower()
number_of_guesses = 0

while guess != secret_word:
    guess = (input('What is your guess? ')).lower()
    print(guess)

    while len(guess) != len(secret_word):
        print('Sorry, the guess must have the same number of letters as the secret word.')
        guess = input('Please enter a new guess: ')
        number_of_guesses = number_of_guesses + 1

    print('Your hint is: ', end="")
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            print(guess[i].capitalize(), end=" ")

        elif guess[i] in secret_word:
            print(guess[i].lower(), end=" ")

        else:
            print(' _ ', end='')
    number_of_guesses = number_of_guesses + 1
    print()
print(f'Congratulations! You guessed it!\nIt took you {number_of_guesses} guesses.')
