import sys

from animate import Animate


def main():
    filename = str(input("Filename (csv): "))
    if ".csv" not in filename:
        sys.exit("Input is not a csv file!")

    while True:
        try:
            timestep = int(input(
                "Note: The time step should be small compared with the orbital"
                " period of the bodies.\n"
                "Time step (s): "
            ))
            break
        except ValueError:
            print("Please insert an integer.")

    while True:
        try:
            total_frames = int(input("Total frames for the animation: "))
            break
        except ValueError:
            print("Please insert an integer")

    animation = Animate(filename, timestep)
    Animate.show(animation, total_frames)


# Good time step for the marsandmoons.csv simulation is 86 seconds.

main()
