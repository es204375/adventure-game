import random

    """
    A class representing a monster that moves independently on the game grid.
    """

class WanderingMonster:
    def __init__(self, x, y, monster_type, color, hp):
        """
        Initializes a new WanderingMonster instance.

        Parameters:
            x (int): The horizontal grid coordinate.
            y (int): The vertical grid coordinate.
            monster_type (str): The name/species of the monster.
            color (list): An RGB list representing the monster's color.
            hp (int): The current health points of the monster.

        Returns:
            None
        """
        self.x = x
        self.y = y
        self.monster_type = monster_type
        self.color = color
        self.hp = hp

    @classmethod
    def random_spawn(cls, occupied, forbidden, grid_w, grid_h):
        """
        Finds a random valid coordinate and returns a new monster instance.

        Parameters:
            occupied (list): A list of (x, y) tuples currently holding other monsters.
            forbidden (list): A list of (x, y) tuples that cannot be entered (e.g., Town).
            grid_w (int): The total width of the grid.
            grid_h (int): The total height of the grid.

        Returns:
            WanderingMonster: A new instance of a monster at a valid location.

        Example:
            >>> m = WanderingMonster.random_spawn([], [(0,0)], 10, 10)
        """
        while True:
            rx = random.randint(0, grid_w - 1)
            ry = random.randint(0, grid_h - 1)
            pos = (rx, ry)
            
            if pos not in occupied and pos not in forbidden:
                # default stats for a new random monster
                return cls(rx, ry, "Goblin", [255, 0, 0], 50)

    @classmethod
    def from_dict(cls, data):
        """
        Reconstructs a monster object from a dictionary (loading games).

        Parameters:
            data (dict): A dictionary containing monsters.

        Returns:
            WanderingMonster: A restored monster instance.

        Example:
            >>> m = WanderingMonster.from_dict({'x': 1, 'y': 2, ...})
        """
        return cls(
            data['x'], 
            data['y'], 
            data['monster_type'], 
            data['color'], 
            data['hp']
        )

    def to_dict(self):
        """
        Returns a JSON  dictionary of the monster state.

        Parameters:
            None

        Returns:
            dict: A dictionary containing all monster attributes.

        Example:
            >>> data = monster.to_dict()
        """
        return {
            "x": self.x,
            "y": self.y,
            "monster_type": self.monster_type,
            "color": self.color,
            "hp": self.hp
        }

    def move(self, occupied, forbidden, grid_w, grid_h):
        """
        Attempts to move 1 space in a random direction.

        Parameters:
            occupied (list): Positions of other monsters to avoid.
            forbidden (list): Positions you can't move on to.
            grid_w (int): The horizontal boundary of the map.
            grid_h (int): The vertical boundary of the map.

        Returns:
            bool: True if the monster successfully moved, False if it stayed put.

        Example:
            >>> monster.move([], [(0,0)], 10, 10)
            True
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            new_x = self.x + dx
            new_y = self.y + dy
            new_pos = (new_x, new_y)

            # check the bounds
            if 0 <= new_x < grid_w and 0 <= new_y < grid_h:
                # check for collisions
                if new_pos not in occupied and new_pos not in forbidden:
                    self.x = new_x
                    self.y = new_y
                    return True # move successful
        
        return False # stayed put
