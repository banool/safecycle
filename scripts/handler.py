#!/usr/bin/python

import urllib2
import json
import googlemaps
from urllib import quote

import cgitb, cgi
cgitb.enable()

print("Content-Type: text/html\n")

apiKey = "AIzaSyADJzDYaO0we1opZUxxUULc8yFgD1W5nKo"
numWaypoints = 8

# We don't check that the fields weren't blank. That kind of data integrity
# assurance can get thrown out the window in a 24 hour hackathon.
def entryPoint():

    form = cgi.FieldStorage()

    gmaps = googlemaps.Client(apiKey)

    #origin = form["origin"].value
    #destination = form["destination"].value
    origin = "ANU, Canberra"
    destination = "parliament house, canberra"

    originCoords = getCoords(origin, gmaps)
    destinationCoords = getCoords(destination, gmaps)
    #print(originCoords)
    #print(destinationCoords)

    testPoints = pathFinder(originCoords, destinationCoords)

    probs = []
    for point in testPoints:
    	res = float(getAzureProbability(point[0], point[1]))
    	probs.append((point, res))
    	#print(res)
    	#probs.append(float(getAzureProbability(point[0], point[1])))

    # Get 8 lowest waypoints.
    #waypoints = []
    waypoints = sorted(probs, key=lambda x: x[1])[:numWaypoints]

    """
    for i in range(0, len(probs)/3):
    	minimum = sorted(probs[i:i+3], key=lambda x: x[1])[0]
    	waypoints.append(minimum)
    """

    #waypoints = sorted(probs, key=lambda x: x[1])[:numWaypoints]
    
    stringWaypoints = []
    for i in waypoints:
    	stringWaypoints.append(str(i[0][0]) + "," + str(i[0][1]))

    #print(stringWaypoints)
    compileMapsRequest(origin, destination, stringWaypoints)
    #print(stringWaypoints)

    """
    #lats = np.arange(-35.21, -35.27, 0.01)
    #longs = np.arange(149.114, 149.17, 0.01)
    
    latitude = -35.21
    longitude = 149.114

    for i in xrange(0,7):
    	for j in xrange(0,7):
    		print(getAzureProbability(latitude, longitude)
    		latitude += 0.01
    	longitude += 0.01
    """

    #diag
    #print(form)

def pathFinder(A,B):
    # A[] and B[] are long and lat coordinates
    if len(A)!=2 or len(B)!=2:
        return -1

    buf = 0.01
    xmin = min(A[0],B[0]) - buf
    ymin = min(A[1],B[1]) - buf
    xmax = max(A[0],B[0]) + buf
    ymax = max(A[1],B[1]) + buf
    step = (xmax-xmin)/8

    m = (float)(A[1]-B[1])/(float)(A[0]-B[0])
    c = A[1] - m*A[0]

    # y = upper + m * x
    # y = lower + m * x

    C = []
    x = xmin
    while x<xmax:
        if x>xmin+2*step and x<xmax-2*step:
            C.append([x,m*x+(c-buf)])
            C.append([x,m*x+c])
            C.append([x,m*x+(c+buf)])
        else:
            C.append([x,m*x+c])
        x+=step
    return C


def getCoords(address, gmaps):
	
	ret = gmaps.geocode(address, {"country":"au"})
	if len(ret) == 0:
		print "Couldn't geolocate " + address
		return None
	else:
		coords = ret[0]["geometry"]["location"]
		return [coords["lat"], coords["lng"]]


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
		requestParts.append(quote(waypoints[-1]))

		request = "".join(requestParts)



	finalString = base + urlTarget + key + request + end
	print finalString


def getAzureProbability(latitude, longitude):

	data =  {

	        "Inputs": {

	                "input1":
	                {
	                    "ColumnNames": ["long", "lat", "time", "event"],
	                    "Values": [ [ longitude, latitude, "9", "0" ], [ "0", "0", "0", "0" ], ]
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
	    return (json.loads(result)["Results"]["output1"]["value"]["Values"][0][-1])
	except urllib2.HTTPError, error:
	    print("The request failed with status code: " + str(error.code))

	    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
	    print(error.info())

	    print(json.loads(error.read()))                 

entryPoint()

