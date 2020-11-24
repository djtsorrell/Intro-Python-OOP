import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D


class Orbit:
    # pylint: disable=too-many-instance-attributes
    grav_const = 6.6743e-11

    """Docstring for Orbit. """

    def __init__(self, filename, timestep):
        """TODO: to be defined. """
        self.timestep = timestep
        data = pd.read_csv(filename)
        self.names = np.array(data.Object)
        self.mass = np.array(data.Mass)
        self.radius = np.array(data.Radius)
        self.color = np.array(data.Color)

        # Finds the number of objects listed in the csv file
        rows = int(data.shape[0])
        # Initialises empty arrays for kinetic and gravitational potential
        # energies.
        self.kinetic = np.zeros(rows)
        self.potential = np.zeros(rows)
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
        # Initialise pathces to be filled in the show method.
        self.patches = []
        # Initialises data lists for plotting kinetic energy
        self.time = []
        self.energy = []

    def getForce(self):
        """Returns the gravitational force using Newtonian mechanics."""
        for i in range(self.objects):
            forces = 0
            for j in range(self.objects):
                if i != j:
                    delta_pos = self.pos[j] - self.pos[i]
                    forces += ((Orbit.grav_const * self.mass[i] * self.mass[j]
                                * delta_pos)
                               / (np.linalg.norm(delta_pos)) ** 3.0)
            self.force[i] = forces
        return self.force

    def getAccel(self):
        """Returns the acceleration of the planetary bodies."""
        for i in range(self.objects):
            self.accel[i] = self.force[i] / self.mass[i]
        return self.accel

    def vel_step(self):
        """Increments the velocities by one timestep."""
        for i in range(self.objects):
            self.vel[i] = self.vel[i] + self.accel[i] * self.timestep
        return self.vel

    def pos_step(self):
        """Increments the positions by one timestep."""
        for i in range(self.objects):
            self.pos[i] = self.pos[i] + self.vel[i] * self.timestep
        return self.pos

    def getKinetic(self):
        """Returns the kinetic energy of the objects."""
        for i in range(self.objects):
            self.kinetic[i] = ((0.5 * self.mass[i])
                               * (np.linalg.norm(self.vel[i])) ** 2.0)
        return np.sum(self.kinetic)

    def anim_init(self):
        return self.patches

    def animate(self, frame):
        """Runs the various update methods needed for the animation."""
        self.getForce()
        self.getAccel()
        self.vel_step()
        self.pos_step()
        for i in range(self.objects):
            self.patches[i].center = (self.pos[i][0], self.pos[i][1])
        # Updates energy plot
        self.time.append(frame * self.timestep)
        self.energy.append(self.getKinetic())
        self.patches[self.objects].set_xdata(self.time)
        self.patches[self.objects].set_ydata(self.energy)
        #print(f't: {self.time} energy: {self.energy}')
        return self.patches

    def show(self, total_frames):
        """Setup and display the animation."""
        # Figure setup
        plt.style.use("dark_background")
        fig = plt.figure()
        # plt.tight_layout(h_pad=2)
        plt.subplots_adjust(wspace=0.5)

        # Axes setup
        #ax = plt.axes(label="anim")
        ax = fig.add_subplot(1, 2, 1, label="anim")
        ax.set_aspect("equal")
        ax.set_title("Orbital Motion")
        # Ensures planets fit in plot.
        r_max = self.pos[self.objects-1][0] * 1.3
        ax.set_xlim(-r_max, r_max)
        ax.set_ylim(-r_max, r_max)

        # Kinetic energy plot
        ax1 = fig.add_subplot(1, 2, 2, label="energy")
        ax1.set_title("Kinetic Energy")
        ax1.plot(self.time, self.energy)
        ax1.set_ylim(2.5E22, 2.65E22)
        time_max = self.timestep * total_frames
        ax1.set_xlim(0, time_max)
        ax1.set_xlabel("Time / s")
        ax1.set_ylabel("Kinetic Energy / J")
        # Ensures energy plot uses scientific notation (numbers are large)
        plt.Axes.ticklabel_format(ax1, style="scientific", scilimits=(-5, 3))

        # Patches setup
        for i in range(self.objects):
            self.patches.append(
                plt.Circle(
                    (self.pos[i][0], self.pos[i][1]),
                    radius=self.radius[i],
                    color=self.color[i],
                    animated=True,
                )
            )
            ax.add_patch(self.patches[i])

        # Add a 2D line to plot the kinetic energy of the planetary objects
        self.patches.append(Line2D([], [], color='red', linewidth=2.5,
                                   animated=True))
        ax1.add_line(self.patches[self.objects])

        anim = FuncAnimation(
            fig,
            self.animate,
            frames=total_frames,
            init_func=self.anim_init,
            repeat=False,
            interval=50,
            blit=True,
        )

        # plt.show()

        anim.save("mars.gif", writer="imagemagick", fps=30)


orbits = Orbit("marsandmoons.csv", 86)
Orbit.show(orbits, 400)
# print(Orbit.getKinetic(orbits))
print("Kinetic Energy")
print(Orbit.getKinetic(orbits))
# print('Accels')
# print(Orbit.getAccel(orbits))
# print('Vels')
# print(Orbit.vel_step(orbits))
# print('Pos_update')
# print(Orbit.animate(orbits))
# print('Pos_update2')
# print(Orbit.animate(orbits))
