import pygame
import math
from constants import (
    CAR_ACCELERATION, CAR_WIDTH, CAR_HEIGHT, TILE_SIZE , 
        CAR_MAX_SPEED,
        CAR_BRAKE_FORCE,
        CAR_REVERSE_ACCELERATION,
        CAR_MAX_REVERSE_SPEED,
        CAR_MAX_STEER_ANGLE,
        CAR_STEER_SPEED,
        CAR_STEER_RETURN,
        CAR_TURN_SPEED,
        AIR_DRAG,
        TERRAIN_PHYSICS,
        DEFAULT_TERRAIN,
)
    
class Car:

    def __init__(self, start_col: int, start_row: int):
        self.x = start_col * TILE_SIZE + TILE_SIZE // 2
        self.y = start_row * TILE_SIZE + TILE_SIZE // 2
        self.speed: float = 0.0
        self.angle: float = 0.0
        self.sprite = self.build_sprite()
        
        # Vecteur vitesse pour distinguer l'avance et la glisse laterale
        self.vx: float = 0.0
        self.vy: float = 0.0
        
        # Angle de braquage des roues (en degres) et etat de derapage automatique ( drift )
        self.steer_angle: float = 0.0
        self.is_drifting: bool = False
