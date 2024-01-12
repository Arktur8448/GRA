class Races:
    def __init__(self, name, health, strength, defence, agility):
        self.name = name
        self.health = health
        self.strength = strength
        self.defence = defence
        self.agility = agility

    def set_race(self, given_race):
        # staty podstawowe zwiększone o staty rasy (możliwość hardmodu bez rasy!?!??!)
        if given_race is None:
            return True
            # czyli jak True, to Gracz.strength += Human.strength itd....
        else:
            return False
