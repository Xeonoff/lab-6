class Creature:
    def __init__(self, name, strength, agility, intelligence):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.max_health = self.strength ** 2
        self.cur_health = self.max_health
        self.max_stamina = self.strength * self.agility
        self.cur_stamina = self.max_stamina
        self.miss_chance_self = (self.agility ** 2) / 400
        self.crit_chance = (self.intelligence ** 2) / 400
        self.avoid_chance = self.agility * self.intelligence / 400
        self.hand_damage = self.strength * self.agility * self.intelligence / 100
        self.armour_bonus = self.strength * self.intelligence / 400

    def change_name(self, name):
        self.name = name

    def change_strength(self, strength):
        self.__init__(self.name, strength, self.agility, self.intelligence)

    def change_agility(self, agility):
        self.__init__(self.name, self.strength, agility, self.intelligence)

    def change_intelligence(self, intelligence):
        self.__init__(self.name, self.strength, self.agility, intelligence)
