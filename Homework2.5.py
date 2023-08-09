class Animals:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def _get_name(self):
        return f"имя - {self._name}"
    
    def _get_age(self):
        return f" возраст - {self._age}"
    


class Dog(Animals):
    def __init__(self, name, age, breed):
        self.breed = breed
        super().__init__(name, age)

    def get_breed(self):
        return f"порода собаки - {self.breed}"
    
    def bark(self):
        return f"{self._name} - аув-аув"
    
    
class Cat(Animals):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def get_color(self):
        return f"цвет кошки - {self.color}"
    
    def meow(self):
        return f"{self._name} - мяу-мяу"
    
dog = Dog("Балли",3,"Бульдок")
cat = Cat("Милли",2,"серый")

print(dog._get_name())
print(dog._get_age())
print(dog.get_breed())
print(dog.bark())

print(cat._get_name())
print(cat._get_age())
print(cat.get_color())
print(cat.meow())
    




