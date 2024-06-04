class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    pass


veh1 = Vehicle(100, 50)
assert (veh1.max_speed, veh1.mileage) == (100, 50)

veh2 = Vehicle(200, 3)
assert (veh2.max_speed, veh2.mileage) == (200, 3)