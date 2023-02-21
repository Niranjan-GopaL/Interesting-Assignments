class Taxi:
    def __init__(self, rateCard, taxiAgencyDetails):
        self.rateCard = rateCard
        self.taxiAgencyDetails = taxiAgencyDetails

class MicroTaxi(Taxi):
    pass

class MiniTaxi(Taxi):
    pass

class SedanTaxi(Taxi):
    pass

class Ride:
    def __init__(self, vehicleType, travelDistance):
        self.vehicleType = vehicleType
        self.travelDistance = travelDistance

    @property
    def fare(self):
        if isinstance(self.vehicleType, MicroTaxi):
            rate = self.vehicleType.rateCard['micro']
        elif isinstance(self.vehicleType, MiniTaxi):
            rate = self.vehicleType.rateCard['mini']
        elif isinstance(self.vehicleType, SedanTaxi):
            rate = self.vehicleType.rateCard['sedan']
        else:
            raise ValueError('Invalid vehicle type')

        if self.travelDistance < 0:
            raise ValueError('Travel distance cannot be negative')

        return rate * self.travelDistance
