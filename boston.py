# read json from URL and print the data
import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)


