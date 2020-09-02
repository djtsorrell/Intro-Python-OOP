import numpy as np
import matplotlib.pyplot as plt


class Mandelbrot:

    iter_max = 255
    z_max = 4.0

    def __init__(self, reals, imags, res, z_init=None):
        real_val = np.linspace(reals[0], reals[1], num=res)
        imag_val = np.linspace(imags[0], imags[1], num=res)

        self.real, self.imag = np.meshgrid(real_val, imag_val)
        self.c_number = self.real + self.imag*1j
        self.mandel_set = np.empty((res, res), dtype=int)

        if z_init is None:
            self.z_init = np.complex(0, 0)
        elif z_init == 'range':
            self.z_init = self.real + self.imag*1j
        else:
            self.z_init = z_init

    @classmethod
    def setIterMax(cls, iter_max):
        cls.iter_max = iter_max

    @classmethod
    def setZMax(cls, z_max):
        cls.z_max = z_max

    def mandelbrot(self, c_number, z_input):
        """ Returns numbers that are within the Mandelbrot set

        """
        iters = 0
        z = z_input
        while iters < self.iter_max and abs(z)**2.0 < self.z_max:
            z = (z)**2.0 + c_number
            iters += 1
        return iters

    def getMandelSet(self):
        z_input = self.z_init
        for i, array in enumerate(self.c_number):
            for j, val in enumerate(array):
                self.mandel_set[i][j] = self.mandelbrot(val, z_input)
        return self.mandel_set, self.real, self.imag

    def display(self, real, imag, mandel_set):
        plt.style.use('dark_background')
        plt.xlabel('Real')
        plt.ylabel('Imaginary')

        plt.pcolormesh(real, imag, mandel_set, cmap='inferno', shading='auto')
        plt.colorbar()

        plt.show()


class Julia(Mandelbrot):

    def __init__(self, reals, imags, resolution, c_number):
        super().__init__(reals, imags, resolution, z_init='range')
        self.c_number = c_number

    def getJuliaSet(self):
        for i, array in enumerate(self.z_init):
            for j, val in enumerate(array):
                self.mandel_set[i][j] = super().mandelbrot(self.c_number, val)
        return self.mandel_set, self.real, self.imag

    def display(self, real, imag, mandel_set):
        super().display(real, imag, mandel_set)
