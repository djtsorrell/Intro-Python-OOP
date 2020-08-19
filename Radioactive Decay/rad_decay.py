import random

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Patch


class Decay:
    """A class to simulate radioactive decay

    Parameters
    ----------
    decay_const : float
        The decay constant of the instance (isotope) given in min^{-1}.

    time_step : float
        A time interval. This should be small compared to the average lifetime of the isotope.

    number : int
        The length of the 2D nuclei array. Since the nuclei array is a square, the number of nuclei
        is given by number*number.

    Attributes
    ----------
    nuclei : numpy array
        A 2D (square) numpy array to hold the state of the nuclei. Decayed = 0; not-decayed = 1.
        Initially set to all ones (all undecayed).

    prob : float
        The probability of any one nucleus decaying.

    iters : int
        The number of iterations of the while loop used in the decay_sim algorithm.

    """

    def __init__(self, decay_const, time_step, number):
        self.decay_const = decay_const
        self.time_step = time_step
        self.nuclei = np.ones((number, number), dtype=int)
        self.prob = decay_const*time_step
        self.iters = 0

    def decay_sim(self):
        """Implements the radioactive decay algorithm.

        The decay algorithm works as follows:
        > Scans the entire array
        > Generate a critical value as a random float between 0 and 1
        > If a nucleus has decayed (cell == 0), ignore it
        > If it has not decayed (cell == 1), compare the decay probability to the critical value
        > If the probability is greater than the critical value, that nucleus decays (i.e. set the
        cell to zero)
        > Repeat the above until half of the nuclei have decayed (i.e. until half-life reached)

        """
        counter = 0  # Counts how many nuclei have decayed.
        while counter < (np.size(self.nuclei)/2):
            self.iters += 1
            for cell in np.nditer(self.nuclei, op_flags=['readwrite']):
                crit_val = random.random()
                if cell[...] == 0:
                    pass
                elif crit_val < self.prob:  # Condition for a decay.
                    cell[...] = 0
                    counter += 1

    def half_life_sim(self):
        """Returns the simulated half-life for the isotope instance.

        """
        return self.iters*self.time_step

    def half_life_calc(self):
        """Returns the calculated half-life for the isotope instance.

        """
        return round((0.693/self.decay_const), 3)

    def visual(self):
        """Creates a colour map of the nuclei, showing which have decayed.

        """
        plt.style.use('classic')

        plt.title('Radioactive Nuclei')

        colors = ['dodgerblue', 'crimson']
        plt.pcolormesh(self.nuclei, edgecolors='w', linewidth=0.01,
                       cmap=LinearSegmentedColormap.from_list('', colors))

        ax = plt.gca()
        ax.set_aspect('equal')

        # Set-up the legend so that the nucleus state is defined by a colour.
        legend_elements = [Patch(facecolor=color, edgecolor='w')
                           for color in colors]
        ax.legend(handles=legend_elements,
                  labels=['decayed', 'not-decayed'],
                  loc='upper left', bbox_to_anchor=[1.02, 1])
        plt.tight_layout(pad=4)

        plt.show()
