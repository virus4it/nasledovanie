class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):

        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.__class__.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.__class__.alive = False


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True

rabbit = Mammal("Кролик")
tiger = Predator("Тигр")

rose = Flower("Роза")
apple = Fruit("Яблоко")

rabbit.eat(rose)
rabbit.eat(apple)

tiger.eat(rose)
tiger.eat(apple)
