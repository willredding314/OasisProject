import numpy as np


startData = [0.5] * 10
userVector = np.array(startData)

#File to get user data in vector form
print("Do you like horror?")
response = input()
userVector[0] = response
print(userVector[0])

