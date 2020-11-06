import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.animation import FuncAnimation


class Orbit:

    grav_const = 6.6743E-11

    """Docstring for Orbit. """

    def __init__(self, filename, timestep):
        """TODO: to be defined. """
        self.timestep = timestep
        data = pd.read_csv(filename)
        self.names = np.array(data.Object)
        self.mass = np.array(data.Mass)
        self.color = np.array(data.Color)

        # Finds the number of objects listed in the csv file
        rows = int(data.shape[0])
        # Create 2D arrays with x coordinates in the left hand column and y
        # coordinates in the right.
        self.pos = np.zeros([rows, 2])
        self.vel = np.zeros([rows, 2])
        self.pos[:, 0] = data.r_x
        self.pos[:, 1] = data.r_y
        self.vel[:, 0] = data.v_x
        self.vel[:, 1] = data.v_y
        self.accel = np.zeros([rows, 2])
        self.force = np.zeros([rows, 2])

        self.objects = rows

    def getForce(self):
        '''Returns the gravitational force using Newtonian mechanics.'''
        for i in range(self.objects):
            forces = 0
            for j in range(self.objects):
                if i != j:
                    delta_pos = self.pos[j]-self.pos[i]
                    forces += (
                        (self.grav_const*self.mass[i]*self.mass[j]*delta_pos)
                        / (np.linalg.norm(delta_pos))**3.0
                    )
            self.force[i] = forces
        return self.force

    def getAccel(self):
        '''Returns the acceleration of the planetary bodies.'''
        for i in range(self.objects):
            self.accel[i] = self.force[i]/self.mass[i]
        return self.accel

    def vel_step(self):
        '''Increments the velocities by one timestep.'''
        for i in range(self.objects):
            self.vel[i] = self.vel[i] + self.accel[i]*self.timestep
        return self.vel

    def pos_step(self):
        '''Increments the positions by one timestep.'''
        for i in range(self.objects):
            self.pos[i] = self.pos[i] + self.vel[i]*self.timestep
        return self.pos

    def anim_init(self):
        return self.patches

    def animate(self, i):
        '''Runs the various update methods needed for the animation.'''
        self.getForce()
        self.getAccel()
        self.vel_step()
        self.pos_step()
        for i in range(self.objects):
            self.patches[i].center = (self.pos[i][0], self.pos[i][1])
        return self.patches

    def show(self):
        '''Setup and display the animation.'''
        plt.style.use('dark_background')
        fig = plt.figure()
        ax = plt.axes()
        self.patches = []
        for i in range(self.objects):
            self.patches.append(plt.Circle((self.pos[i][0], self.pos[i][1]),
                                           radius=5E5, color=self.color[i],
                                           animated=True))
            ax.add_patch(self.patches[i])

        # Ensures planets fit in plot.
        r_max = self.pos[self.objects-1][0] + 5.0E6
        ax.set_xlim(-r_max, r_max)
        ax.set_ylim(-r_max, r_max)

        anim = FuncAnimation(fig, self.animate, frames=500,
                             init_func=self.anim_init, repeat=True,
                             interval=50, blit=True)

        plt.show()


orbits = Orbit('marsandmoons.csv', 90)
Orbit.show(orbits)
# print('Forces')
# print(Orbit.getForce(orbits))
# print('Accels')
# print(Orbit.getAccel(orbits))
# print('Vels')
# print(Orbit.vel_step(orbits))
# print('Pos_update')
# print(Orbit.animate(orbits))
# print('Pos_update2')
# print(Orbit.animate(orbits))
