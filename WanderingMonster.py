import random

class WanderingMonster:
    def __init__(self, x, y, monster_type, color, hp):
        self.x = x
        self.y = y
        self.monster_type = monster_type
        self.color = color
        self.hp = hp

    @classmethod
    def random_spawn(cls, occupied, forbidden, grid_w, grid_h):
        """Finds a random valid coordinate and returns a new monster instance."""
        while True:
            rx = random.randint(0, grid_w - 1)
            ry = random.randint(0, grid_h - 1)
            pos = (rx, ry)
            
            if pos not in occupied and pos not in forbidden:
                # default stats for a new random monster
                return cls(rx, ry, "Goblin", [255, 0, 0], 50)

    @classmethod
    def from_dict(cls, data):
        """Reconstructs the object from a dictionary."""
        return cls(
            data['x'], 
            data['y'], 
            data['monster_type'], 
            data['color'], 
            data['hp']
        )

    def to_dict(self):
        """Returns a JSON-serializable dictionary of the monster state."""
        return {
            "x": self.x,
            "y": self.y,
            "monster_type": self.monster_type,
            "color": self.color,
            "hp": self.hp
        }

    def move(self, occupied, forbidden, grid_w, grid_h):
        """Attempts to move 1 space in a random cardinal direction."""
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
