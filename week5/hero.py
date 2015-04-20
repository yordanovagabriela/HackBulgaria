from weapons import Weapons


from spell import Spell


class Hero:
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.max_health = health
        self.weapon_damage = 0
        self.spell_damage = 0

#When a hero reaches 0 health he is considered death.
#When a hero reaches 0 mana, he cannot cast any spells

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        if self.get_health():
            return True
        return False

    def can_cast(self):
        #which returns True, if our hero can cast the magic
        #he has been given. Otherwise - False
        pass

    def take_damage(self, damage_points):
        if damage_points > self.health:
            self.health = 0
        else:
            self.health -= damage_points

    def take_healing(self, healing_points):
        if self.health == 0:
            return False
        if self.health + healing_points > self.max_health:
            self.health = 100
        else:
            self.health += healing_points

    def take_mana(self, mana_points):
        pass
# Our hero can also increase his mana in two ways:
# Each time he makes a move, his mana is increased by mana_regeneration_rate amount.
# He can drink a mana potion, which will increse his mana by the amount of mana points the potion have.
# Hero's mana cannot go above the start mana given to him, neither he can go down below 0 mana.

    def equip(self, weapon):
        # Our hero can equip one weapon and one spell in order to have damage.
        # Check the weapon example for more information.
        self.weapon_damage = weapon.damage

    def learn(self, spell):
        self.spell_damage = spell.damage
        if self.mana < spell.mana_cost:
            raise ValueError
        else:
            self.mana -= spell.mana_cost
        # Our hero can learn only 1 spell at a time.
        # If you learn a given spell, and after this learn another one, the hero can use only the latest.

    def attack(self, by):
        if by == "weapon":
            if self.weapon_damage == 0:
                return "0"
            return self.weapon_damage
        if self.spell_damage == 0:
            return "0"
        return self.spell_damage
