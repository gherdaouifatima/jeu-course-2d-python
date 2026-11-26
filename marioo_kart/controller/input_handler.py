
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


# Cette classe permet de gerer les commandes des deux joueurs
class InputHandler:

    # Cette methode initialise les touches des deux joueurs
    # Elle est appelee quand on cree un objet InputHandler
    def __init__(self):
        self.joueur1 = touches_joueur1
        self.joueur2 = touches_joueur2

    # Cette methode verifie les touches appuyees par un joueur
    # Elle renvoie les actions correspondantes dans un dictionnaire
    def get_inputs(self, touches) -> dict:

        # On recupere les touches actuellement appuyees
        clavier = pygame.key.get_pressed()

        # Au debut, aucune action n'est activee
        actions = {
            "accelerate": False,
            "brake": False,
            "left": False,
            "right": False
        }

        # On parcourt les touches et les actions correspondantes
        for touche, action in touches.items():

            # Si une touche est appuyee, on active son action
            if clavier[touche]:
                actions[action] = True

        # On renvoie les actions du joueur
        return actions
