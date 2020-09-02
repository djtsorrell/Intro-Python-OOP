from mandelbrot import Mandelbrot as Mandel

reals = (-2.025, 0.6)
imags = (-1.125, 1.125)
fractal = Mandel(reals, imags, 1000)
mandel_set, real, imag = Mandel.getMandelSet(fractal)
Mandel.display(fractal, real, imag, mandel_set)
