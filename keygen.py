from random import sample


chars = "cZà08^<qhwstuR,-defgïâz]xBEOP|nüijklç{m9ro_pû%(è+HIY:}~Q7NîTUv>?6=êyb!\"#$SFXAM1ë./2;GLJK CDéV[aòW4&'3)*5@ùô`ì"
closing_chars = "\\"  #add this at the end of every generated key -> total len of every key should be 110

#key = "".join(sample(chars, len(chars))) + closing_chars

#print(len(key), key)


####################################################################

print("---------------------------------------------------")
print("|        Key generator      |      Rivolt32       |")
print("---------------------------------------------------")
print("|           Type 'exit' anytime to leave          |")
print("---------------------------------------------------\n")



while True:

	print(" Generate a new key?")

	response = input("  ").lower()


	if response == "yes" or response == "y" :
		# Generating a random key and assigning it to the variable key
		key = "".join(sample(chars, len(chars))) + closing_chars

		print("\n A new key has been created. Give it a name: ")

		key_name = input("  ")

		# Saving the key with its name in keys.txt
		#print(len(key), key)
		with open("keys.txt", "a") as f:
			f.write(f"Key {key_name}:\n{key}\n-------------------------------------------\n")

		print(f"\n The key ({key[:8]}...) has been created and saved with the name \"{key_name}\" in the keys.txt file.\n Press any key to close the program.")
		
		input("  ")

		break



	elif response == "no" or response == "n" or response == "exit" :
		break


	else:
		print(" Invalid input. You can answer using 'yes' or 'y', 'no' or 'n', or close the program by typing 'exit'.\n")