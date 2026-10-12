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
			x = (chr(ord(ptxPZISuwuwt[i]) + k))
			if ord(x) > 122:
				x = chr(ord(x) - 26)
		print(x,end="")

welcome = input("Welcome, would you like to encrypt or decrypt? [e/d] ")
key = int(input("Key: "))
text = (input("Text: "))

if welcome == "e":
	cezar_enc(text,key)
elif welcome == "d":
	cezar_dec(text, key)
elif welcome == "b":
	cezar_brut(text)

print("")
