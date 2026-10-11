import sys

def cezar_dec(ctxt, k):
	print("Plaintext: ", "")
	for i in range(len(ctxt)):
		print(chr(ord(ctxt[i]) - k), "")

def cezar_enc(ptxt, k):
	print("Ciphertext: ", "")
	for i in range(len(ptxt)):
		x = (chr(ord(ptxt[i]) + k))
		if ord(x) > 122:
			x = chr(ord(x) - 26)
		print(x,"")

welcome = input("Welcome, would you like to encrypt or decrypt? [e/d] ")
if welcome != "e" or "d":
	sys.exit("Invalid character.")
key = int(input("Key: "))
text = (input("Text:"))

if welcome == "e":
	cezar_enc(text,key)
elif welcome == "d":
	cezar_dec(text, key)