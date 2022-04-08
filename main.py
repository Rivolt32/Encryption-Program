#functions def
def encrypt():
    print("-------------------------------")
    text = input(' Enter a text to encrypt:\n')
    if text == "exit":
        return 0
    for i in text:
        i = chars[chars.index(i)+steps]
        encresult.append(i)
    print("\nYour encrypted text:\n",''.join(encresult))
    print('-------------------------------\n \n \n')


def decrypt():
    print("-------------------------------")
    text = input(' Enter a text to decrypt:\n')
    if text == "exit":
        return 0
    for i in text:
        i = chars[chars.index(i)-steps]
        decresult.append(i)
    print('\nYour decrypted text:\n',''.join(decresult))
    print('-------------------------------\n \n \n')
    
#end of functions def


chars = "cZà08^<qhùwstuR,-defgïâzxBEOPnüijklçmropû%(è+HIY:}~QNîTUvì>?6=êyb!\"#$SFXAM1ë./2;GLJK CDéVaòW4&'3)*5@[ô7`{_9]|\\"
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
    task = input(" ")

    #encryption
    if task == "1":
        if encrypt() == 0:
            break

    #decryption
    elif task == "2":
        if decrypt() == 0:
            break
    
    #exit
    elif task == "exit" or task == "0":
        break

    else:
        print("Invalid input, choose one of the options available.\n-------------------------------")

    encresult = []
    decresult = []
    