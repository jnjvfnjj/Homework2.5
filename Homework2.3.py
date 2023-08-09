class Vehicle:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"марка {self.brand}, модель {self.model}")




class Car(Vehicle):
    def __init__(self, brand, model, year):
        self.year = year
        super().__init__( brand, model)
        

    def info(self):
        print(f"марка {self.brand}, модель {self.model}, год {self.year}")


car =Car("Tesla","BMW",1945)
print(car.info())














class Parent:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f"имя:{self.first_name}, фамилия:{self.last_name}"



class Mother(Parent):
    def __init__(self, first_name, last_name, child_count):
        self.child_count = child_count
        super().__init__(first_name, last_name)

    def get_child_count(self):
        return f"у {self.first_name} {self.child_count} детей"
    


class Father(Parent):
    def __init__(self, first_name, last_name, child_count):
        self.child_count = child_count
        super().__init__(first_name, last_name)

    def get_child_count(self):
        return f"у {self.first_name} {self.child_count} детей"
    


mother = Mother("Жаркын","Иметова",3)
father = Father("Ашим","Батаев",3)
print(mother.get_child_count())
print(father.get_child_count())