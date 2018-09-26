from pprint import pprint
import os
import time
import telepot
import json



bot = telepot.Bot("<bot token number")
response = bot.getUpdates('100000001')
time.sleep(2)
pprint(response)

file=open('data1.txt','w')
file.write(str(response))
file.close()






