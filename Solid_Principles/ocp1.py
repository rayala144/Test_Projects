# Open for extension, closed for modification
from abc import abstractmethod


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    @abstractmethod
    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return "Roar!!!"


class Bear(Animal):
    def make_sound(self):
        return "Snoar..."


class Horse(Animal):
    def make_sound(self):
        return "Huuuu..hu.hu...."


animals = [
    Bear('bear'),
    Lion('lion'),
    Horse('horse')
]


def animal_sound(animal_list: list):
    for animal in animal_list:
        print(animal.make_sound())


if __name__ == '__main__':
    animal_sound(animals)
