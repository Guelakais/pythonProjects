#!usr/bin/env python
from solarSystem3D import SolarSystem, Sun, Planet

solar_system = SolarSystem(400, projection_2d=True)

suns = (
    Sun(solar_system, position=(40, 40, 40), velocity=(6, 0, 6)),
    Sun(solar_system, position=(-40, -40, 40), velocity=(-6, 0, -6)),
)

planets = (
    Planet(
        solar_system,
        10,
        position=(100, 100, 0),
        velocity=(0, 5.5, 5.5),
    ),
    Planet(solar_system,20,position=(0, 0, 0),velocity=(-11, 11, 0),),
    Planet(solar_system,40,position=(50,50,0),velocity=(5,-1, 5),)
)

while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()
    solar_system.draw_all()