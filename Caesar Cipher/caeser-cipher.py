import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text,shift_amount):
  cypher_text = ""
  for letters in original_text:
     shifted_position = alphabet.index(letters) + shift_amount
     shifted_position %= len(alphabet) # 0 - 25
     cypher_text +=alphabet[shifted_position]
  
  print(f"The encoded Message: {cypher_text}")

#encrypt(text,shift)

def decrypt(original_text,shift_amount):
  output_text = ""
  for letters in original_text:
     shifted_position = alphabet.index(letters) - shift_amount
     shifted_position %= len(alphabet) # 0 - 25
     output_text +=alphabet[shifted_position]
  
  print(f"The encoded Message: {output_text}")

#decrypt(text,shift)



def caesar(original_text,shift_amount,direction):
   if direction == "encode":
         encrypt(text,shift)
   elif direction == "decode":
         decrypt(text,shift)
       
      
again = True
while again:
   direction = input("Type Encode for encryption or Type decode decryption : ").lower()
   text = input("Your Message : ")
   shift =int(input("Type a Integer number : "))      
   caesar(text,shift,direction)
   restart = input("Type 'Yes' if you want to encode or decode again. Otherwise type 'No' : \n").lower()
   if restart == "no":
       again = False
       print("See You Soon")
