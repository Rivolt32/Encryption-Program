chars = "cZ08^<qhwstuR,-defgzxBEOPnijklmrop%(+HIY:}~QNTUv>?6=yb!\"#$SFXAM1./2;GLJK CDVaW4&'3)*5@[7`{_9]|\\"
steps = 2
encresult = []
decresult = []

print("---------------------------------------------------")
print("| Encryption / Decryption | 07/04/2022 | Rivolt32 |")
print("---------------------------------------------------")
print("|           Type 'exit' anytime to leave          |")
print("---------------------------------------------------\n")

while True:
	print(" What are you wishing to do")
	print("   |1| Encrypt a text")
	print("   |2| Decrypt a text")
	print("   |0| Leave the program")
	task = input("teeesttt ")
	
	#encryption
	if task == "1":
		print("-------------------------------")
		text = input(' Enter a text to encrypt:\n')
		if text == "exit":
			break
		for i in text:
			i = chars[chars.index(i)+steps]
			encresult.append(i)
		print("Your encrypted text:\n",''.join(encresult))
		print('-------------------------------\n \n \n')

	#decryption
	if task == "2":
		print("-------------------------------")
		text = input(' Enter a text to decrypt:\n')
		if text == "exit":
			break
		for i in text:
			i = chars[chars.index(i)-steps]
			decresult.append(i)
		print('Your decrypted text:\n',''.join(decresult))
		print('-------------------------------\n \n \n')

	#exit
	if task == "exit" or task == "0":
		break

	if task != "1" and task != "2":
		print("Invalid input, choose one of the options available.\n-------------------------------")

	encresult = []
	decresult = []
	