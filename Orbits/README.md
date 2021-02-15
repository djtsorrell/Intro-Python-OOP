# Orbital Simulation

A Python simulation of orbital motion. The program uses Euler-Cromer method of
numerical integration to obtain bodies' velocity and position. Gravitational
forces are calculated using Newton's Universal Law of Gravitation. It should be
noted that this is a many-body problem; therefore, the program calculates the
forces and resulting accelerations, velocities and positions for **all** bodies.
Below is one example of the simulation working. Alongside the animation of the
orbital motion, the total energy of the system is plotted. As is clear from the
plot, this simple numerical integration leads to energy **not** being
conserved.

## Mars, Phobos, and Deimos

![Animation](mars.gif?raw=true)
