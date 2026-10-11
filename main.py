def cezar_dec(ctxt, k):
	print("Plaintext: ")
	for i in range(len(ctxt)):
		print(chr(ord(ctxt[i]) - k), "")

def cezar_enc(ptxt, k):
	print("Ciphertext: ")
	for i in range(len(ptxt)):
		print(chr(ord(ptxt[i]) + k), "")

key = int(input("Key: "))
plaintext = input("Plaintext:")

cezar_enc(plaintext,key)