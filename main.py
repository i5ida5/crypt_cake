import sys

def cezar_brut(ctxt):
	k = 1
	print("Bruteforce: ")
	for j in range(25):
		for i in range(len(ctxt)):
			x = (chr(ord(ctxt[i]) - k))		
			if ord(x) < 65 or 90 < ord(x) < 97:
				x = chr(ord(x) + 26)
			print(x, end="")	
		k += 1
		print("")


def cezar_dec(ctxt, k):
	print("Plaintext: ", end = "")
	for i in range(len(ctxt)):
		x = (chr(ord(ctxt[i]) - k))		
		if ord(x) < 65 or 90 < ord(x) < 97:
			x = chr(ord(x) + 26)
		print(x, end="")

def cezar_enc(ptxt, k):
	print("Ciphertext: ", end="")
	for i in range(len(ptxt)):
		x = (chr(ord(ptxt[i]) + k))
		if 90 < ord(x) < 96 or ord(x) > 122:
			x = chr(ord(x) - 26)
		print(x,end="")

welcome = input("Welcome, would you like to encrypt or decrypt? [e/d] ")
#if ord(welcome) != ord("e") or ord(welcome) != ord ("d"):
#	sys.exit("Invalid character.")
key = int(input("Key: "))
text = (input("Text:"))

if welcome == "e":
	cezar_enc(text,key)
elif welcome == "d":
	cezar_dec(text, key)
elif welcome == "b":
	cezar_brut(text)

print("")