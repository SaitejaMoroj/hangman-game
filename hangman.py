import random
from hangman_words import word_list
choosen_word=random.choice(word_list)
print("welcome to hangman game")
lives=6
print(choosen_word)
display_words=['_']*len(choosen_word)

guess=input("guess a letter").lower()
found=False


for i in range(len(choosen_word)):
    if choosen_word[i].lower() == guess:
        display_words[i] = guess
        found = True 

if not found:
    lives-=1
    if lives==0:
        print("game over")
    else:
        print('Incorrect guess. Remaining lives:', lives)
print(display_words)
print('Remaining lives:', lives)
