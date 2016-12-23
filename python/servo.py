#!/usr/bin/env python
#auhor ME...

from nanpy import (Servo, Arduino)
from pprint import pprint
import requests, json

#Set up servo objects for lines
redLine = Servo(9)
yellowLine = Servo(8)
blueLine = Servo(7)
greenLine = Servo(6)
orangeLine = Servo(5)

#Lists to hold lines and affected lines to compare later
masterLinesAffectedList = []
masterLinesList = {
	'RD' : redLine,
	'YL' : yellowLine, 
	'BL' : blueLine,
	'GR' : greenLine,
	'OR' : orangeLine,
}

#Angles for pictures
notDelayedAngle = 90
delayedAngle = 45

#API
def getAPIData():
	apiKey = 'wenc7pxhr3am78e47u8h2x83'
	url = 'http://api.wmata.com/Incidents.svc/json/Incidents?api_key=' + apiKey 
	response = requests.get(url)
	data = json.loads(response.text)
	
	for incident in data['Incidents']:
		lines = incident['LinesAffected'].split(';')
		for line in lines:
			if not line in masterLinesAffectedList and line != '':
				masterLinesAffectedList.append(line)

#change angles of affected lines servos
def updatePictureAngles():
	for l in masterLinesList.viewkeys() :
		if l in masterLinesAffectedList:
			masterLinesList[l].write(delayedAngle)
		else:
			masterLinesList[l].write(notDelayedAngle)

if __name__ == "__main__":
	getAPIData()
	updatePictureAngles()
