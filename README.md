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

## Viability and growth

## More information
Feel free to contact [me](https://github.com/banool) or any of the contributors about the project :)
