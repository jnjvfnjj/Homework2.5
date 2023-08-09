# import time

# class Timer:
#     def __init__(self, initial_time):
#         self.initial_time = initial_time
#         self.time_left = initial_time

#     def get_time(self):
#         return self.time_left

#     def start(self):
#         while self.time_left > 0:
#             print(f"Осталось времени: {self.time_left} секунд.")
#             time.sleep(1)
#             self.time_left -= 1
#         print("Таймер завершен!")

#     def reset(self):
#         self.time_left = self.initial_time

# timer = Timer(25)

# timer.start()






# #       ище одно задание
# class Cow:
#     def make_sound():
#         return "Мууу"
    
# cow = Cow
# print(cow.make_sound())


# #       2
# class Cars:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.odometer = 0
#         self.type_of = ""
#         self.volume = 0
#         self.is_going = False
#     def info_about_car(self):
#         return {f"brand - {self.brand}, model - {self.model}, year - {self.year}"}
#     def car_is_going(self, km):
#         self.odometer += km
#         self.is_going = True
#         return self.odometer, self.is_going
#     def car_not_going(self):
#         self.is_going = False
#         return self.is_going
    
# cars = Cars('Tayota','Corolla',1987)
# print(cars.info_about_car())


# odometer_reading, is_car_going = cars.car_is_going(100)
# print(f"Пробег: {odometer_reading} km, Машина в движении: {is_car_going}")

# is_car_going = cars.car_not_going()
# print(is_car_going)




# #           3
# class Airplane:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.max_speed = 1200
#         self.odometer = 0
#         self.is_flying = False
#     def take_off(self):
#         self.is_flying = True
#         return self.is_flying
#     def fly(self, distance):
#         return self.odometer + distance
#     def land(self):
#         self.is_flying = False
#         return self.is_flying
#     def info_about_fly(self):
#         if self.is_flying == True:
#             print("самолет летит")
#         else:
#             print("самолет не летит")
#     def info_about_plane(self):
#         print(f"make: {self.make}, model: {self.model}, year: {self.year}")

# airplane_instance = Airplane("Boeing", "737", 2023)


# airplane_instance.info_about_plane()
# print(airplane_instance.take_off())
# print(airplane_instance.fly(500))
# print(airplane_instance.land())
# airplane_instance.info_about_fly()
# airplane_instance.fly(300)
# print(airplane_instance.info_about_plane())



#           4
class Math:
    def addition(a,b):
        print(a + b)
    
    def multiplication(a,b):
        print (a * b)
    
    def division(a,b):
        print (a - b)
    
    def subtraction(a,b):
        print (a / b)
    
math = Math
math.addition(5,5)
math.multiplication(5,5)
math.division(5,5)
math.subtraction(5,5)