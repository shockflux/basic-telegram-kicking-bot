# importing the requests library
import requests
 
# api-endpoint
URL = "https://api.telegram.org/<bot token number>/kickChatMember"
 
# location given here
location = "<location>"
 
# defining a params dict for the parameters to be sent to the API
chat_id=<chat id>
user_id=<user id>
PARAMS = {'chat_id':chat_id,'user_id':user_id}

 
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
 
# extracting data in json format
data = r.json()
 
 
# extracting latitude, longitude and formatted address 
# of the first matching location
#latitude = data['results'][0]['geometry']['location']['lat']
#longitude = data['results'][0]['geometry']['location']['lng']
#formatted_address = data['results'][0]['formatted_address']
 
# printing the output
#print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
 #     %(latitude, longitude,formatted_address))
