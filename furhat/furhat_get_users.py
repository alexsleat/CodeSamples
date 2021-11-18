# importing the requests library
import requests
  
# api-endpoint
URL = "http://192.168.0.110:54321/furhat/users"
  
# location given here
text_speech = "beep blorp"
  
# defining a params dict for the parameters to be sent to the API
PARAMS = {'text': text_speech}
  
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)

data = r.json()

print(data) 
