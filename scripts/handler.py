#!/usr/bin/python

import urllib2
import json 
from urllib import quote
#import numpy as np

import cgitb, cgi
cgitb.enable()

print("Content-Type: text/html\n")

apiKey = "AIzaSyADJzDYaO0we1opZUxxUULc8yFgD1W5nKo"


# We don't check that the fields weren't blank. That kind of data integrity
# assurance can get thrown out the window in a 24 hour hackathon.
def entryPoint():

    form = cgi.FieldStorage()

    origin = form["origin"].value
    destination = form["destination"].value
    waypoints = []

    #compileMapsRequest(origin, destination, waypoints)

    #lats = np.arange(-35.21, -35.27, 0.01)
    #longs = np.arange(149.114, 149.17, 0.01)

    latitude = -35.21
    longitude = 149.114

    for i in xrange(0,7):
    	for j in xrange(0,7):
    		getAzureData(latitude, longitude)
    		latitude += 0.01
    	longitude += 0.01

    for i in lats:
    	for j in longs:
    		getAzureData(i, j)

    

    #diag
    #print(form)


def compileMapsRequest(origin, destination, waypoints):
	base = """
				<div class="row">
					<iframe
					  width="1215"
					  height="675"
					  frameborder="0" style="border:0"
					  src='
			"""

	urlTarget = "https://www.google.com/maps/embed/v1/directions?key="
	key = apiKey

	end = """
						&mode=bicycling' allowfullscreen>
					</iframe>
				</div>
			"""

	if len(waypoints) == 0:
		request = "&origin=" + quote(origin) + "&destination=" + quote(destination)
	else:
		requestParts = []
		# Build base request again.
		requestParts.append("&origin=")
		requestParts.append(quote(origin))
		requestParts.append("&destination=")
		requestParts.append(quote(destination))
		requestParts.append("&waypoints=")
		# Add waypoints
		for wp in waypoints[:-1]:
			requestParts.append(quote(wp))
			requestParts.append("|")
		# Add last one without the pipe.
		requestParts.append(quote(wp))

		request = "".join(requestParts)



	finalString = base + urlTarget + key + request + end
	print finalString


def getAzureData(latitude, longitude):


	data =  {

	        "Inputs": {

	                "input1":
	                {
	                    "ColumnNames": ["long", "lat", "time", "event"],
	                    "Values": [ [ latitude, longitude, "9", "0" ], [ "0", "0", "0", "0" ], ]
	                },        },
	            "GlobalParameters": {
	}
	    }

	body = str.encode(json.dumps(data))

	url = 'https://ussouthcentral.services.azureml.net/workspaces/0188131680ce420794e35a3a48d85416/services/bbc6c1a5e65241b397a0b6e3a52a4a91/execute?api-version=2.0&details=true'
	api_key = 'gkYlkVyl1Z2eA0IZWe/Qr4I/JDT0RsKCHl3ggAaeRKQqQ6ehY4EXgD0yze9NYdOopXPIzKH9bB2h8e5PopOQFA==' # Replace this with the API key for the web service
	headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

	req = urllib2.Request(url, body, headers) 

	try:
	    response = urllib2.urlopen(req)

	    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
	    # req = urllib.request.Request(url, body, headers) 
	    # response = urllib.request.urlopen(req)

	    result = response.read()
	    print(result) 
	except urllib2.HTTPError, error:
	    print("The request failed with status code: " + str(error.code))

	    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
	    print(error.info())

	    print(json.loads(error.read()))                 

entryPoint()

