#import numpy as np

####  INSTALLS NEEDED
# git - can then clone the repo
# pip - for all python downloads $ pip install NAME
#      - python
#      - numpy
#      - requests

#git commit -m "message"
#git push origin CREATE-USER-DATA

startData = [0.5] * 17
userVector = startData
userFilters = [0] * 10
filterMovies = userFilters

#File to get user data in vector form
print("Do you like horror?")
response = input()
userVector[0] = response
print(userVector[0])

print("Do you like romance?")
response = input()
userVector[1] = response
print(userVector[1])

print("Do you like action?")
response = input()
userVector[2] = response
print(userVector[2])

print("Do you like comedy?")
response = input()
userVector[3] = response
print(userVector[3])

print("Do you like drama?")
response = input()
userVector[4] = response
print(userVector[4])

print("Do you like thrillers?")
response = input()
userVector[4] = response
print(userVector[4])

print("Do you like animation?")
response = input()
userVector[5] = response
print(userVector[5])

print("Do you like crime?")
response = input()
userVector[6] = response
print(userVector[6])

print("Do you like thriller?")
response = input()
userVector[7] = response
print(userVector[7])

print("Do you like history?")
response = input()
userVector[8] = response
print(userVector[8])

print("Do you like war?")
response = input()
userVector[9] = response
print(userVector[9])

print("Do you like adventure?")
response = input()
userVector[10] = response
print(userVector[10])

print("Do you like fantasy?")
response = input()
userVector[11] = response
print(userVector[11])

print("Do you like western?")
response = input()
userVector[12] = response
print(userVector[12])

print("Do you like romance?")
response = input()
userVector[13] = response
print(userVector[13])

print("Do you like science-fiction?")
response = input()
userVector[14] = response
print(userVector[14])

print("Do you like mystery?")
response = input()
userVector[15] = response
print(userVector[15])

print("Do you like family?")
response = input()
userVector[15] = response
print(userVector[15])

print("Do you like musicals?")
response = input()
userVector[16] = response
print(userVector[16])



print("Do you have Hulu?")
response = input()
userFilters[0] = response
print(userVector[0])

print("Do you have Netflix?")
response = input()
userFilters[1] = response
print(userVector[1])

print("Do you have Amazon Prime?")
response = input()
userFilters[2] = response
print(userVector[2])

print("Do you watch rated R movies?")
response = input()
userFilters[3] = response
print(userVector[3])

fakeDict = {} 
fakeDict["fakeKey"] = "fakeVal"
# holds all the data on the movies
# one field on hard filters and one on vector
# how many values in filters, vs. how many values in current vector
# make data type for movie/user response

# USER DATA -> DICT: {"Filters": Filters-Dict, "Vectors": List-of Nums}

user = {
    "Filters" : {
        "Netflix" : 1, 
        "Hulu" : 1,
        "R-accepted" : 1
    },
    "Vectors" : startData
}

#make the list (third item), a sample movie vector, matching the ordering of 
#the vector items (genres should be 0 or 1, runtime between 0 and 1, cast between 0 and 5)
movieTup1 = ("Moviename", {}, [])
movieTup2 = ("Moviename", {}, [])

userVector = []
# a lot of vectors 
# add final vector number between 0-5
# LIST :
#    VECTORS - one for each movie, really just a list of numbers
# Create a new list with same length as movie list
# Run cosine similarity on each, add structure of ( movie-name , cosine similarity )
tup = ("moviename", 0.016) #second value is cosine similarity
# Run though that list, get top 5 highest in order