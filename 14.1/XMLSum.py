import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as et
import ssl


# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

total = 0

url = input("Enter XML file location: ")
#print(url)

data = urllib.request.urlopen(url.strip(), context=ctx).read()

print(data.decode())

tree = et.fromstring(data)

results = tree.findall("comments/comment")

for result in results:

    if result is not None:
        total += int(result.find('count').text)

print(total)