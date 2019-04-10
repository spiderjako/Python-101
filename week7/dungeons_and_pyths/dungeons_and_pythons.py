class Hero:
    __max_hp = 0
    __max_mana = 0
    __attack_points = 0
    __spell_points = 0

    def __init__(self, name, title, __health, __mana, __mana_regen):
        self.name = name
        self.title = title
        self.__health = __health
        self.__max_hp = self.__health
        self.__mana = __mana
        self.__mana_regen = __mana_regen

    def known_as(self):
        return '{0} the {1}'.format(self.name, self.title)
    def get_hp(self):
        return self.__health
    def get_mana(self):
        return self.__mana
    def is_alive(self):
        return self.get_hp() > 0
            
    def can_cast(self):
        return self.get_mana() > 0

    def take_damage(self, damage_points):
        if damage_points >= self.get_hp():
            self.__health = 0
        else:
            self.__health -= damage_points
        return self.__health
    def take_healing(self, healing_points):
        if self.is_alive()==False:
            return False
        elif self.__health == self.__max_hp:
            return 'Already at max'
        elif self.__health + healing_points < self.__max_hp:
            self.__health += healing_points
            return self.__health
        else:
            self.__health = self.__max_hp
            return self.__health
    def take_mana(self, mana_points):
        if self.__mana == self.__max_mana:
            return 'Already at max'
        elif self.__mana + mana_points < self.__max_mana:
            self.__mana += mana_points
            return self.__mana
        else:
            self.__mana = self.__max_mana
            return self.__mana

h = Hero('Bron', 'Dragon', 100, 100, 2)

print(h.known_as())
print(h.is_alive())
print(h.can_cast())
print(h.take_damage(50))
print(h.take_healing(10))
print(h.take)