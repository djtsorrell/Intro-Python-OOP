from rad_decay import Decay


def main():
    isotope = Decay(0.02775, 0.01, 50)
    Decay.decay_sim(isotope)
    print(f'Half-life (sim) = {Decay.half_life_sim(isotope)} min')
    print(f'Half-life (calc) = {Decay.half_life_calc(isotope)} min')
    Decay.visual(isotope)


main()
