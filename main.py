def cezar_enc(ptxt, k):
	print("Ciphertext: ")
	for i in range(len(ptxt)):
		print(chr(ord(ptxt[i]) + k), "")

key = int(input("Key: "))
plaintext = input("Plaintext:")

cezar_enc(plaintext,key)