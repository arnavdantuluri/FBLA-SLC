import socket    
import json
import requests
import geoip2

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)  

response = requests.get("https://geolocation-db.com/json/.39.110.142.79&position=true").json()

ip = (response['IPv4'])

request_url = "https://geolocation-db.com/jsonp/" + IPAddr
response = requests.get(request_url)
result = response.content.decode()

result = result.split("(")[1].strip(")")

result = json.loads(result)
loc = (result['city'], result['state'])

print(loc)
print(IPAddr)