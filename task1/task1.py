import random
import matplotlib.pyplot as plt
import cv2
import numpy as np

array = np.empty(1000000, dtype = int)

for i in range(1000000):
    array[i] = random.randint(0, 999)
print(array)

#начиная отсюда надо подумать
def calcHist(tdata):
hist = [0]*10


print(hist)

#   hist [1] = number of values in tdata from 100..199

#   hist [2] = number of values in tdata from 200..299

#   ...

#   hist [9] = number of values in tdata from 900..sys.maxint

    return hist

#   data contains List with size 1000 000 with 0 values

data = [0]*1000000

a = calcHist(data)

print(a)
