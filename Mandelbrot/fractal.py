import numpy as np
import matplotlib.pyplot as plt


class Fractal:

    iter_max = 255
    z_max = 4.0

    def __init__(self, z_init=None):
        if z_init is None:
            self.z_init = np.complex(0, 0)
        else:
            self.z_init = z_init

    @classmethod
    def setIterMax(cls, iter_max):
        cls.iter_max = iter_max

    @classmethod
    def setZMax(cls, z_max):
        cls.z_max = z_max

    def mandelbrot(self, c_number):
        """ Returns numbers that are within the Mandelbrot set

        """
        iters = 0
        z = self.z_init
        while iters < self.iter_max and abs(z)**2.0 < self.z_max:
            z = (z)**2.0 + c_number
            iters += 1
        return iters


class Mandelbrot(Fractal):

    def __init__(self, real_start, real_end, im_start, im_end, resolution):
        super().__init__()
        self.real_val = np.linspace(real_start, real_end, num=resolution)
        self.imag_val = np.linspace(im_start, im_end, num=resolution)
        self.res = resolution

    def display(self):

        real, imag = np.meshgrid(self.real_val, self.imag_val)
        c_number = real + imag*1j
        mandel_set = np.empty((self.res, self.res), dtype=int)
        for i, array in enumerate(c_number):
            for j, val in enumerate(array):
                mandel_set[i][j] = super().mandelbrot(val)

        plt.style.use('dark_background')
        plt.xlabel('Real')
        plt.ylabel('Imaginary')
        plt.title('Mandelbrot Set')

        plt.pcolormesh(real, imag, mandel_set, cmap='inferno')
        plt.colorbar()

        plt.show()


# class Julia(Fractal):
#
#    def __init__(self, c_number):
#        self.c_number = c_number
#        self.z_init = np.linsp
