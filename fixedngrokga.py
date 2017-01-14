#!/usr/local/bin/python3
import requests
import json
import sys

# EDIT THIS #

bag_id = ""
authtoken = ""


class Req:
	content = b'{"tunnels":[],"uri":"/api/tunnels"}'

r = Req()

while len(json.loads(r.content.decode("utf-8"))['tunnels']) is 0:
	r = requests.get('http://localhost:4040/api/tunnels')

content = json.loads(r.content.decode("utf-8"))
url = content['tunnels'][0]['public_url']
print("URL is: "+url)
r = requests.get('http://fixedngrok.ga/'+bag_id+'&authtoken='+authtoken+'&value='+url)
print("fixedngrokga bag updated.")

sys.exit(0)
