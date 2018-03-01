import sys

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

    def print(self, output_file):
        print(len(self.rides), end=' ', file=output_file)
        for ride in self.rides:
            print(ride.number, end=' ',file=output_file)
        print(file=output_file)

# --------- Read ----------

for file_example in ['a_example', 'b_should_be_easy', 'c_no_hurry', 'd_metropolis', 'e_high_bonus']:
    rides = []
    with open('input/' + file_example + '.in') as input_file:
        rows, columns, car_number, ride_number, bonus_value, steps = [int(i) for i in input_file.readline().split(' ')]
        
        # Rides
        number = 0
        for line in input_file.readlines():
            startX, startY, endX, endY, earliest, latest = [int(i) for i in line.split(' ')]
            rides.append(RideRequest(startX, startY, endX, endY, earliest, latest, number))
            number += 1

        rides.sort(key=lambda x: x.earliest)
        

        # Cars
        cars = []
        number = 1
        for i in range(car_number):
            cars.append(Car(number))
            number += 1
        nb_cars = len(cars)

    # --------- Compute ----------

    current_step = 0
    while current_step < steps:
        current_rides = rides[(current_step * nb_cars):((current_step + 1) * nb_cars)]

        car_index = 0
        for current_ride in current_rides:
            cars[car_index].rides.append(current_ride)
            car_index += 1

        current_step += 1

    # --------- Output ----------

    with open('output/' + file_example + '.out', 'w') as output_file:
        for car in cars:
            # Print on console and in file
            car.print(sys.stdout)
            car.print(output_file)
