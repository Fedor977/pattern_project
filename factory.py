"""
2. Factory (Фабрика)
Этот паттерн предоставляет интерфейс для создания объектов в суперклассе,
позволяя подклассам изменять тип создаваемых объектов.
"""

class Animal:
    def speak(self):
        raise NotImplementedError  # Базовый метод, который должен быть переопределён

class Dog(Animal):
    def speak(self):
        return "Woof!"  # Реализация метода speak для собак

class Cat(Animal):
    def speak(self):
        return "Meow!"  # Реализация метода speak для кошек

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")  # Исключение для неизвестного типа

animal = AnimalFactory.create_animal("dog")
print(animal.speak())  # "Woof!"
