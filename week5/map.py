from hero import Hero


class Dungeons:
    def __init__(self, map):
        self.map = map
        # self.symb = []
        self.mapi = ""
        with open(self.map, 'r') as outfile:
            for line in outfile:
                self.mapi += line

    def print_map(self):
        print(self.mapi)

    def spawn(self, hero):
        self.mapi = [list(x) for x in self.mapi.splitlines()]
        for row in range(len(self.mapi)):
            for col in range(len(self.mapi[0])):
                if self.mapi[row][col] == 'S':
                    self.mapi[row][col] = 'H'
                    self.x = row
                    self.y = col
                break
        self.mapi = '\n'.join([''.join(x) for x in self.mapi])

    def move_hero(self, direction):
        self.mapi = [list(x) for x in self.mapi.splitlines()]
        if direction == "up":
            if self.x == 0:
                return False
nwmap = Dungeons("map.txt")
nwmap.print_map()
h = Hero(name="gabi", title="nz", health=100, mana=30, mana_regeneration_rate=1)
nwmap.spawn(h)
nwmap.print_map()
print(nwmap.move_hero(direction="up"))
