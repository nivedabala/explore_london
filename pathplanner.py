import csv, requests, json
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
api_key = 'AIzaSyDnsX9Fpb8jvEp7RssX49SF1oGQzqz4ojY'
user_wants_parks = True
user_wants_art = True
user_wants_trees = True
return_to_start = True
total_distanceKM = 5
destinations = []
art = {}
parks = []
#testing
dest = '378 Horton St E, London, ON N6B 1L7'
start_location = '111 Wharncliffe Rd S, London, ON N6J 2K2'

def calcDist():
    # calculate distance between two places
    r = requests.get(url + 'origins=' + start_location + '&mode=walking' +
                   '&destinations=' + dest +
                   '&key=' + api_key)
    x = r.json() 
    print(x)


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
        print("file had %d lines" % line_count)
        print(parks)

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
        print("file had %d lines" % line_count)
        print(art)

# def sortParks():
#     # find nearest parks

# def sortArt():
#     # find nearest art

# def plan():
#     # create plan until path length = desired length


# def feedback():
#     # most visited destinations


# TESTING
#calcDist()
readParks(parks)
readArt(art)