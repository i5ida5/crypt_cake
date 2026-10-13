import sys

def cezar_brut(ctxt):
	for every_key in range(26):
		cezar_dec(ctxt,every_key)
		print("")
	
def cezar_dec(ctxt, k):
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

def cezar_enc(ptxt, k):
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

print("Welcome, would you like to decrypt, encrypt or bruteforce?")
system = int(input("1 - decrypt ceasar, 2 - encrypt ceasar, 3 - bruteforce ceasar: "))
if system == 1 or system == 2:
	key = int(input("Key: ")) % 26
elif system == 3:
	print()
else:
	sys.exit("Invalid decision.")
text = (input("Text: "))

if system == 1:
	cezar_dec(text,key)
elif system == 2:
	cezar_enc(text, key)
elif system == 3:
	cezar_brut(text)

print("")
