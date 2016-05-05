# Safe Cycle
Safe Cycle is the 1st place winning project our team created in less than 24 hours for the 2016 Melbourne Data Science Challenge, sponsored by Microsoft and Azure ML.

Take a look at the project here: http://safecycle.xyz/

## Overview
Safe Cycle is a web app that tries to create safer routes for cyclists. The approach we took uses Azure ML, Google Maps and some Python scripts with an HTML jQuery driven front end. Data related to past crashes and the time of day is used to try and avoid danger hot spots on a cyclist's journey, with room for additional data such as weather and traffic to be taken into account. The project was inspired by a cycling injury I had sustained where I fell off my bike and broke my collarbone (for which I was getting surgery the next morning), check it out [here!](https://www.dropbox.com/sh/4ojal2l0ha7kf3r/AAC_VnPk-99WFY5O_PDhui3Da?dl=0)

### Basic functionality
The app currently exists as a one pager, with core functionality involving user interaction with the Google Maps interface. The user enters an origin and destination and, after waiting for Azure ML to think for a bit, the python script receives risk probabilities for the route. The script then generates a new Google Maps map with the new waypoints which is asynchronously reloaded.

Currently only requests for Canberra can be processed properly as we haven't loaded data for other locations into Azure ML.

### Directory structure
- **web** Contains the all the HTML for the front end, including relevant CSS and Javascript. No images were used, but they would be here too.
- **scripts** Contains the Python scripts that communicate with Azure ML and create the Google Maps request.
- **other** Contains the original template used for the front end (thanks to [Pixelarity!](http://pixelarity.com/)) as well as other unused / old working files.

## Technical implementation details
This diagram loosely explains what happens when a user submits a request for a route map.

![Tech implementation flowchart](https://dl.dropboxusercontent.com/s/enlhio7lhh5msob/2016-05-05%2009.47.01.jpg?dl=0)

### Steps followed in a single transaction

1. User enters origin and destination. This is sent as a GET request to the python script, handler.py.
2. The origin and destination are sent to the Google Maps geolocation service and coordinates are returned.
3. These two sets of coords are passed to the pathFinder function. The function draws an ellipse between these two points, breaks it into a grid and creates a list of coords to check based on this grid.
4. We iterate through this list, using the Azure ML HTML API to get risk probabilities for each point.
5. We sort this list of probabilities and choose the waypoints with this lowest risk.
6. Using the original origin and destination, with the waypoints we have selected, a new link for a Google Maps embed map is created and printed via CGI.
7. This new map is reloaded asynchronously into the webpage using jQuery AJAX.

### Generating a risk probability for a point with Azure ML
![Azure ML workflow](https://dl.dropboxusercontent.com/s/6pucmwj12rvdpkc/2016-05-05%2009.59.36.jpg?dl=0)
- The dataflow in Azure ML



## Viability and growth
This app has room to scale in multiple different ways. Geographical scalability is the first thing that comes to mind. Google Maps already has the ability to geolocate and create maps for most major places across the world, so we would just need to add crash data for these locations worldwide. The accuracy and reliability of these maps can be improved further by incorporating more data into the calculations, such as weather of traffic data. The room for growth here is enormous as data availability is increasing day by day. 

Demand for this app could extend beyond just end user cyclists. Food delivery companies with a fleet of cyclists, for example Deliveroo, could find great value in an app that ensures their cyclists' safety. The app could also obviously be reintegrated into Google Maps itself, since currently all they have for cyclists is the ability to avoid ferries, not danger hotspots.

## More information
Feel free to contact [me](https://github.com/banool) or any of the contributors about the project :)
