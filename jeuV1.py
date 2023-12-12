from random import choice

def get_mot():
    mots = [word.strip() for word in open("mots.txt", encoding="utf-8")]
    return choice(mots)

def jeu():
    essais = 6
    mot = ""
    decouvert = 0
    lettres_trouvees = []
    debut = input("Voulez-vous jouer au jeu du pendu (y/n) ? ").lower()
    if debut == 'y':
        mot = get_mot()
        mot_cache = "_" * len(mot)
        print(mot_cache)
        while decouvert != len(mot):
            lettre = input("\nEntrez une lettre : ")
            if lettre in mot and lettre not in lettres_trouvees:
                lettres_trouvees.append(lettre)
                for i in range(len(mot)):
                    if mot[i] == lettre:
                        mot_cache = mot_cache[:i] + lettre + mot_cache[i+1:]
                        decouvert += 1
                print(f"\n{mot_cache}")
            elif lettre in lettres_trouvees:
                print(f"\n{mot_cache}")
            else:
                essais -= 1
                print("\nEssais restants : ", essais)
                if essais == 0:
                    print("\nVous avez perdu ! Le mot était : ", mot)
                    break

jeu()
