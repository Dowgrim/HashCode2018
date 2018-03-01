import math
from enum import Enum

def distance(startX, startY, endX,endY):
    return math.fabs(startX-endX)+math.fabs(startY-endY)

class RideRequest:
    def __init__(self, startX, startY, endX, endY, earliest, latest, number):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        self.earliest = earliest
        self.latest = latest
        self.number = number
        self.done = False

    def getDistance(self):
        return distance(self.startX, self.startY, self.endX, self.endY)
    def getValue(self, start_time, early_bonus):
        bonus = 0
        if start_time == self.earliest:
            bonus = early_bonus
        return self.getDistance() + bonus
    def __str__(self):
        return self.number
class CarState(Enum):
    WAITING_PASSENGER = 0
    WAITING_TO_START = 1
    TRAVELLING_TO_PASSENGER = 2
    TRAVELLING = 3


class Car:
    def __init__(self, number):
        self.number = number
        self.rides = []
        self.steps = 0
        self.x = 0
        self.y = 0
        self.currentRide = None
        self.state = CarState.WAITING_PASSENGER
        self.stepsRemaining = 0
        self.active = True


    def print(self):
        print(len(self.rides), end=' ')
        for ride in self.rides:
            print(ride.number, end=' ')
        print()
    def computeList(self, rides, step, early_bonus):
        rideList = []
        for ride in rides:
            wait_time = distance(self.x, self.y, ride.startX, ride.startY)
            if step + wait_time + ride.getDistance() < ride.latest:# the ride is possible
                rideList.append((ride.getValue(wait_time, early_bonus), ride))
        sorted(rideList, key=lambda ride: ride[0])
        return rideList

    def avalaible(self):
        return self.state == CarState.WAITING_PASSENGER

    def incrementSteps(self, cur_step):
        #print(self.stepsRemaining == 0)
        #print(self.state)
        if self.stepsRemaining > 0:
            self.stepsRemaining -= 1
        if self.stepsRemaining == 0 and not self.avalaible():
            ride = self.rides[len(self.rides) - 1]
            if self.state == CarState.TRAVELLING_TO_PASSENGER:
                if cur_step < ride.earliest:
                    self.state = CarState.WAITING_TO_START
                    self.stepsRemaining = cur_step - ride.earliest
                else:
                    self.state = CarState.TRAVELLING#if we can start
                    self.stepsRemaining = ride.getDistance()
            elif self.state == CarState.TRAVELLING:
                self.state = CarState.WAITING_PASSENGER
                self.x = ride.endX
                self.y = ride.endY
            elif self.state == CarState.WAITING_TO_START:
                self.state = CarState.TRAVELLING
                self.stepsRemaining = ride.getDistance()

    def doRide(self, ride):
        self.rides.append(ride)
        if self.x == ride.startX and self.y == ride.startY:
            self.stepsRemaining = ride.getDistance()
            self.state = CarState.TRAVELLING
        else:
            self.stepsRemaining = distance(self.x, self.y, ride.startX, ride.startY)
            self.state = CarState.TRAVELLING_TO_PASSENGER

rides = []
with open('b_should_be_easy.in') as file:
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

current_step = 0
while current_step < steps:
    if len(rides) == 0:
        break
    for car in cars:
        car.incrementSteps(current_step)
        if car.avalaible():
            rideList = car.computeList(rides, current_step, bonus_value)
            if len(rideList) > 0:
                curRide = rideList[0][1]
                rides.remove(rideList[0][1])
                car.doRide(curRide)
    current_step += 1

for car in cars:
    car.print()
