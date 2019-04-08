class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal_name):
        self.animals.append(animal_name)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        index = self.index
        self.index +=1 
        #try:
        return self.animals[index]
        #except IndexError:
        #   raise StopIteration

z = Zoo()
z.add_animal('zebra')
z.add_animal('jellyfish')
z.add_animal('lion')
z.add_animal('bat')

i = iter(z)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))