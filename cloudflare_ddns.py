import requests

from urllib.request import urlopen
import re as r

def getIP():
    d = str(urlopen('http://checkip.dyndns.com/').read())
    return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)

def getPayload(ip, host):
    pl = "{\n  \"content\": \""+ip+"\",\n  \"name\": \""+host+"\",\n  \"type\": \"A\",\n  \"proxied\": false,\n  \"ttl\": 60\n}" 
    return pl

def getUrl(zoneId, recordId):
    url = "https://api.cloudflare.com/client/v4/zones/"+zoneId+"/dns_records/"+recordId
    return url

ip = getIP()

zoneId = ""
recordId = ""
authToken = 'Bearer your-cloudflare-token'
emailId = 'your-cloudflare-email'

host = '*.your-domain.com'

headers = {
  'Content-Type': 'application/json',
  'X-Auth-Email': emailId,
  'Authorization': authToken
}

response = requests.request("PUT", getUrl(zoneId, recordId), headers=headers, data=getPayload(ip, host))
print(response.text)
