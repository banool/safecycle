#!/usr/bin/python

import cgitb, cgi
cgitb.enable()

print("Content-Type: text/html\n")

print("""
									<div class="row">
										<iframe
										  width="1215"
										  height="750"
										  frameborder="0" style="border:0"
										  src="https://www.google.com/maps/embed/v1/directions?key=AIzaSyADJzDYaO0we1opZUxxUULc8yFgD1W5nKo
										    &origin=8+first+court+preston,3072
										    &destination=Ivanhoe
										    &waypoints=Museum+of+Melbourne
										    &mode=bicycling" allowfullscreen>
										</iframe>
									</div>
""")

