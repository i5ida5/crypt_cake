import sys

def cezar_brut(ctxt): #bruteforce function for ceasar cipher, calls ceasar_decrypt
	for every_key in range(26):
		cezar_dec(ctxt,every_key)
		print("")
	
def cezar_dec(ctxt, k): #ceasar decryption function
	print("Plaintext: ", end = "")    
	for i in range(len(ctxt)):
		x = chr(ord(ctxt[i]))
		if 64 < ord(x) < 91:
			x = (chr(ord(ctxt[i]) - k))
			if ord(x) < 65:
				x = chr(ord(x) + 26)		
		elif 96 < ord(x) < 123:
			x = chr(ord(ctxt[i]) - k)
			if ord(x) < 97:
				x = chr(ord(x) + 26)
		print(x, end="")

def cezar_enc(ptxt, k): #ceaser encryption function
	print("Ciphertext: ", end="")
	for i in range(len(ptxt)):
		x = chr(ord(ptxt[i]))
		if 64 < ord(x) < 91:
			x = (chr(ord(ptxt[i]) + k))
			if ord(x) > 90:
				x = chr(ord(x) - 26)
		elif 96 < ord(x) < 123:
			x = (chr(ord(ptxt[i]) + k))
			if ord(x) > 122:
				x = chr(ord(x) - 26)
		print(x,end="")

def substitution(ctxt):
	for letter in range(len(ctxt)):
		counter = 0
		current_char = ctxt[letter]
		for repetition in range(len(ctxt)):
			if ctxt[repetition] == current_char:
				counter += 1
		print(ctxt[letter],": " ,counter)
		




print("Welcome, would you like to decrypt, encrypt or bruteforce?") #welcomes user
system = int(input("1 - decrypt ceasar, 2 - encrypt ceasar, 3 - bruteforce ceasar: ")) #shows options
if system == 1 or system == 2: #for enc and dec prompt key entry
	key = int(input("Key: ")) % 26 #key bigger than 26 loops back(27=1)
elif system == 3 or system == 4: #skips key entry for bruteforcing
	print()
else:
	sys.exit("Invalid decision.") #filters invalid decisions
text = (input("Text: ")) #prompts plain/cipher-text entry

if system == 1: #calls function based on decision
	cezar_dec(text,key)
elif system == 2:
	cezar_enc(text, key)
elif system == 3:
	cezar_brut(text)
elif system == 4:
	substitution(text)

print("") #makes sure entry isn't same row
