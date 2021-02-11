from animate import Animate


def main():
    """Test the simulation with Mars and its moons."""
    anim = Animate('marsandmoons.csv', 86)
    anim.show(500)


main()
