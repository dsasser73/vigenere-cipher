##################################################################
# Author: David Sasser
# Date: April 2017
# Purpose: To encrypt or decrypt a message using a Vigenere Cipher
#		   with key provided
# Version: Python 2.7
##################################################################

import sys

def encrypt():
	# counter used to to know the position in key list
	counter = 0
	# Loop through the characters in the input message
	for x in charList:
		# Checks for uppercase letters
		if(ord(x) >=65 and ord(x) <= 90):
			# Gets the ASCII value and subtract 65
			# so that 0 - 25 is used
			charVal = ord(x) - 65
			if(ord(keyList[counter]) <= 90):
				keyVal = ord(keyList[counter]) - 65
			else:
				keyVal = ord(keyList[counter]) - 97
			sys.stdout.write(chr(((charVal + keyVal) % 26) + 65))
			counter = (counter + 1) % lengthKeyList
		# Checks for lowercase letters
		elif(ord(x) >= 97 and ord(x) <= 122):
			# Gets the ASCII value and subtract 97
			# so that 0 - 25 is used
			charVal = ord(x) - 97
			if(ord(keyList[counter]) <= 90):
				keyVal = ord(keyList[counter]) - 65
			else:
				keyVal = ord(keyList[counter]) - 97
			sys.stdout.write(chr(((charVal + keyVal) % 26) + 97))
			counter = (counter + 1) % lengthKeyList
		# Prints characters other than letters
		else:
			sys.stdout.write(x)

def decrypt():
	# counter used to to know the position in key list
	counter = 0
	# Loop through the characters in the input message
	for x in charList:
		# Checks for uppercase letters
		if(ord(x) >=65 and ord(x) <= 90):
			# Gets the ASCII value and subtract 65
			# so that 0 - 25 is used
			charVal = ord(x) - 65
			if(ord(keyList[counter]) <= 90):
				keyVal = ord(keyList[counter]) - 65
			else:
				keyVal = ord(keyList[counter]) - 97
			sys.stdout.write(chr(((charVal - keyVal) % 26) + 65))
			counter = (counter + 1) % lengthKeyList
		# Checks for lowercase letters
		elif(ord(x) >= 97 and ord(x) <= 122):
			# Gets the ASCII value and subtract 97
			# so that 0 - 25 is used
			charVal = ord(x) - 97
			if(ord(keyList[counter]) <= 90):
				keyVal = ord(keyList[counter]) - 65
			else:
				keyVal = ord(keyList[counter]) - 97
			sys.stdout.write(chr(((charVal - keyVal) % 26) + 97))
			counter = (counter + 1) % lengthKeyList
		# Prints characters other than letters
		else:
			sys.stdout.write(x)

# Gets message to encrypt
inputText = raw_input()

# Stores third argument and on as key and removes all spaces
key = ''.join(i for i in sys.argv[2:])	
# Converts the string into a list of characters
keyList = list(key)
# Converts the input message into a string of characters
charList = list(inputText)
# Stores the length of the key list to use to wrap around
lengthKeyList = len(keyList)
			
# if the user wants to encrypt
if(str(sys.argv[1]) == '-e'):
	encrypt()
# if the user wants to decrypt
if(str(sys.argv[1]) == '-d'):
	decrypt()
