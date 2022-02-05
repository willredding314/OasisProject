
import json
import requests 
#need to install -- pip3 install requests 
#use as requests.get("url")

################################
#             TMDB             #
#                              #
# user: oasisproj13            #
# pw: oasis                    #
# setup through will's email   #
#                              #
################################


api_key = "k_rxh9t80o"

f = open("sampleData.json")
sampleData = json.load(f)
top250 = sampleData["items"]



