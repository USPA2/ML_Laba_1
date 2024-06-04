from number31 import Vehicle

class Truck(Vehicle):
    pass


truck1 = Truck(50, 1000)
assert (truck1.max_speed, truck1.mileage) == (50, 1000)

truck2 = Truck(43, 235)
assert (truck2.max_speed, truck2.mileage) == (43, 235)