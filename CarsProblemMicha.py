class Simulation:
    def __init__(self, rows, columns, car_number, ride_number, bonus_value, steps):
        self.rows = rows
        self.columns = columns
        self.car_number = car_number
        self.ride_number = ride_number
        self.bonus_value = bonus_value
        self.steps = steps
        self.rides = []
        self.cars = []

    def run(self):
        print("yolo")
            
            




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
        self.roundAvailable = 0

    def isAvailable(self, actualRound):
        return actualRound > self.roundAvailable

    def print(self):
        print(self.number, end=' ')
        for ride in self.rides:
            print(ride.number, end=' ')
        print()

with open('a_example.in') as file:
    rows, columns, car_number, ride_number, bonus_value, steps = [int(i) for i in file.readline().split(' ')]
    sim = Simulation(rows, columns, car_number, ride_number, bonus_value, steps)
    number = 0
    for line in file.readlines():
        startX, startY, endX, endY, earliest, latest = [int(i) for i in line.split(' ')]
        sim.rides.append(RideRequest(startX, startY, endX, endY,earliest,latest, number) )
        number += 1
    number = 1
    for i in range(car_number):
        sim.cars.append(Car(number))
        number += 1


for car in sim.cars:
    car.print()
