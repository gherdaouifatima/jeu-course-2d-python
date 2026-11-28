import pygame
from constants import TILE_SIZE,DEFAULT_TERRAIN

class Terrain:
    """
    definit les caractéristiques d'un type de terrain
    """
    def __init__(self,name,color):
        self.name=name
        self.color=color
#definition des types de terrains
road=Terrain("route",(85,87,95))
grass=Terrain("herbe",(34,157,80))
dirt=Terrain("terre",(145,74,32))
ice=Terrain("glace",(145,211,229))
void=Terrain("vide",(41,41,52))

class RoadTile:

    def __init__(self, col: int, row: int,terrain=None,block=None):
        self.col = col
        self.row = row
        terrains={"road":road, "grass":grass,"dirt":dirt,"ice":ice,"void":void}
        self.terrain=terrain if terrain is not None else terrains[DEFAULT_TERRAIN]
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
