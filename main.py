chars = "cZ08^<qhwstuR,-defgzxBEOPnijklmrop%(+HIY:}~QNTUv>?6=yb!\"#$SFXAM1./2;GLJK CDVaW4&'3)*5@[7`{_9]|\\"
steps = 2
encresult = []
decresult = []

print("---------------------------------------------------")
print("| Encryption / Decryption | 07/04/2022 | Rivolt32 |")
print("---------------------------------------------------")
print("|           Type 'exit' anytime to leave          |")

while True:
	print(" What are you wishing to do")
	#encryption
	text = list(input('Enter a text to encrypt: '))
	for i in text:
		i = chars[chars.index(i)+steps]
		encresult.append(i)
	print("After encryption:",''.join(encresult))

	#decryption
	for i in encresult:
		i = chars[chars.index(i)-steps]
		decresult.append(i)
	print('After decryption:',''.join(decresult))

	print('--------------------------')

	encresult = []
	decresult = []