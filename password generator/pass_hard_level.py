import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '"', "'", '<', '>', ',', '.', '/', '?', '\\', '|', '~', '']

pass_letters = int(input("How many letters would you like in your password?\n"))
pass_numbers = int(input("How many number would you like?\n"))
pass_symbols = int(input("How many Symbols would you like in ypur password?\n"))


#password empty List
password = []

for char in range(0 , pass_letters):
 password+=random.choice(letters)

for char in range(0, pass_numbers):
 password+=random.choice(numbers)

for char in range(0,pass_symbols):
 password+=random.choice(symbols)


# shuffle the password text 
random.shuffle(password)

# empty string 
password1 = ""

# stroring the value in password1 string
for char in password:
 password1 +=char

print(f"Your Password is: {password1}")