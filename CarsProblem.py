

class RideRequest:
    def __init__(self, startX, startY, endX, endY, earliest, latest, number):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        self.earliest = earliest
        self.latest = latest
        self.number = number

class Car:
    def __init__(self, number):
        self.number = number
        self.rides = []

    def print(self):
        print(self.number, end=' ')
        for ride in self.rides:
            print(ride.number, end=' ')
        print()

rides = []
with open('a_example.in') as file:
    rows, columns, car_number, ride_number, bonus_value, steps = [int(i) for i in file.readline().split(' ')]
    number = 0
    for line in file.readlines():
        startX, startY, endX, endY, earliest, latest = [int(i) for i in line.split(' ')]
        rides.append(RideRequest(startX, startY, endX, endY,earliest,latest, number) )
        number += 1
    cars = []
    number = 1
    for i in range(car_number):
        cars.append(Car(number))
        number += 1


for car in cars:
    car.print()
