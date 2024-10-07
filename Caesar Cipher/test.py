import random

word_list = ["anything","sometiong","nothing"]

chosen_word = random.choice(word_list)

print(chosen_word) # testing purpose

placeholder = ""
for position in chosen_word:
 placeholder+= "_"

print(placeholder) # testing purpose

guess = input("Enter a letter you have gussed: ").lower()

display = ""
