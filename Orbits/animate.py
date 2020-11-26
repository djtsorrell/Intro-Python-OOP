import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D

from orbit import Orbit


class Animate(Orbit):

    """Initialises patches to visualise orbital motion."""

    def __init__(self, filename, timestep):
        """TODO: to be defined. """
        super().__init__(filename, timestep)
        # Initialises the objects to be animated.
        self.patches = []
        # Initialises data lists for plotting kinetic energy.
        self.time = []
        self.energy = []

    def anim_init(self):
        return self.patches

    def animate(self, frame):
        """Updates the positions of the bodies and the energy data"""
        # Runs the update methods for all physical attributes.
        super().getForce()
        super().getAccel()
        super().vel_step()
        super().pos_step()

        # Updates the positions of the planetary objects.
        for i in range(self.objects):
            self.patches[i].center = (self.pos[i][0], self.pos[i][1])

        # Updates energy plot.
        self.time.append(frame * self.timestep)
        self.energy.append(super().getKinetic())
        self.patches[self.objects].set_xdata(self.time)
        self.patches[self.objects].set_ydata(self.energy)

        return self.patches

    def show(self, total_frames):
        """Setup and display the animation."""
        # Figure setup.
        plt.style.use("dark_background")
        fig = plt.figure()
        # Add extra horizontal space between subplots.
        plt.subplots_adjust(wspace=0.5)

        # Axes setup for planetary bodies.
        ax = fig.add_subplot(1, 2, 1, label="planets")
        ax.set_aspect("equal")
        ax.set_title("Orbital Motion")
        # Ensures planets fit in axes.
        r_max = self.pos[self.objects-1][0] * 1.3
        ax.set_xlim(-r_max, r_max)
        ax.set_ylim(-r_max, r_max)

        # Axes setup for energy plot.
        ax1 = fig.add_subplot(1, 2, 2, label="energy")
        ax1.set_title("Kinetic Energy")
        ax1.set_ylim(2.5E22, 2.65E22)  # based off expected values for energy.
        x_max = self.timestep * total_frames  # i.e. the total duration.
        ax1.set_xlim(0, x_max)
        ax1.set_xlabel("Time / s")
        ax1.set_ylabel("Kinetic Energy / J")
        # Ensures energy plot uses scientific notation (numbers are large).
        plt.Axes.ticklabel_format(ax1, style="scientific", scilimits=(-5, 3))

        # Adds the planets to the patches list which will then be animated.
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

        # Add a 2D line to plot the kinetic energy of the planetary objects.
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

        plt.show()

        # anim.save("mars.gif", writer="imagemagick", fps=30)
