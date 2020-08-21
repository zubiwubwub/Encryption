text_crypt = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

alphabet = 'abcdefghijklmnopqrstuvwxyz'
punctuation = ".,?'! "

#DECRYPTION

def decoder(message, offset):
  clear_message = ""
  for letter in message:
    if not letter in punctuation:
      letter_index = alphabet.find(letter)
      clear_message += alphabet[(letter_index + offset) % 26]
    else:
      clear_message += letter
  return clear_message

#print(decoder(text_crypt, 10))

#ENCRYPTION

text_clear = "hey man, it was an amazing experience because now i can secretly speak to my girl without anyone knowing"

def coder(message, offset):
  crypt_message = ""
  for letter in message:
    if not letter in punctuation:
      letter_index = alphabet.find(letter)
      crypt_message += alphabet[(letter_index - offset) % 26]
    else:
      crypt_message += letter
  return crypt_message

#print(coder(text_crypt, 10))

#BRUTE FORCE HACK

coded_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

def brute_force(message):
  for i in range(1,26):
    print("offset:" + str(i))
    print("\t " + decoder(coded_message, i) + "\n")

#print(brute_force(coded_message))

def vigenere_decoder(coded_message, keyword):
  letter_pointer = 0
  final = ''
  for i in range(0,len(coded_message)):
    if coded_message[i] in punctuation:
      final += coded_message[i]
    else:
      final += keyword[letter_pointer]
      letter_pointer = (letter_pointer+1)%len(keyword)
  translated_message = ''
  for i in range(0, len(coded_message)):
    if not coded_message[i] in punctuation:
      ln = alphabet.find(coded_message[i]) - alphabet.find(final[i])
      translated_message += alphabet[ln % 26]
    else:
      translated_message += coded_message[i]
  return translated_message

message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = "friends"

#print(vigenere_decoder(message, keyword))

def vigenere_coder(message, keyword):
  letter_pointer = 0
  keyword_final = ''
  for i in range(0,len(message)):
      if message[i] in punctuation:
          keyword_final += message[i]
      else:
          keyword_final += keyword[letter_pointer]
          letter_pointer = (letter_pointer+1)%len(keyword)
  translated_message = ''
  for i in range(0,len(message)):
      if message[i] not in punctuation:
          ln = alphabet.find(message[i]) + alphabet.find(keyword_final[i])
          translated_message += alphabet[ln % 26]
      else:
          translated_message += message[i]
  return translated_message

my_message = "i believe im on to something"
keyword = "amazing"

print(vigenere_coder(my_message,keyword))
print(vigenere_decoder(vigenere_coder(my_message, keyword), keyword))

