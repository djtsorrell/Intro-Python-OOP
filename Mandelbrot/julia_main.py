from mandelbrot import Julia

reals = (-2.025, 0.6)
imags = (-1.125, 1.125)

while True:
    try:
        c_number = complex(input('Enter a complex number: '))
        break
    except ValueError:
        print('Input was not a complex number (x + yj)')
fractal = Julia(reals, imags, 1000, c_number)
mandel_set, real, imag = Julia.getJuliaSet(fractal)
Julia.display(fractal, real, imag, mandel_set)
