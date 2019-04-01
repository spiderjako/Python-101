class Panda:
    current_panda = 'lyusi'
    def __init__(self, name, food, weight, age, city = 'Sofia', **kwargs):
        self.validate_init_params(name,food,weight)
        self.panda_name = name
        self.food = food
        self.weight = weight
        self.age = age
        self.city = city

    def validate_init_params(self, name, food, weight):
        if name is str:
            print('Panda name is valid')

    def celebrate_birthday(self):
        self.age += 1 

    def __str__(self):
        return 'Panda: {0}'.format(self.panda_name)

panda_ivo = Panda('Ivo', 'ice', 66, 23)
panda_ivo2 = Panda('Ivo','ice', 66, 23)
print(panda_ivo.current_panda)
print(panda_ivo)
print(panda_ivo.panda_name)
print(panda_ivo.food)
print(panda_ivo.weight)
print(panda_ivo.city)
Panda.current_panda = 'Rosi'
print(panda_ivo.current_panda)
panda_ivo.celebrate_birthday()
print(panda_ivo.age)