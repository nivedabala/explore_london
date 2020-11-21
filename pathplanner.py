import urllib.request
import csv
endpoint = 'https://maps.googleapis.com/maps/api/diractions/json?'
api_key = ''
current_location = '111 Wharncliffe Rd S, London, ON N6J 2K2'
user_wants_parks = True
user_wants_art = True
user_wants_trees = True
total_distanceKM = 5
destinations = []
