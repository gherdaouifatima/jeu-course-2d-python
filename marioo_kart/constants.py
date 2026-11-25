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
#================================================================================================
#L'ajout des parametres : 
#================================================================================================

# vitesse maximale en marche avant (en pixels / frame) pour éviter que la voiture n'accélère à l'infini.
CAR_MAX_SPEED = 9.0
# décélération quand on freine alors qu'on avance.
CAR_BRAKE_FORCE = 0.35

# poussée et vitesse max en marche arrière
CAR_REVERSE_ACCELERATION = 0.12
CAR_MAX_REVERSE_SPEED = 3.0

#  petit bonus d'accélération et de vitesse max quand la voiture passe sur un bloc boost.   
CAR_BOOST_ACCEL = 0.20
CAR_BOOST_SPEED_FACTOR = 1.35

# angle maximal des roues avant (en degrés)
CAR_MAX_STEER_ANGLE = 30.0

# vitesse à laquelle l'angle de braquage augmente/diminue quand on appuie sur gauche/droite.
CAR_STEER_SPEED = 3.5

# vitesse à laquelle les roues reviennent vers 0 quand on relâche gauche et droite.
CAR_STEER_RETURN = 4.0

# vitesse angulaire maximale de rotation de la caisse (en degrés / frame).
CAR_TURN_SPEED = 3.2

# la résistance de l'air
AIR_DRAG = 0.015

# Proprietes par type de terrain (pour les fonctionnalites de base) :
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
