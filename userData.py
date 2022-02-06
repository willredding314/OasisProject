import numpy as np

####  INSTALLS NEEDED
# git - can then clone the repo
# pip - for all python downloads $ pip install NAME
#      - python
#      - numpy
#      - requests



startData = [0.5] * 10
userVector = np.array(startData)

#File to get user data in vector form
print("Do you like horror?")
response = input()
userVector[0] = response
print(userVector[0])

