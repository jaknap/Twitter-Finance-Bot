import urllib2
import json

response = urllib2.urlopen('https://www.kimonolabs.com/api/XXXX')
data = json.load(response)
#print data


d= data["results"]["collection1"][0]["property3"]
