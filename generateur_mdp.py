import string
import random

taille = int(input("Entrer le nombre de caracteres du mot de passe que vous souhaiter créer: "))

tout_cara = string.ascii_letters + string.digits + string.punctuation
code1 =  [str(random.choice(tout_cara)) for i in range(taille)]
print(''.join(code1))