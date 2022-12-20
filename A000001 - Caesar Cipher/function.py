
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def ceasar(txt, shift_num, direct):
    text = ''
    if direct == 'decode':
        shift_num *= -1
    for char in txt:
      #only take the alphabet not the space/symbol/number:
      if char in alphabet:
        pos = alphabet.index(char) 
        new_pos = pos + shift_num
        new_let = alphabet[new_pos]
        text += new_let
      else:
        #appends the space/symbol/number:
        text += char
    print(f'The {direct}d text is: -[ {text} ]-\n')
