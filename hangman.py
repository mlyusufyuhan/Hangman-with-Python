import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)        
    word_letters= set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() 


while len(word_letters) > 0:

    print('you have used these', ' '.join(used_letters))

    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('Current word', ' ' .join(word_list))
    user_letter= input('Guess the letter:').upper()
    if used_letter in  alphabet - used_letters:
     
      used_letter.add(user_letter)
      if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letter:
            print('you have already used the character please try again')    

    else:
        print('invalid character. please try again')


hangman()      
