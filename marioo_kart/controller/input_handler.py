
import pygame

# Les touches utilisees par le joueur 1 (ZQSD)
touches_joueur1 = {
    pygame.K_z: "accelerer",
    pygame.K_s: "freiner",
    pygame.K_q: "gauche",
    pygame.K_d: "droite"
}

# Les touches utilisees par le joueur 2 (les fleches)
touches_joueur2 = {
    pygame.K_UP: "accelerer",
    pygame.K_DOWN: "freiner",
    pygame.K_LEFT: "gauche",
    pygame.K_RIGHT: "droite"
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
