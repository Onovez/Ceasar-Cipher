from function import *

stop = False

while not stop:

  answer = input("Type 'encode' to encrypt, type 'decode' tp decrypt:\n> ").lower().strip(" ")
  message = input('Type your message:\n> ').lower()
  shift = int(input('Type the shift number:\n> '))
  shift = shift % 26

  ceasar(txt=message, shift_num=shift, direct=answer)

  # to end the while loop:
  if input("Type 'yes' if you want to go again. Otherwise type 'no'.\n> "
           ).lower() == 'no':
    print('Goodbye')
    stop = True
  else:
    continue
