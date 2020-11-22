import csv
import requests
import json
import math
import random
from geopy.geocoders import Nominatim
class Session:
    def __init__(self, userinput, distance):
        self.url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
        self.api_key = 'AIzaSyDnsX9Fpb8jvEp7RssX49SF1oGQzqz4ojY'
        self.user_wants_parks = False
        self.user_wants_art = False
        self.desiredLength = int(distance) / 2  # user walks back the way they came
        self.path = []
        self.pathlength = 0  # the walking distance of the generated path
        self.parks = {}
        self.art = {}
        self.userinput = userinput
        self.currentLocation = '1151 Richmond St, London, ON N6A 3K7'
        self.currentX = 0
        self.currentY = 0

    def main(self):
        random.seed(a=None, version=2)
        self.checkInput()
        self.findCoords()

        return self.OptimizedgreedyPlan()

    def findCoords(self):
        geolocator = Nominatim(user_agent="test")
        location = geolocator.geocode(self.currentLocation)
        oldX = self.currentX
        oldY = self.currentY
        try:
            self.currentX = location.longitude
            self.currentY = location.latitude
        except:
            self.currentX = oldX
            self.currentY = oldY

    def checkInput(self):
        if "Parks" in self.userinput:
            self.user_wants_parks = True
            self.readParks()
        if "Art" in self.userinput:
            self.user_wants_art = True
            self.readArt()

    def coorDistance(self, goal, type):  # goal is the address of a park or art
        x1 = self.currentX
        y1 = self.currentY
        if type == 'Park':
            x2 = self.parks[goal][1]
            y2 = self.parks[goal][2]
        else:  # art
            x2 = self.art[goal][1]
            y2 = self.art[goal][2]

        # convert to km
        y1Lat = y1
        y2Lat = y2
        y1 = y1 * 110.574
        y2 = y2 * 110.574
        degrees1 = math.cos(y1Lat) * (180.0 / math.pi)
        degrees2 = math.cos(y2Lat) * (180.0 / math.pi)
        oneDegreeInKM = (111.320 * degrees1)
        oneDegreeInKM2 = (111.320 * degrees2)

        x1 = x1 * oneDegreeInKM
        x2 = x2 * oneDegreeInKM2

        # find distance straight-line
        # distance = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
        # find distance manhattan
        distance = abs(x1 - x2) + abs(y1 - y2)

        return distance  # in KM

    def readParks(self):
        # read in parks data, stores it as a list of address strings
        with open('newParks.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    address = row[0]
                    X = float(row[1])
                    Y = float(row[2])
                    if (address != '') and (X != 0.0):
                        self.parks[address] = [address, X, Y]
                        line_count += 1

    def readArt(self):
        # read in art data, stores it as a list of address strings
        with open('newArt.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    address = row[1]
                    X = float(row[2])
                    Y = float(row[3])
                    if (address != '') and (X != 0.0):
                        self.art[address] = [address, X, Y]
                        line_count += 1

    def calcDist(self, goal):
        # calculate walking distance between two places
        r = requests.get(self.url + 'origins=' + self.currentLocation + '&mode=walking' + '&destinations=' + goal + '&key=' + self.api_key)
        x = r.json()
        # print(x)
        try:
            x["rows"][0]["elements"][0]["distance"]["value"] / 1000
        except:
            # error in reading spreadsheet data, set weighting so point isnt used.
            return 10000000000
        # return the distance only (in metres)
        return x["rows"][0]["elements"][0]["distance"]["value"] / 1000  # /1000 to get km

    def FindNearestCordPark(self):
        distToBeat = 1000000000  # in KM
        nearestPark = ''
        nearestParkx = ''
        nearestParky = ''
        for parkADR, lis in self.parks.items():
            dist = self.coorDistance(parkADR, 'Park')
            if ((dist < distToBeat) and (parkADR not in self.path)):
                nearestPark = parkADR
                nearestParkx = lis[1]
                nearestParky = lis[2]
                distToBeat = dist
        # all parks searched
        self.pathlength += self.calcDist(nearestPark)
        # print(self.pathlength)
        self.path.append(nearestPark)
        self.currentLocation = nearestPark
        self.currentX = nearestParkx
        self.currentY = nearestParky

    def FindNearestCordArt(self):
        distToBeat = 1000000000  # in KM
        nearestArt = ''
        nearestArtx = ''
        nearestArty = ''
        for artADR, lis in self.art.items():
            dist = self.coorDistance(artADR, 'Art')
            if ((dist < distToBeat) and (artADR not in self.path)):
                nearestArt = artADR
                nearestArtx = lis[1]
                nearestArty = lis[2]
                distToBeat = dist
        # all parks searched
        self.pathlength += self.calcDist(nearestArt)
        # print(self.pathlength)
        self.path.append(nearestArt)
        self.currentLocation = nearestArt
        self.currentX = nearestArtx
        self.currentY = nearestArty

    def OptimizedgreedyPlan(self):
        # trying the greedyplanner, but calculates closest goal using coordinates
        self.path.append(self.currentLocation)  # adds the start address
        if (self.user_wants_parks and not self.user_wants_art):
            while self.pathlength < self.desiredLength:
                self.FindNearestCordPark()
        elif (self.user_wants_art and not self.user_wants_parks):
            while self.pathlength < self.desiredLength:
                self.FindNearestCordArt()
        else:  # user wants both parks and art
            while self.pathlength < self.desiredLength:
                variance = random.randint(0, 100)
                if variance <= 75:
                    self.FindNearestCordPark()
                else:
                    self.FindNearestCordArt()

            pass

        return self.path

    # def feedback(self):
    #     # most visited destinations
    #     pass


# print(Session(["Parks"], "30").main())
# print(Session(["Art"], "30").main())
# print(Session(["Art", "Parks"], "30").main())
# print(Session(["Art", "Parks"], "30").main())
# print(Session(["Parks"], "7").main())
