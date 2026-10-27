import base64
from Crypto.Util.number import *
import pwn

"""
ascii = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

for i in range(len(ascii)):
	print(chr(ascii[i]), end = "")
	
print("")
	
hexstring = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
print(bytes.fromhex(hexstring))

print("")

hexstring_into_bytes = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
bytes_into_b64 = bytes.fromhex(hexstring_into_bytes)
b64string = base64.b64encode(bytes_into_b64)
print(b64string)

print("")

pretty_string = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
pretty_string2 = long_to_bytes(pretty_string)
print(pretty_string2)

print("")


text = "label"
rezult = ""
for char in text:
	 rezult += chr(ord(char) ^ 13)
	 
print(rezult)







#KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
#KEY2___KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
#KEY2 ^ KEY3 = 
#FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 

key1  = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key1_xor_key2 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
key2_xor_key3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
flag_xor = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

key2 = pwn.xor(key1 , key1_xor_key2)
key3 = pwn.xor(key2, key2_xor_key3)
flag = pwn.xor(flag_xor,key3,key2,key1)
print(flag)

before = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for i in range(20):
	print(pwn.xor(before, i))


print("")
"""

know_xor_dont = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
print(pwn.xor(know_xor_dont,"crypto{".encode()))
print(pwn.xor(know_xor_dont,"myXORkey".encode()))
	

#for i in range(256):
#	print(pwn.xor(know_xor_dont,i),)








