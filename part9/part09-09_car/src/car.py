# WRITE YOUR SOLUTION HERE:
class Car:
	 
    def __init__(self):
        self.__petrol = 0
        self.__reading = 0
    
    def __str__(self):
        return f"odometer reading {self.__reading} km, petrol remaining {self.__petrol} litres"
    
    def fill_up(self):
        self.__petrol = 60
    
    def drive(self, amount:int):
        if amount <= self.__petrol:
            self.__reading += amount
            self.__petrol -= amount
	 
if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)



