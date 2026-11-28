
import pygame
from controller.input_handler import InputHandler

# On initialise pygame
pygame.init()

# On cree une fenetre pour tester le clavier
fenetre = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Test des commandes")

# On cree un objet pour lire les touches
clavier = InputHandler()


continuer = True

while continuer:

    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            continuer = False

    # On recupere les commandes des deux joueurs
    joueur1 = clavier.get_inputs(clavier.joueur1)
    joueur2 = clavier.get_inputs(clavier.joueur2)

    # On affiche les actions dans le terminal
    print("Joueur 1 :", joueur1)
    print("Joueur 2 :", joueur2)

    # On met un fond noir
    fenetre.fill((0, 0, 0))

    # On actualise la fenetre
    pygame.display.flip()

    # On limite la vitesse de la boucle
    pygame.time.Clock().tick(10)

# On ferme pygame
pygame.quit()
