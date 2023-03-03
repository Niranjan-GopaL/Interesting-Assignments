class Vehicle:
    def __init__(self, name, maxSpeed, seatingCapacity, mileage):
        self.name = name
        
    '''        
        self.maxSpeed = maxSpeed
        self.seatingCapacity = seatingCapacity
        self.mileage = mileage
    '''
    def fare(self):
        return self.seatingCapacity * 200


class Bus(Vehicle):
    def __init__(self, name, maxSpeed, seatingCapacity, mileage):
        super().__init__(name, maxSpeed, seatingCapacity, mileage)
  
    def fare(self):
        fare = super().fare()
        return fare + (fare * 0.05)

vehicles = []

while True:
    line = input().split()
    if line[0] == 'E':
        break

    name = line[0]
    maxSpeed, seatingCapacity, mileage = list(map(int,line[1:]))


    '''    
    vehicle = Bus(name, maxSpeed, seatingCapacity, mileage)
    vehicles.append(vehicle)
    '''

for vehicle in vehicles:
    print(vehicle.name, int(vehicle.fare()))

    '''
    name,maxSpeed, seatingCapacity, mileage = line
    maxSpeed = int(maxSpeed)
    seatingCapacity = int(seatingCapacity)
    mileage = int(mileage)
    '''

    