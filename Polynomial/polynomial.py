from itertools import zip_longest


class Poly:
    """
    A class to represent and manipulate polynomials.

    Parameters
    ----------
    coeff : list of float
        List of coefficients for the polynomial.

    Attributes
    ----------
    coeff : list of float
        List of coefficients for the polynomial.

    """

    def __init__(self, coeff):
        self.coeff = coeff

    def __str__(self):
        # Finds the index of the first non-zero value in the coefficients list.
        idx = next((i for i, val in enumerate(self.coeff) if val != 0), None)
        if idx == 0:
            poly_string = f'{self.coeff[idx]} '
        else:
            poly_string = f'{self.coeff[idx]}x^{idx} '
        for i, val in enumerate(self.coeff[(idx+1):], (idx+1)):
            if val < 0:
                poly_string += f'- {abs(val)}x^{i} '
            elif val and i != 0:
                poly_string += f'+ {val}x^{i} '
        return 'P(x) = ' + poly_string

    def __add__(self, other):
        return Poly([sum(i) for i in zip_longest(self.coeff, other.coeff, fillvalue=0)])

    def order(self):
        """Returns the order of the polynomial.

        """
        return len(self.coeff)-1

    def deriv(self):
        """Returns the derivative of the polynomial.

        """
        poly_deriv = []
        for i, val in enumerate(self.coeff):
            poly_deriv.append(i*val)
        # Removes the differentiated constant (which is always 0).
        del poly_deriv[0]
        return Poly(poly_deriv)

    def anti_deriv(self):
        """Returns the integral of the polynomial.

        """
        poly_anti_deriv = [0]
        for i, val in enumerate(self.coeff):
            poly_anti_deriv.append(round(val/(i+1.0), 2))
        return Poly(poly_anti_deriv)
