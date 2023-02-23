from abc import abstractmethod 


class Animal:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

    @abstractmethod
    def make_sound(self):
        pass

    # def save(self, animal): ==> violating SRP rules (Adding more than one responsibility)
    #     pass


class SaveAnimalDB:
    def get_animal(self) -> Animal:
        pass

    def save(self, animal: Animal):
        pass
