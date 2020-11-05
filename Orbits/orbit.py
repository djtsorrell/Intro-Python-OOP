import numpy as np
import pandas as pd


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
        # print(self.names)
        # print(self.mass)
        # print(self.pos)
        # print(self.vel)
        # print(self.color)
        # print(self.accel)
        # print(self.force)

    def getForce(self):
        '''Returns the gravitational force using Newtonian mechanics.'''
        for i in range(self.objects):
            forces = 0
            for j in range(self.objects):
                if i != j:
                    delta_pos = self.pos[j]-self.pos[i]
                    forces += \
                        (self.grav_const*self.mass[i]*self.mass[j])\
                        * (delta_pos) / (np.linalg.norm(delta_pos))**3.0
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


orbits = Orbit('marsandmoons.csv', 0.1)
print('Forces')
print(Orbit.getForce(orbits))
print('Accels')
print(Orbit.getAccel(orbits))
print('Vels')
print(Orbit.vel_step(orbits))
print('Pos')
print(Orbit.pos_step(orbits))
