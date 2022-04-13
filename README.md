# Encryption Program
Simple text encryption program to train my python skills

Don't encrypt this characters: \ 

---

## Notes:

How can someone try to hack a key? Can brut force be enough? If yes, how much time would it take?

use the ra



## To Do:

- Ability to use the generated keys in the main.py file

- Modify the keygen file so the keys are saved in a csv format, so the user can access them from the main.py file


- Make the main.py file read the keys existing in the keys.txt file and make the user choose the key to be used



## Done:

Ask the user what he whichs to do: Encrypt or decrypt

- Create 2 functions:
    - One for encrypting the text 
    - One for decrypting the text

- Add french characters

- Create an infinit key generator by randomizing the order of the characters in the key
    - A separate py program to create new keys and store them in a txt file


The possibility to create multiple key, to store them, and give each one a name. By doing so, i can give the person A the key a, and give an other person B the key b. Even if someone has the program, he wont be able to read the messages of other persons unless they give him the same key too.