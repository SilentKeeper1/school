class Car:
    def __init__(self, mileage, fuel):
        self.mileage = mileage
        self.fuel = fuel

    def vitr(self): 
        self.fuel -= 3
        print('залишилось пального', self.fuel)

    def zapr(self): 
        self.fuel += 10
        print('залишилось пального', self.fuel)

car1 = Car(0, 0)
print('Пробіг', car1.mileage)
car1.zapr()

a = int(input('відстань?'))

while a > 0:
    print('ЇДEMO!')
    a -= 50
    car1.vitr()
    if car1.fuel < 3:
        car1.zapr()