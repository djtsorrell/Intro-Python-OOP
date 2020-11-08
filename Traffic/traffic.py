import random

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Patch


class Traffic:

    road = 10

    def __init__(self, density, iters, update_method=None):
        self.iters = iters
        self.cars_init = int(density*self.road)

        # Populates a road with cars in random positions.
        self.cars = [1]*self.cars_init + [0]*(self.road - self.cars_init)
        random.shuffle(self.cars)
        # Converts list to array
        self.cars = np.asarray(self.cars)

        # Defines update method to be used in the simulation.
        if update_method is None:
            self.update_method = self.update
        elif update_method == 1:
            self.update_method = self.prob_update
        else:
            raise SystemExit(
                'Error: Not a valid update method.\n'
                'Use either 1 for prob_update or leave blank (i.e. None) '
                'for simple update method.'
            )

    @classmethod
    def setRoad(cls, road_input):
        '''Set the road length.'''
        cls.road = road_input

    def update(self):
        '''
        A simple update method which moves cars if and only if the space in
        front is empty.
        '''
        cars_update = np.zeros(self.road, dtype=int)
        car_moves = 0

        for i, car in enumerate(self.cars):
            # Update method for all but the last index.
            if i < len(self.cars)-1:
                # If there is a car in the current index and no car in the
                # next index, move the car.
                if car == 1 and self.cars[i+1] == 0:
                    cars_update[i] = 0
                    cars_update[i+1] = 1
                    car_moves += 1
                # If there is a car at the current index and a car in the
                # next index, do not move the car.
                elif car == 1 and self.cars[i+1] == 1:
                    cars_update[i] = 1
            # Update method for last index.
            else:
                # If the last index has a car and the first index does not,
                # move the car to the first index.
                if car == 1 and self.cars[0] == 0:
                    cars_update[i] = 0
                    cars_update[0] = 1
                    car_moves += 1
                # If the last index has a car and the first does too, keep
                # the car in the last index.
                elif car == 1 and self.cars[0] == 1:
                    cars_update[i] = 1

        # Update self.cars with movements.
        self.cars = cars_update
        return car_moves

    def prob_update(self):
        ''' Update method based on probabilites. '''
        cars_update = np.zeros(self.road, dtype=int)
        car_moves = 0
        for i, car in enumerate(self.cars):
            # Update method for all but the last index.
            if i < len(self.cars)-1:
                # If there is a car in the current index and no car in the
                # next index, move the car.
                if car == 1 and self.cars[i+1] == 0:
                    cars_update[i] = 0
                    cars_update[i+1] = 1
                    car_moves += 1
                # If there is a car at the current index and a car in the
                # next index, do not move the car.
                elif car == 1 and self.cars[i+1] == 1:
                    cars_update[i] = 1
            # Update method for last index.
            else:
                # If the last index has a car and the first index does not,
                # move the car to the first index.
                if car == 1 and self.cars[0] == 0:
                    cars_update[i] = 0
                    cars_update[0] = 1
                    car_moves += 1
                # If the last index has a car and the first does too, keep
                # the car in the last index.
                elif car == 1 and self.cars[0] == 1:
                    cars_update[i] = 1
        # Update self.cars with movements.
        self.cars = cars_update
        return car_moves

    def getVel(self):
        '''Returns the average velocity of the traffic for one iteration.'''
        car_moves = self.update_method()
        av_vel = float(car_moves / self.cars_init)
        return av_vel

    def show(self):
        '''
        Displays a 2D grid with the car positions along the x axis and the
        iterations along the y axis.
        '''
        plt.style.use('dark_background')
        plt.title('Traffic Simulation')

        plt.xlabel('Road Position')
        plt.ylabel('Iteration')

        ax = plt.gca()
        ax.set_aspect('equal')
        ax.invert_yaxis()

        traffic = np.empty((self.iters, self.road), dtype=int)

        traffic[0] = self.cars
        for i in range(1, self.iters):
            self.update_method()
            traffic[i] = self.cars

        colors = ['k', 'r']
        plt.pcolormesh(traffic, edgecolors='w', linewidth=0.01,
                       cmap=LinearSegmentedColormap.from_list('', colors))

        legend_elements = [Patch(facecolor=color, edgecolor='w') for color in
                           colors]
        ax.legend(handles=legend_elements, labels=['empty', 'car'],
                  loc='upper left', bbox_to_anchor=[1.02, 1])
        plt.tight_layout(pad=4)

        plt.show()

    def show_vel(self):
        '''
        Plots the average velocity of the traffic over the current
        simulation.
        '''
        # Initial velocity of traffic is 0.
        velocities = [0]
        for _ in range(1, self.iters):
            velocities.append(self.getVel())

        x_data = range(self.iters)

        plt.style.use('dark_background')
        plt.plot(x_data, velocities)

        plt.title('Average Velocity of Traffic')
        plt.xlabel('Iteration')
        plt.ylabel('Average Velocity')

        plt.show()


cars = Traffic(0.6, 10)
Traffic.show(cars)
# Traffic.show_vel(cars)
# for i in range(5):
#    print(Traffic.getVel(cars))
