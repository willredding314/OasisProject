import numpy as np
from numpy import dot
from numpy.linalg import norm

#git commit -m "message"
#git push origin CREATE-USER-DATA

startData = [0.5] * 17
userVector = startData
userFilters = [0] * 10
filterMovies = userFilters

# USER DATA -> DICT: {"Filters": Filters-Dict, "Vectors": List-of Nums}

user = {
    "Filters" : {
        "Netflix" : 1, 
        "Hulu" : 1,
        "R-accepted" : 1
    },
    "Vectors" : startData
}

#horror, romance, action, comedy, 
#make the list (third item), a sample movie vector, matching the ordering of 
#the vector items (genres should be 0 or 1, runtime between 0 and 1, cast between 0 and 5)
movieData = [0.5] * 10
exVector = movieData
exVector = [("The Lorax", {}, [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]),
("The Godfather Pt. 1", {}, [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]),
("The Dark Knight", {}, [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]),
("Spirited Away", {}, [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]),
("Pulp Fiction", {}, [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]),
("Fight Club", {}, [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]),
("Forrest Gump", {}, [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]),
("Goodfellas", {}, [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]),
("Interstellar", {}, [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]),
("Parasite", {}, [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1])]

userVector = [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]
# a lot of vectors 
# add final vector number between 0-5
# LIST :
#    VECTORS - one for each movie, really just a list of numbers
# Create a new list with same length as movie list
# Run cosine similarity on each, add structure of ( movie-name , cosine similarity )
tup = ("moviename", 0.016) #second value is cosine similarity
# Run though that list, get top 5 highest in order


def get_similarity(movieTup, userVector):
  x = userVector
  y = movieTup()[2]
  tuple = (movieTup()[0], dot(x, y)/(norm(x)*norm(y)))
  return tuple

def convert_to_similarity(listMovieTup, userVector):
    for i in listMovieTup:
        get_similarity(i, userVector)

def tuple_sort(tup): 
    return (sorted(tup, key = lambda x: x[1])) 

def best_movies(listMovieTup, userVector):
    tupsList = convert_to_similarity(listMovieTup, userVector)
    sortTups = tuple_sort(tupsList)
    topFive = sortTups[-5 : ]
    print(topFive)