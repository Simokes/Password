import re,hashlib,json
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def motdepasse(c):
    with open ("json.json","r") as f:
        donnees = json.load(f)

        # if c in donnees:
        #     print("mot des passe deja utilise.")
        for p in donnees:

            if c == p:
                print("mot des passe deja utilise.")
                break
        
        else:
            donnees.append (c)
            with open ("json.json","w") as f:
                json.dump(donnees,f)
            print('Validation de votre mot de passe.')
            print(donnees)
            quit()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            
while True :
    a = input('veuillez entrer votre mot de passe:')

    if len(a)<=7:
        print("Il doit contenir au moins 8 caractères.")

    elif not re.search("[a-z]",a):
        print('Il doit contenir au moins une lettre minuscule.')

    elif not re.search("[A-Z]",a):
        print('Il doit contenir au moins une lettre majuscule.')

    elif not re.search("[1-9]",a):
        print('Il doit contenir au moins un chiffre.')

    elif not re.search("[!, @, #, $, %, ^, &, *]",a):
        print('Il doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).')

    else:

        c = hashlib.sha256(a.encode()).hexdigest()
        motdepasse(c) 

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        with open ("json.json","r") as f:
            donnees = json.load(f)

            for p in  donnees  :

                if c == p:
                    print("mot des passe deja utilise.")
                    break

            else:
                donnees.append (c)
                with open ("json.json","w") as f:
                    json.dump(donnees,f)
                    print('Validation de votre mot de passe.')
                    print(donnees)            
                    break


        
          







            
        
