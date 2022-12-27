class item:
    def __init__(self, name,
                 bonus_strength,
                 bonus_agility,
                 bonus_intelligence,
                 bonus_max_health,
                 bonus_max_stamina,
                 bonus_cur_health,
                 bonus_cur_stamina,
                 bonus_miss_chance_self,
                 bonus_crit_chance,
                 bonus_avoid_chance,
                 bonus_hand_damage,
                 bonus_armour_bonus):
        self.name = name
        self.bonus_strength = bonus_strength
        self.bonus_agility = bonus_agility
        self.bonus_intelligence = bonus_intelligence
        self.bonus_max_health = bonus_max_health
        self.bonus_max_stamina = bonus_max_stamina
        self.bonus_cur_health = bonus_cur_health
        self.bonus_cur_stamina = bonus_cur_stamina
        self.bonus_miss_chance_self = bonus_miss_chance_self
        self.bonus_crit_chance = bonus_crit_chance
        self.bonus_avoid_chance = bonus_avoid_chance
        self.bonus_hand_damage = bonus_hand_damage
        self.bonus_armour_bonus = bonus_armour_bonus
