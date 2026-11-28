
import pygame

# Les touches utilisees par le joueur 1 (ZQSD)
touches_joueur1 = {
    pygame.K_z: "accelerate",
    pygame.K_s: "brake",
    pygame.K_q: "left",
    pygame.K_d: "right"
}

# Les touches utilisees par le joueur 2 (les fleches)
touches_joueur2 = {
    pygame.K_UP: "accelerate",
    pygame.K_DOWN: "brake",
    pygame.K_LEFT: "left",
    pygame.K_RIGHT: "right"
}


#gestion des commandes des joueurs
class InputHandler:

    # initialisation des touches des joueurs
    def __init__(self):
        self.joueur1 = touches_joueur1
        self.joueur2 = touches_joueur2

    # verification des touches appuyees
    def get_inputs(self, touches) -> dict:

        clavier = pygame.key.get_pressed()

        actions = {
            "accelerate": False,
            "brake": False,
            "left": False,
            "right": False
        }

        for touche, action in touches.items():

            # activation de la touche
            if clavier[touche]:
                actions[action] = True

        # On renvoie les actions du joueur
        return actions


#test du code a copier dans une autre fenetre et lance 

#     import pygame
# from controller.input_handler import InputHandler

# # On initialise pygame
# pygame.init()

# # On cree une fenetre pour tester le clavier
# fenetre = pygame.display.set_mode((600, 300))
# pygame.display.set_caption("Test des commandes")

# # On cree un objet pour lire les touches
# clavier = InputHandler()


# continuer = True

# while continuer:

#     for evenement in pygame.event.get():
#         if evenement.type == pygame.QUIT:
#             continuer = False

#     # On recupere les commandes des deux joueurs
#     joueur1 = clavier.get_inputs(clavier.joueur1)
#     joueur2 = clavier.get_inputs(clavier.joueur2)

#     # On affiche les actions dans le terminal
#     print("Joueur 1 :", joueur1)
#     print("Joueur 2 :", joueur2)

#     # On met un fond noir
#     fenetre.fill((0, 0, 0))

#     # On actualise la fenetre
#     pygame.display.flip()

#     # On limite la vitesse de la boucle
#     pygame.time.Clock().tick(10)

# # On ferme pygame
# pygame.quit()

