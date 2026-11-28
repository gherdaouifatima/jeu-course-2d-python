import pygame
from constants import TILE_SIZE

class Terrain:
    """
    definit les caractéristiques d'un type de terrain
    """
    def __init__(self,name,color,traction,drift_threshold,drift_friction):
        self.name=name
        self.color=color
        self.traction=traction
        self.drift_threshold=drift_threshold
        self.drift_friction=drift_friction
#definition des types de terrains
road=Terrain("route",(85,87,95),1.0,0.8,1.0)
grass=Terrain("herbe",(34,157,80),0.6,0.4,0.8)
dirt=Terrain("terre",(145,74,32),0.6,0.3,0.5)
ice=Terrain("glace",(145,211,229),0.3,0.1,0.05)
void=Terrain("vide",(41,41,52),0.0,0.0,0.0)

class RoadTile:

    def __init__(self, col: int, row: int,terrain=road,block=None):
        self.col = col
        self.row = row
        self.terrain=terrain
        self.block=block
        self.sprite: pygame.Surface | None = None

    def get_sprite(self, tile_size: int = TILE_SIZE) -> pygame.Surface:
        if self.sprite and self.sprite.get_width() == tile_size:
            return self.sprite
        surface = pygame.Surface((tile_size, tile_size))
        surface.fill(self.terrain.color)
        pygame.draw.rect(surface, (60, 60, 70), surface.get_rect(), 2)

        self.sprite = surface
        return self.sprite
