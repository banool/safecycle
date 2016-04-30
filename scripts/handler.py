#!/usr/bin/python

from urllib import quote
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

    compileMapsRequest(origin, destination, waypoints)

    print(form)


def compileMapsRequest(origin, destination, waypoints):
	base = """
				<div class="row">
					<iframe
					  width="1215"
					  height="750"
					  frameborder="0" style="border:0"
					  src="
			"""

	urlTarget = "https://www.google.com/maps/embed/v1/directions?key="
	key = apiKey

	end = """
						 allowfullscreen>
					</iframe>
				</div>
			"""

	if len(waypoints) == 0:
		request = "&origin=" + quote(origin) + "&destination=" + quote(destination) + "&mode=bicycling"

	finalString = base + urlTarget + key + request + end
	print finalString



entryPoint()

