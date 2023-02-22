# Define a Taxi class that takes rate card and agency details as input
class Taxi:
    def __init__(self, rateCard, taxiAgencyDetails):
        self.rateCard = rateCard
        self.taxiAgencyDetails = taxiAgencyDetails

# Define a MicroTaxi class that inherits from Taxi class
class MicroTaxi(Taxi):
    pass    

#MiniTaxi class that inherits from taxi class
class MiniTaxi(Taxi):
    pass

#SedanTaxi class that inherits from Taxi class
class SedanTaxi(Taxi):
    pass

#Ride class that takes vehicle type and travel distance as input
class Ride:
    def __init__(self, vehicleType, travelDistance):
        self.vehicleType = vehicleType
        self.travelDistance = travelDistance

    #function to calculate the fare based on the vehicle type and travel distance
    def Fare(self):
        if(self.vehicleType == "MicroTaxi"):
           fare=MicroTaxi(rateCard[0], x[0])
           return rateCard[0]*self.travelDistance

        if(self.vehicleType=="MiniTaxi"):
            fare = MicroTaxi(rateCard[1], x[0])
            return rateCard[1] * self.travelDistance

        if (self.vehicleType == "SedanTaxi"):
            fare = MicroTaxi(rateCard[2], x[0])
            return rateCard[2] * self.travelDistance

rateCard=list(map(int,input().split()))

#number of test cases
n=int(input())
obj_taxi = []
obj_taxi_name = []

#Loop through each test case and populate obj_taxi and obj_taxi_name
for i in range(n):
    x=input().split()
    obj_taxi.append(Ride(x[1], int(x[2])))
    obj_taxi_name.append(x[0])  

#To leave a line between input and output
print()

# Output loop
for i in range(n):
    print(obj_taxi_name[i], obj_taxi[i].Fare())



'''
Sample Input
10 12 15
4
Ola1 MicroTaxi 26
Uber1 MicroTaxi 13
Ola2 SedanTaxi 10
Uber2 MiniTaxi 20


Sample Output : 
Ola1 260
Uber1 130
Ola2 150
Uber2 240
'''