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

f = open("sampleData.json")
sampleData = json.load(f)
top250 = sampleData["items"]

#details sample, can get info like:
# - genres -> "genres", [index], "name"
# - overview -> "overview"
# - runtime -> "runtime"
sampleResponse = requests.get("https://api.themoviedb.org/3/movie/tt0111161?api_key=61927fa19fa76dd5fbeac609493ca3c1&language=en-US")


#gets the genres of a movie from TMDB
def getMovieGenre(imdbID):
    responseBytes = requests.get(f"https://api.themoviedb.org/3/movie/{imdbID}?api_key=61927fa19fa76dd5fbeac609493ca3c1&language=en-US").content
    genresDicts = json.loads(responseBytes)["genres"]
    genres = []
    for item in genresDicts:
        genres.append(item["name"])
    return genres

def getMovieRuntime(imdbID):
    responseBytes = requests.get(f"https://api.themoviedb.org/3/movie/{imdbID}?api_key=61927fa19fa76dd5fbeac609493ca3c1&language=en-US").content
    return json.loads(responseBytes)["runtime"]

#gets the cast of a movie from TMDB
def getMovieCast(imdbID):
    castResponseBytes = requests.get(f"https://api.themoviedb.org/3/movie/{imdbID}/credits?api_key=61927fa19fa76dd5fbeac609493ca3c1&language=en-US").content
    castResponse = json.loads(castResponseBytes)['cast']
    actorsList = []
    for item in castResponse:
        if item["known_for_department"] == "Acting":
            actorsList.append(item['name'])
    return actorsList

############################################
#produces a dictionary of the top 250 movies
#
#current items of importance:
#   id
#   rank
#   title
#   year
#   director
#   cast
#   imDbRating
############################################
def getTop250():
    f = open("sampleData.json")
    sampleData = json.load(f)
    top250 = sampleData["items"]
    
    for item in top250:
        id = item['id']
        actors = getMovieCast(id)
        item["cast"] = actors
        item["director"] = item["crew"].split("(")[0]

        item["genre"] = getMovieGenre(id)
        item["runtime"] = getMovieRuntime(id)
        item["castscore"] = 0

    return top250


######### FOR RISHA
# call getCastTuples() to get a list of (movies, [FULL CAST LIST])
def getCastTuples():
    top250 = getTop250()
    casts = []
    for item in top250:
        print("HIT")
        casts.append((item["title"], item["cast"]))

    return casts

def dumpTop250():
    tops = getTop250()
    jsonTops = json.dumps(tops)
    print(jsonTops)
    f = open("newData.json", "w")
    f.write(jsonTops)
    f.flush()
    print("Post Write")

print("Pre dumps")
dumpTop250()