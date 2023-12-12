import pygame, os, random, sys

pygame.init()

FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLEU = (70, 130, 180)
OMBRE = 3  # decalage de l'ombre

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jeu du Pendu")
pygame.display.set_icon(pygame.image.load("images/icone.png"))

# Charge les images du pendu
pendu_images = [pygame.image.load(os.path.join("images", f"pendu{i}.png")) for i in range(0, 5)]

# Charge les mots depuis le fichier mots.txt
with open("mots.txt", "r") as file:
    mots = [mot.strip().lower() for mot in file.readlines()]

# En cas de défaite, affiche le mot correct
mot_a_deviner_actuel = ""

# Choix d'un mot au hasard
def choisir_mot():
    return random.choice(mots)

# Fonction pour afficher le mot avec des espaces entre les lettres
def afficher_mot(mot, lettres_decouvertes):
    affichage = ""
    for lettre in mot:
        if lettre in lettres_decouvertes:
            affichage += lettre + " "
        else:
            affichage += "_ "
    return affichage.strip()

# Menu principal
def afficher_menu():
    screen.fill(BLEU)

    font_large = pygame.font.Font(None, 72)
    titre_texte = font_large.render("Menu Principal", True, BLACK)
    screen.blit(titre_texte, (800 // 2 - titre_texte.get_width() // 2, 50))
    font = pygame.font.Font(None, 36)

    # Ajouter un mot
    ajouter_rect = pygame.Rect(250, 200, 300, 50)
    pygame.draw.rect(screen, BLACK, (ajouter_rect.x + OMBRE, ajouter_rect.y + OMBRE, ajouter_rect.width, ajouter_rect.height))
    pygame.draw.rect(screen, GRAY, ajouter_rect)
    ajouter_texte = font.render("Ajouter un mot", True, BLACK)
    screen.blit(ajouter_texte, (ajouter_rect.centerx - ajouter_texte.get_width() // 2, ajouter_rect.centery - ajouter_texte.get_height() // 2))

    # Jouer
    jouer_rect = pygame.Rect(250, 300, 300, 50)
    pygame.draw.rect(screen, BLACK, (jouer_rect.x + OMBRE, jouer_rect.y + OMBRE, jouer_rect.width, jouer_rect.height))
    pygame.draw.rect(screen, GRAY, jouer_rect)
    jouer_texte = font.render("Jouer au Pendu", True, BLACK)
    screen.blit(jouer_texte, (jouer_rect.centerx - jouer_texte.get_width() // 2, jouer_rect.centery - jouer_texte.get_height() // 2))

    # Quitter
    quitter_rect = pygame.Rect(250, 400, 300, 50)
    pygame.draw.rect(screen, BLACK, (quitter_rect.x + OMBRE, quitter_rect.y + OMBRE, quitter_rect.width, quitter_rect.height))
    pygame.draw.rect(screen, GRAY, quitter_rect)
    quitter_texte = font.render("Quitter", True, BLACK)
    screen.blit(quitter_texte, (quitter_rect.centerx - quitter_texte.get_width() // 2, quitter_rect.centery - quitter_texte.get_height() // 2))


    pygame.display.flip()

    return jouer_rect, ajouter_rect, quitter_rect

def fond_ajouter_mot():
    screen.fill(BLEU)

# Ajouter un mot
def ajouter_mot():
    fond_ajouter_mot()

    font_large = pygame.font.Font(None, 72)
    titre_texte = font_large.render("Ajouter un Mot", True, BLACK)
    screen.blit(titre_texte, (800 // 2 - titre_texte.get_width() // 2, 50))

    font = pygame.font.Font(None, 36)

    # rectangle pour le texte de l'input
    input_rect = pygame.Rect(250, 200, 300, 50)
    pygame.draw.rect(screen, BLACK, (input_rect.x + OMBRE, input_rect.y + OMBRE, input_rect.width, input_rect.height))
    pygame.draw.rect(screen, GRAY, input_rect)
    input_texte = font.render("", True, BLACK)
    screen.blit(input_texte, (input_rect.centerx - input_texte.get_width() // 2, input_rect.centery - input_texte.get_height() // 2))

    # rectangle pour le bouton ajouter
    ajouter_rect = pygame.Rect(250, 300, 300, 50)
    pygame.draw.rect(screen, BLACK, (ajouter_rect.x + OMBRE, ajouter_rect.y + OMBRE, ajouter_rect.width, ajouter_rect.height))
    pygame.draw.rect(screen, GRAY, ajouter_rect)
    ajouter_texte = font.render("Ajouter", True, BLACK)
    screen.blit(ajouter_texte, (ajouter_rect.centerx - ajouter_texte.get_width() // 2, ajouter_rect.centery - ajouter_texte.get_height() // 2))

    pygame.display.flip()

    # Tant que l'utilisateur n'a pas appuyé sur entrée
    input_active = True
    input_text = ""
    clock = pygame.time.Clock()

    # boucle qui gère le clavier
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        screen.fill(BLEU)
        screen.blit(titre_texte, (800 // 2 - titre_texte.get_width() // 2, 50))

        # rectangle pour le texte de l'input
        pygame.draw.rect(screen, BLACK, (input_rect.x + OMBRE, input_rect.y + OMBRE, input_rect.width, input_rect.height))
        pygame.draw.rect(screen, GRAY, input_rect)
        input_texte = font.render(input_text, True, BLACK)
        screen.blit(input_texte, (input_rect.centerx - input_texte.get_width() // 2, input_rect.centery - input_texte.get_height() // 2))

        # rectangle pour le bouton ajouter
        pygame.draw.rect(screen, BLACK, (ajouter_rect.x + OMBRE, ajouter_rect.y + OMBRE, ajouter_rect.width, ajouter_rect.height))
        pygame.draw.rect(screen, GRAY, ajouter_rect)
        screen.blit(ajouter_texte, (ajouter_rect.centerx - ajouter_texte.get_width() // 2, ajouter_rect.centery - ajouter_texte.get_height() // 2))

        pygame.display.flip()
        clock.tick(FPS)

    # si l'utilisateur a entré un mot, l'ajouter au fichier à la ligne suivante
    if input_text:
        with open("mots.txt", "a") as file:
            if file.tell() != 0:
                file.write("\n")
            file.write(input_text)


def fond_jouer():
    screen.fill(BLEU)

def victoire():
    fond_jouer()

    font_large = pygame.font.Font(None, 72)
    titre_texte = font_large.render("Bien joué !", True, BLACK)
    screen.blit(titre_texte, (800 // 2 - titre_texte.get_width() // 2, 50))

    pygame.display.flip()

    pygame.time.wait(3000) # Attendre 3 secondes avant de retourner au menu

def jouer():
    global mot_a_deviner_actuel  

    fond_jouer()

    mot_a_deviner = choisir_mot().lower()
    mot_a_deviner_actuel = mot_a_deviner 
    lettres_decouvertes = set()
    erreurs = 0

    clock = pygame.time.Clock()
    running = True

# boucle qui gère le jeu et touche appuyée
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    lettre = chr(event.key).lower()
                    if lettre not in lettres_decouvertes:
                        lettres_decouvertes.add(lettre)
                        if lettre not in mot_a_deviner:
                            erreurs += 1

        screen.fill(BLEU)

# Affiche le mot à deviner
        font = pygame.font.Font(None, 36)
        mot_affiche = font.render(afficher_mot(mot_a_deviner, lettres_decouvertes), True, BLACK)
        screen.blit(mot_affiche, (800 // 2 - mot_affiche.get_width() // 2, 450)) 

    # si erreurs < 5, affiche les images pendu{i}.png
        if erreurs < 5:
            screen.blit(pendu_images[erreurs], (800 // 2 - pendu_images[erreurs].get_width() // 2, 75))
    # sinon, affiche l'image pendu4.png et le message "Perdu !" en faisant appel à la fonction afficher_bon_mot()
        else:
            afficher_bon_mot()
            pygame.display.flip()
            pygame.time.wait(3000)
            afficher_menu()
            return

        pygame.display.flip()

    # si le mot est entièrement découvert ou si erreurs >= 5, affiche le message "Bien joué !" en faisant appel à la fonction victoire()
        if set(mot_a_deviner) <= lettres_decouvertes or erreurs >= 5:
            victoire() if set(mot_a_deviner) <= lettres_decouvertes else pygame.time.wait(3000)  # Attendre 3 secondes avant de quitter
            running = False

        clock.tick(FPS)

def afficher_bon_mot():
    fond_jouer()

# Affiche le message "Perdu !"
    font_large = pygame.font.Font(None, 72)
    titre_texte = font_large.render("Perdu !", True, BLACK)
    screen.blit(titre_texte, (800 // 2 - titre_texte.get_width() // 2, 50))

    font = pygame.font.Font(None, 36)

# Affiche le mot correct en cas de défaite
    mot_correct_texte = font.render(f"Dommage, le mot était : {mot_a_deviner_actuel.upper()}", True, BLACK)
    screen.blit(mot_correct_texte, (800 // 2 - mot_correct_texte.get_width() // 2, 200))

    pygame.display.flip()

def menu_principal():
    jouer_rect, ajouter_rect, quitter_rect = afficher_menu()

# boucle qui gère le menu et les clics sur les boutons
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if jouer_rect.collidepoint(mouse_pos):
                    jouer()
                    afficher_menu()
                elif ajouter_rect.collidepoint(mouse_pos):
                    ajouter_mot()
                    afficher_menu()
                elif quitter_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

menu_principal()



