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
def freq_anal(ctxt): #frequency analysis function
	ltrs = [] #array of letters in word
	for letter in range(len(ctxt)):
		skip_ltr = False 
		for chr in range(len(ltrs)): #checks if letter has already been added to list
			if ctxt[letter] == ltrs[chr]:
				skip_ltr = True
		if skip_ltr == False: #add letter to list if not already
			ltrs.append(ctxt[letter])
		cur_ltr = len(ltrs) - 1 #focuses on current letter of word, not the one of the whole loop
		counter = 0
		for repetition in range(len(ctxt)): #checks how many times a letter has appeared
			if ctxt[repetition] == ltrs[cur_ltr]:
				counter += 1
		if skip_ltr == False:
			procent = int(counter/len(ctxt)*100)
			print(f'{ltrs[cur_ltr]}{": "}{procent}{"%"}{" "}{"|"}{"="*procent}{ " "*(100-procent)}{"|"}')
	print("-" * 130)
	usual_anal()
def usual_anal():
	crkice = [("A", 8),
			  ("B", 2),
			  ("C", 3),
			  ("D", 4),
			  ("E", 13),
			  ("F", 2),
			  ("G", 2),
			  ("H", 6),
			  ("I", 7),
			  ("J", 0),
			  ("K", 1),
			  ("L", 4),
			  ("M", 2),
			  ("N", 7),
			  ("O", 8),
			  ("P", 2),
			  ("Q", 0),
			  ("R", 6),
			  ("S", 6),
			  ("T", 9),
			  ("U", 3),
			  ("V", 1),
			  ("W", 2),
			  ("X", 0),
			  ("Y", 2),
			  ("Z", 0),
			  ]
	for crka, procent in crkice:
		print(f'{crka}{": "}{procent}{"%"}{" "}{"|"}{"="*procent}{ " "*(100-procent)}{"|"}')


print("Welcome to crypt_cake, a cryptography tool! Choose a tool of your choice: ") #welcomes user
system = int(input("1 - decrypt ceasar, 2 - encrypt ceasar, 3 - bruteforce ceasar, 4 - frequency analysis tool: ")) #shows options
if system == 1 or system == 2: #for enc and dec prompt key entry
	key = int(input("Enter your key: ")) % 26 #key bigger than 26 loops back(27=1)
elif system == 3 or system == 4: #skips key entry for bruteforcing
	print()
else:
	sys.exit("Invalid decision.") #filters invalid decisions
text = (input("Enter your text: ")).replace(" ", "").upper() #prompts plain/cipher-text entry

if system == 1: #calls function based on decision
	cezar_dec(text,key)
elif system == 2:
	cezar_enc(text, key)
elif system == 3:
	cezar_brut(text)
elif system == 4:
	freq_anal(text)

print("") #makes sure entry isn't same row
