import csv, requests, json
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
api_key = 'AIzaSyDnsX9Fpb8jvEp7RssX49SF1oGQzqz4ojY'
start_location = '111 Wharncliffe Rd S, London, ON N6J 2K2'
user_wants_parks = True
user_wants_art = True
user_wants_trees = True
return_to_start = True
total_distanceKM = 5
destinations = []
#testing
dest = '378 Horton St E, London, ON N6B 1L7'

def calcDist():
    # calculate distance between two places
    r = requests.get(url + 'origins=' + start_location + '&mode=walking' +
                   '&destinations=' + dest +
                   '&key=' + api_key)
    x = r.json() 
    print(x)


# def parks():
#     # read in parks data

# def art():
#     # read in art data

# def sortParks():
#     # find nearest parks

# def sortArt():
#     # find nearest art

# TESTING
calcDist()