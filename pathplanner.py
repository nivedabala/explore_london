import csv
import requests
import json
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
api_key = 'AIzaSyDnsX9Fpb8jvEp7RssX49SF1oGQzqz4ojY'
user_wants_parks = True
user_wants_art = True
user_wants_trees = True
return_to_start = True
total_distanceM = 10000
first_park_dist_threshold = 5000  # this is the max acceptable distance for the first park
path = []
art = {}
parks = []
# TESTING
goal = '378 Horton St E, London, ON N6B 1L7'
start = '111 Wharncliffe Rd S, London, ON N6J 2K2'
# ONE TIME USE
numClosestParks = 3  # number of closest parks to find for each park (walking distance)


def calcDist(start, goal):
    # calculate walking distance between two places
    r = requests.get(url + 'origins=' + start + '&mode=walking' + '&destinations=' + goal + '&key=' + api_key)
    x = r.json()
    # print(x)
    # return the distance only (in metres)
    return x["rows"][0]["elements"][0]["distance"]["value"]  # /1000 to get km

def readParks(parks):
    # read in parks data
    with open('Parks.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                # add address to parks[]
                parks.append(row[2])
                line_count += 1
        # print("file had %d lines" % line_count)
        # print(parks)

def readArt(art):
    # read in art data
    with open('Public_Art.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                # add name and address to art{}
                art[row[3]] = row[5]
                line_count += 1
        # print("file had %d lines" % line_count)
        # print(art)

def findFirstPark(parks, threshold, start_location):
    # finds the first park in list that is in acceptable threshold
    # returns the address of the park
    # this may be very time consuming/costly (lots of api calls), use sparingly
    for park in parks:
        if calcDist(start_location, park) <= threshold:
            return park
    return("no parks within threshold")

def findNearestArt(art, start):
    distanceToBeat = 100000000
    for a in art:
        dist = calcDist(start, a)
        if dist <= distanceToBeat:
            nearestArt = a
            distanceToBeat = dist

    return nearestArt

def closestParks(X, parks):
    # RUN ONCE TO GENERATE SPREADSHEET (lots of api calls)
    # Finds the X closest parks to each park
    # Finds the distance between the found parks and the OG park
    return

def plan(path, wantsArt, wantsTrees, desiredLength, start, parks, art, threshold):
    # returns an ordered list of locations
    # plans until pathLength == desiredLength

    # find first park or art depending on choices and start location
    # if both are selected, choose closeset one
    if (wantsArt and wantsTrees):
        # find a park within threshold
        firstPark = findFirstPark(parks, threshold, start)
        # find the nearest art
        firstArt = findNearestArt(art, start)
        if calcDist(start, firstPark) > calcDist(start, firstArt):
            path.append(firstArt)
        else:
            path.append(firstPark)
    elif (wantsArt and not wantsTrees):
        # find the nearest art
        firstArt = findNearestArt(art, start)
        path.append(firstArt)
    elif (not wantsArt and wantsTrees):
        # find a park within threshold
        firstPark = findFirstPark(parks, threshold, start)
        path.append(firstPark)

    return path

# def feedback():
#     # most visited destinations

# TESTING
# print(calcDist(start, goal))
# readParks(parks)
# readArt(art)

# TESTING
# if __name__ == "__main__":
#     calcDist()
#     readParks(parks)
#     readArt(art)
