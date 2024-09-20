alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plain_text,shift_key):
  cipher_text=""
  for char in plain_text:
    if char in alphabet:  
      position=alphabet.index(char)
      new_position=(position+shift_key)%26
      cipher_text+=alphabet[new_position]
    else:
      cipher_text+=char
  print(f"here the encryption text: {cipher_text}")


def decryption(cipher_text,shift_key):
  plain_text=""
  for char in cipher_text:
    if char in alphabet:
      position=alphabet.index(char)
      new_position=(position-shift_key)%26
      plain_text+=alphabet[new_position]
    else:
      plain_text+=char
  print(f"here the decryption text: {plain_text}")


wanna_end=False

while not wanna_end:
  
  what_to_do=input("Type 'E(capital)'for encrption and 'D(capital)' for decryption: ")
  text=input("Type your message:").lower()
  shift=int(input("Type the shift number: "))
  if what_to_do=="E":
    encryption(plain_text=text,shift_key=shift)
  elif what_to_do=="D":
    decryption(cipher_text=text,shift_key=shift)
  
  play_again=input("Type 'Y(capital)' for cotinue and 'N(capital)' for end: ")
  if play_again=="N":
    wanna_end=True
    print("have a nice day!")
