chars = "cZ08^<qhwstuR,-defgzxBEOPnijklmrop%(+HIY:}~QNTUv>?6=yb!\"#$SFXAM1./2;GLJK CDVaW4&'3)*5@[7`{_9]|\\"
steps = 2

encresult = []
decresult = []

while True:
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