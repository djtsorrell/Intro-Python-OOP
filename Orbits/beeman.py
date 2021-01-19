import numpy as np
import pandas as pd


class Beeman:

    """Docstring for Beeman. """

    def __init__(self, filename, timestep):
        """TODO: to be defined. """
        self.timestep = timestep
        data = pd.read_csv(filename)
        self.names = np.array(data.Object)
        self.mass = np.array(data.Mass)
        self.radius = np.array(data.Radius)
        self.color = np.array(data.Color)
