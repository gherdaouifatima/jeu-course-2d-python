from constants import GameState, GRID_ROWS, GRID_COLS
from model.car import Car
from model.circuit import Circuit
from model.road_tile import RoadTile, grass, road, dirt, ice


class GameModel:

    def __init__(self):
        self.state: str = GameState.MENU
        self.circuit: Circuit | None = None
        self.car: Car | None = None

    def load_circuit(self) -> None:
        grid = [[RoadTile(col=col_idx, row=row_idx)
                for col_idx in range(GRID_COLS)] for row_idx in range(GRID_ROWS)]
        self.build_track(grid)
        self.circuit = Circuit(grid=grid)
        self.spawn_car()

    
    def build_track(self, grid: list[list[RoadTile]]) -> None:
        """
        Définit la disposition des différents terrains
        dans la grille du circuit.
        """

        # Chaque caractère représente une case de la grille.
        layout = [
            "GGGGGGGGGGGGGGGG",
            "GGGRRRRRRRRRRGGG",
            "GGRRRRRRRRRRRRGG",
            "GRRRRGGGGGGRRRRG",
            "GRRRGGGGGGGGRRRG",
            "GRRRGGGGGGGGRRRG",
            "GRRRGGGGGGGGRRRG",
            "GRRRGGGGGGGGRRRG",
            "GRRRRGGGGGGRRRRG",
            "GGRRRRRRRRRRRRGG",
            "GGGRRRRRRRRRRGGG",
            "GGGGGGGGGGGGGGGG"
        ]

        # Association entre chaque lettre du plan et l'objet Terrain correspondant.
        terrains = {
            "G": grass,
            "R": road,
            "D": dirt,
            "I": ice
        }

        # On parcourt chaque ligne du plan.
        for row_idx, line in enumerate(layout):

            # On parcourt chaque caractère de cette ligne.
            for col_idx, symbol in enumerate(line):

                # On récupère la case correspondante dans la grille
                # et on lui attribue le terrain indiqué par la lettre.
                grid[row_idx][col_idx].terrain = terrains[symbol]

                # On vide le sprite pour qu'il soit redessiné
                # avec la nouvelle couleur du terrain.
                grid[row_idx][col_idx].sprite = None


    def spawn_car(self) -> None:
        self.car = Car(7, 1)

    def update(self) -> None:
        if self.state != GameState.RACING or self.circuit is None:
            return
        self.car.update_position()
