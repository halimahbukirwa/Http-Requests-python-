 
# HTTP POST REQUEST
# used when submitting data from an html form or uploading files
# A post request is designed for creating or updating resources 
# And allows larger amounts of resources to be sent in a single request compared to a get request

import requests

payload = {"First Name": "John", "Last Name": "Smith"}

r = requests.post("https://httpbin.org/post" data = payload)

# post is an endpoint set up by httpbin to receive data from a form or a file
# data keyword converts our payload dictionary to send to our url
# the post route on the httpbin is expecting a form or a file in the post request

print(r.text)

# the parameters are not url encoded like in the get request
