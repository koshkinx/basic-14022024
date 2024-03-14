class Car:
    def move(self):
        print('car is moving')

    def stop(self):
        print('car stopped')


Car().move()
Car().stop()
print(Car().__str__)
Car().__doc__