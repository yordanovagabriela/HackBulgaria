from hero import Hero


class Enemies(Hero):
    def __init__(self, health, mana, damage):
        self.health = health
        self.mana = mana
        self.damage = damage

en = Enemies(20, 20, 100)
print(en.is_alive())
