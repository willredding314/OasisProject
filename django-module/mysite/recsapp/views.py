from cmath import sqrt
import string
from xmlrpc.client import boolean
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TextSelection
from .form import QuestionsForm
import json

def index(request):
    return HttpResponse("Index Page!")

def questions(request):

    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            formDict = form.cleaned_data
            return results(request, formDict)

    else:
        form = QuestionsForm()

    return render(request, 'recsapp/questions.html', {'form': form})

def results(request, formDict):
    filterChoices = getFilters(formDict)
    vectorChoices = getVectors(formDict)
    actors = formDict["actors"].split(",")
    directors = formDict["directors"].split(",")
    movieVectors = makeMovieVectors(actors, directors)
    movieFilters = makeMovieFilters()
    movieNames = getMovieNames()
    blockedInd = filterMovies(movieFilters, filterChoices)
    clearedVectors = finalVectors(blockedInd, movieNames, movieVectors)
    vectorScores = compareVectors(clearedVectors, vectorChoices)
    top5 = getTop5(vectorScores)

    return render(request, 'recsapp/results.html', {'top5': top5})

def getTop5(scores):
    scoresSorted = sorted(scores, key = lambda i: i["score"].real, reverse = True)
    top5 = [
        scoresSorted[0]["name"],
        scoresSorted[1]["name"],
        scoresSorted[2]["name"],
        scoresSorted[3]["name"],
        scoresSorted[4]["name"],
    ]
    return top5

def compareVectors(movies, user):
    
    results = []
    for item in movies:
        res = {}
        res["name"] = item["name"]
        score = cosineSimilarity(user, item["vectors"])
        res["score"] = score
        results.append(res)
    return results

def cosineSimilarity(v1, v2):
    num = dotProduct20(v1, v2)
    den = vectorMagnitude(v1) * vectorMagnitude(v2)
    res = num / den
    return res

def vectorMagnitude(v):
    res = 0
    for a in v:
        res = a * a + res
    res = sqrt(res)
    return res

def dotProduct20(v1, v2):
    res = 0
    for i in range (19):
        res = v1[i] * v2[i] + res
    return res

def finalVectors(blockedInd, movieNames, movieVectors):

    clearedVectors = []
    for i in range (249):
        if i not in blockedInd:
            entry = {}
            entry["name"] = movieNames[i]
            entry["vectors"] = movieVectors[i]
            clearedVectors.append(entry)

    return clearedVectors

def filterMovies(movieFilters, choices):

    blocked = []
    for i in range (249):
        if movieFilters[i]["year"] < choices["yearEarly"]:
            blocked.append(i)
        elif movieFilters[i]["year"] > choices["yearLatest"]:
            blocked.append(i)
        elif noSharedSource(movieFilters[i]["streaming"], choices):
            blocked.append(i)
        elif noMatchingRating(movieFilters[i]["rating"], choices):
            blocked.append(i)
    return blocked

def noMatchingRating(rating, choices):
    if rating == "free":
        return False
    elif choices[rating] == True:
        return False
    else: 
        return True

def noSharedSource(sources, choices):

    if sources[0] == "free":
        return False
    for item in sources:
        if choices[item]:
            return False
    return True

def makeMovieFilters():
    f = open("./recsapp/movieData.json")
    movieData = json.load(f)
    movieFilters = [{}] * 250

    for i in range (249):
        movie = movieData[i]
        filters = {}
        filters["year"] = movie["year"]
        filters["rating"] = movie["rating"]
        filters["streaming"] = movie["Source"]
        movieFilters[i] = filters
    
    return movieFilters


def makeMovieVectors(actors, directors):
    f = open("./recsapp/movieData.json")
    movieData = json.load(f)
    movieVectors = [[]] * 250
    
    for i in range (249):
        movie = movieData[i]
        vector = [0] * 20
        vector[0] = actorScore(movie["cast"], actors)
        vector[1] = directorScore(movie["director"], directors)
        vector[2] = int(movie["runtime"]) / 200
        for genre in movie["genre"]:
            if genre == 'Drama':
                vector[3] = 1
            if genre == 'Crime':
                vector[4] = 1
            if genre == 'Action':
                vector[5] = 1
            if genre == 'Thriller':
                vector[6] = 1
            if genre == 'History':
                vector[7] = 1
            if genre == 'War':
                vector[8] = 1
            if genre == 'Adventure':
                vector[9] = 1
            if genre == 'Fantasy':
                vector[10] = 1
            if genre == 'Western':
                vector[11] = 1
            if genre == 'Comedy':
                vector[12] = 1
            if genre == 'Romance':
                vector[13] = 1
            if genre == 'Science Fiction':
                vector[14] = 1
            if genre == 'Mystery':
                vector[15] = 1
            if genre == 'Family':
                vector[16] = 1
            if genre == 'Animation':
                vector[17] = 1
            if genre == 'Horror':
                vector[18] = 1
            if genre == 'Music':
                vector[19] = 1
        movieVectors[i] = vector
            
    return movieVectors

def getMovieNames():
    f = open("./recsapp/movieData.json")
    movieData = json.load(f)
    movieNames = [""] * 250
    for i in range (249):
        movieNames[i] = movieData[i]["title"]
    return movieNames

def actorScore(cast, actors):
    base = len(actors)
    score = 0
    for item in actors:
        if item in cast:
            score += 1
    
    return score * 5 / base

def directorScore(director, favorites):
    for item in favorites:
        if item in director:
            return 5
    return 0

def getFilters(formDict):
    #important: amazon, apple, hbo, netflix, disney
    filters = {}
    filters["yearEarly"] = formDict["yearEarly"]
    filters["yearLatest"] = formDict["yearLatest"]
    filters["R"] = formDict["ratedr"]
    filters["PG-13"] = formDict["ratedpg13"]
    filters["PG"] = formDict["ratedPG"]
    filters["G"] = formDict["ratedG"]
    filters["netflix"] = formDict["netflix"]
    filters["hulu"] = formDict["hulu"]
    filters["amazon"] = formDict["amazon"]
    filters["peacock"] = formDict["peacock"]
    filters["hbo"] = formDict["hbo"]
    filters["disney"] = formDict["disney"]
    filters["paramount"] = formDict["paramount"]
    filters["discovery"] = formDict["discovery"]
    filters["apple"] = formDict["apple"]
    return filters

def getVectors(formDict):
    vectors = [0] * 20
    vectors[0] = 5
    vectors[1] = 5
    vectors[2] = int(formDict['length']) / 200
    if (formDict['drama'] == False):
        vectors[3] = 0
    else:
        vectors[3] = 1
    if (formDict['crime'] == False):
        vectors[4] = 0
    else:
        vectors[4] = 1
    if (formDict['action'] == False):
        vectors[5] = 0
    else:
        vectors[5] = 1
    if (formDict['thriller'] == False):
        vectors[6] = 0
    else:
        vectors[6] = 1
    if (formDict['history'] == False):
        vectors[7] = 0
    else:
        vectors[7] = 1
    if (formDict['war'] == False):
        vectors[8] = 0
    else:
        vectors[8] = 1
    if (formDict['adventure'] == False):
        vectors[9] = 0
    else:
        vectors[9] = 1
    if (formDict['fantasy'] == False):
        vectors[10] = 0
    else:
        vectors[10] = 1
    if (formDict['western'] == False):
        vectors[11] = 0
    else:
        vectors[11] = 1
    if (formDict['comedy'] == False):
        vectors[12] = 0
    else:
        vectors[12] = 1
    if (formDict['romance'] == False):
        vectors[13] = 0
    else:
        vectors[13] = 1
    if (formDict['scifi'] == False):
        vectors[14] = 0
    else:
        vectors[14] = 1
    if (formDict['mystery'] == False):
        vectors[15] = 0
    else:
        vectors[15] = 1
    if (formDict['family'] == False):
        vectors[16] = 0
    else:
        vectors[16] = 1
    if (formDict['animation'] == False):
        vectors[17] = 0
    else:
        vectors[17] = 1
    if (formDict['horror'] == False):
        vectors[18] = 0
    else:
        vectors[18] = 1
    if (formDict['music'] == False):
        vectors[19] = 0
    else:
        vectors[19] = 1

    return vectors