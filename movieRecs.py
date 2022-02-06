import json
import requests 
#need to install -- pip3 install requests 
#use as requests.get("url")

################################
#             TMDB             
#                              
# user: oasisproj13            
# pw: oasis                    
# setup through will's email: redding.w@northeastern.edu 
#                              
tmdb_api_key = "61927fa19fa76dd5fbeac609493ca3c1"
# read-access-token: eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MTkyN2ZhMT
#                    lmYTc2ZGQ1ZmJlYWM2MDk0OTNjYTNjMSIsInN1YiI6I
#                    jYxZmRmNzgzY2Y0YjhiMDA4Yzc0NDQ3ZiIsInNjb3Bl
#                    cyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.76Kk
#                    uBWyUkVw0h5g2YVwFk1cPgiAc3FLwA7URCraSUc                             
#
################################

imdb_api_key = "k_rxh9t80o"

#imdb data, can get info like:
# - imdb rank -> "rank"
# - title -> "title"
# - release year -> "year"
# - director and leads -> "crew" (is a single string, need to parse)
# - imdb rating -> "imDbRating"
f = open("sampleData.json")
sampleData = json.load(f)
top250 = sampleData["items"]

#details sample, can get info like:
# - genres -> "genres", [index], "name"
# - overview -> "overview"
# - runtime -> "runtime"
response = requests.get("https://api.themoviedb.org/3/movie/tt0111161?api_key=61927fa19fa76dd5fbeac609493ca3c1&language=en-US")

castResponse = requests.get("https://api.themoviedb.org/3/movie/tt0111161/credits?api_key=61927fa19fa76dd5fbeac609493ca3c1&language=en-US")

#requests are often formatted like json, but only text, need json loads

#add change comment
#change number 2