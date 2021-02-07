# name: Stephen Wang
# date: November 7, 2020
# purpose: City class

class City:
    def __init__(self, code, name, region, population, latitude, longtitude):
        self.code = code
        self.name = name 
        self.region = region
        self.population = int(population)
        self.latitude = float(latitude)
        self.longtitude = float(longtitude)
    
    def __str__(self):
        return self.name + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longtitude)
    



    