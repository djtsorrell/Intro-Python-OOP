import random

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Traffic:

    road = 10

    def __init__(self, density, iters):
        self.iters = iters
        cars_init = int(density*self.road)

        # Populates a road with cars in random positions.
        self.cars = [1]*cars_init + [0]*(self.road - cars_init)
        random.shuffle(self.cars)
        # print('Update0: ', self.cars, 'cars = ', self.cars.count(1))
        print(self.cars)

    def update(self):
        print(f'update')
        # counter = 0
        # while counter < self.iters:
        # Create a temporary list to store car movements.
        cars_update = [0]*len(self.cars)
       # counter += 1
        for i, car in enumerate(self.cars):
            # Update method for all but the last index.
            if i < len(self.cars)-1:
                # If there is a car in the current index and no car in the
                # next index, move the car.
                if car == 1 and self.cars[i+1] == 0:
                    cars_update[i] = 0
                    cars_update[i+1] = 1
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
                # If the last index has a car and the first does too, keep
                # the car in the last index.
                elif car == 1 and self.cars[0] == 1:
                    cars_update[i] = 1

        # Update self.cars with movements.
        self.cars = cars_update
        return self.cars

    def init(self):
        print(f'init_func')
        return self.patches

    def animate(self, i):
        print(f'animate')
        self.update()
        for i, car in enumerate(self.cars):
            # if car == 1:
            patch = plt.Rectangle((i, 0), 0.9, 1, angle=0.0, facecolor='r',
                                  edgecolor='w', linewidth='2.0',
                                  animated=True,
                                  visible=bool(car))
            self.patches[i] = patch
#        for i in range(self.road):
#            print(i)
#            self.patches[i].xy = (i, 0)
#        plt.axes.add_patch(self.patches)
        return self.patches

    def show(self):
        plt.style.use('dark_background')
        fig = plt.figure()
        ax = plt.axes()

        self.patches = []

        # Create rectangles for the cars.
        for i, car in enumerate(self.cars):
            # if car == 1:
            patch = plt.Rectangle((i, 0), 0.9, 1, angle=0.0, facecolor='r',
                                  edgecolor='w', linewidth='2.0',
                                  animated=True,
                                  visible=bool(car))
            self.patches.append(patch)
            # else:
            #    self.patches.append(plt.Rectangle((i, 0), 1, 1, angle=0.0,
            #                                      facecolor='k',
            #                                      edgecolor='k',
            #                                      animated=False))

            ax.add_patch(patch)

#        print(f'no. patches = {len(self.patches)}')
        ax.axis('scaled')
        ax.set_xlim(0, self.road)

        anim = FuncAnimation(fig, self.animate, frames=self.iters,
                             init_func=self.init, repeat=False, interval=1000,
                             blit=True)
        plt.show()


cars = Traffic(0.6, 50)
# Traffic.update(cars)
Traffic.show(cars)
# Traffic.test(cars)
