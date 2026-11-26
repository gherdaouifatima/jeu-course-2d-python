WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
FPS = 60

TILE_SIZE = 64
GRID_COLS = 16
GRID_ROWS = 12

CAR_ACCELERATION = 0.05
CAR_WIDTH = 30
CAR_HEIGHT = 50


class GameState:
    MENU = "menu"
    RACING = "racing"


# --- Couleurs UI ---
COLOR_BG = (15, 15, 25)
COLOR_TEXT = (240, 240, 240)
COLOR_ACCENT = (255, 200, 0)
COLOR_PANEL = (30, 30, 50)
COLOR_PANEL_BORDER = (60, 60, 100)

# ================================================================================================
# Parametres physiques des voitures et des terrains (ajoutes pour la dynamique dans car.py)
# ================================================================================================

# Plafond de vitesse en marche avant pour garder la voiture controlable et eviter qu'elle n'accelere indefiniment.
CAR_MAX_SPEED = 9.0

# Force de deceleration appliquee quand on freine alors que la voiture avance encore ; plus elevee que l'acceleration normale pour permettre des freinages francs avant un virage.
CAR_BRAKE_FORCE = 0.35

# Poussee et vitesse max en marche arriere (en pixels/frame), volontairement plus douces que la marche avant pour faciliter les manœuvres sans rendre la marche arriere trop rapide.
CAR_REVERSE_ACCELERATION = 0.12
CAR_MAX_REVERSE_SPEED = 3.0

# Angle maximal de braquage des roues avant (en degres) pour limiter le rayon de braquage.
CAR_MAX_STEER_ANGLE = 30.0

# Variation de l'angle de braquage par frame (en degres/frame) lorsqu'une touche gauche/droite est maintenue, afin d'obtenir un braquage progressif.
CAR_STEER_SPEED = 3.5

# Vitesse de retour des roues vers l'axe neutre (0 degres/frame) quand aucune touche de direction n'est appuyee, pour eviter que la voiture reste braquee.
CAR_STEER_RETURN = 4.0

# Vitesse angulaire maximale de rotation de la caisse (en degres/frame), modulee ensuite dans car.py selon la vitesse et le sens de marche.
CAR_TURN_SPEED = 3.2

# Frottements de l'air (coefficient applique a chaque frame) pour ralentir naturellement la voiture en roue libre et participer a la limitation de vitesse.
AIR_DRAG = 0.015

# Proprietes par type de terrain :
# - traction : efficacite de l'acceleration et du freinage
# - drift_threshold_deg : angle (en degres) entre orientation et vitesse pour declencher le drift
# - drift_grip : amortissement de la vitesse laterale en cours de drift
# - drift_drag : frottement du terrain en cours de drift (ralentissement)
TERRAIN_PHYSICS = {
    "road": {
        "traction": 1.0,
        "drift_threshold_deg": 28.0,
        "drift_grip": 0.22,
        "drift_drag": 0.045,
    },
    "grass": {
        "traction": 0.72,
        "drift_threshold_deg": 16.0,
        "drift_grip": 0.12,
        "drift_drag": 0.030,
    },
    "dirt": {
        "traction": 0.65,
        "drift_threshold_deg": 12.0,
        "drift_grip": 0.09,
        "drift_drag": 0.020,
    },
    "ice": {
        "traction": 0.35,
        "drift_threshold_deg": 4.0,
        "drift_grip": 0.02,
        "drift_drag": 0.003,
    },
}

DEFAULT_TERRAIN = "road"
