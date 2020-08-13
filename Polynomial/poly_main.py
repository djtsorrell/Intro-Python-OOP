from polynomial import Poly


def main():
    """Main function to test Poly class.

    """
    coeff = Poly([2, 0, 4, -1, 0, 6])
    coeff2 = Poly([-1, -3, 0, 4.5])
    print('P_a: ', coeff, ' Order = ', Poly.order(coeff))
    print('P_b: ', coeff2, ' Order = ', Poly.order(coeff2))
    print('P_a + P_b: ', coeff + coeff2)
    print('Diff P_a: ', Poly.deriv(coeff))
    print('Diff P_b: ', Poly.deriv(coeff2))
    print('Integral P_a: ', Poly.anti_deriv(coeff))
    print('Integral P_b: ', Poly.anti_deriv(coeff2))


main()
