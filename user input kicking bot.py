chat_id=<chat id>
    
import json

import os.path

import sys

import requests



try:

    import apiai

except ImportError:

    sys.path.append(

        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)

    )

    import apiai



CLIENT_ACCESS_TOKEN = '<client access token>'



with open('data.json') as json_data:
    d = json.load(json_data)
    #print(d)
    print("-------------------------")
    #print(len(d))

#for i in range(len(d)):
hey=input("Enter the person to be kicked")


ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)



request = ai.text_request()



request.lang = 'en'  # optional, default value equal 'en'



request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"



request.query = hey



response = json.load(request.getresponse())

kickname = response['result']['parameters']['name']

print (kickname)


for i in range(len(d)):
    find=d[i]["message"]["from"]["first_name"]
    
    #print(find)
    
    
    if find.lower()==kickname.lower():
        print ('')
        #kick:\n\t','ID:',d[i]["message"]["from"]["id"]
        
        
        user_id=d[i]["message"]["from"]["id"]
        



    
# api-endpoint
URL = "https://api.telegram.org/bot<bot token>/kickChatMember"
 
# location given here
location = "<location>"
 
# defining a params dict for the parameters to be sent to the API

PARAMS = {'chat_id':chat_id,'user_id':user_id}

 
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
 
# extracting data in json format
data = r.json()

print("removed")
 

        
