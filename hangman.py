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

    lives = 9


while len(word_letters) > 0 and lives > 0:

    print('you have lives',lives,'you have used these letters', ' '.join(used_letters))

    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('Current word', ' ' .join(word_list))
    user_letter= input('Guess the letter:').upper()
    if used_letter in  alphabet - used_letters:
     
      used_letter.add(user_letter)
      if user_letter in word_letters:
            word_letters.remove(user_letter)

      else:
        lives = lives - 1      

    elif user_letter in used_letter:
            print('you have already used the character please try again')    

    else:
        print('invalid character. please try again')

if lives == 0:
    print('you died, sorry. the word was ' , word) 
else:
    print ('you have guessed the word', word,'!!')      


hangman()      
