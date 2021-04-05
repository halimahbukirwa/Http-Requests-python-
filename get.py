
#HTTP GET REQUEST
#It is used for retrieving data from a specified resource.
#The content received from a get request can be used for :
#rendering a list of data retrieved from an API
#Filtering a list of products based on a query string
#It should not be used for sensitive information


import requests
          

# payload dictionary
payload = {"First Name": "John", "Last Name": "Smith"}

# declare a response object
r = requests.get("https://httpbin.org/get", params = payload) 

# When the request to the url is made, a response object r will contain information received from the url
# we are using httpbin because it provides us with a quick simple way to send and receive well formatted responses
# from a server
# it acts much as an api from google or twitter
# It is an option to quickly test our http request without needing any authentication
# httpbin.org is a base url and we appended /get which is a route to the end of the base url
# we can also pass url parameters through the request get function
# url parameters are declared as a query string in the url 
# and are a way to dynamically send data to a url (additional information to a page)
# To declare a query string string, a ? is placed after the domain name and path which indicates a query string has started
# followed by parameter names and values
# a value is assigned with an equal sign
# multiple parameters with corresponding values will use an ampersand &
# keyword params converts the payload dictionary into a query string
# that can be sent to the specified url

print (r.url) 
#reveals the full url

print(r.status_code)
# http response code
# 200 indicates a successful request has been made

print(r.content)
# view response content from the url
#returns the response body as bytes

print(r.text)
# view response content from the url
# returns the response body that is decoded by the response library 
# based on the http headers passed in the http request