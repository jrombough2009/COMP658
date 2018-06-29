import tensorflow as tf
import numpy as np
from random import randrange

#scoreof is the sum of the attributes(7) in each student 
#group size is 4
#each student belongs to one group
#GH is goodness of heterogeneity
#Euclidean distance between at least two of the students must be > 2
#Euclidean distance defined as the rooted sum of two student's vectors square 
dict = {}


ScoreClass7 = []
ScoreClass8 = []
ScoreClass9 = []
ScoreClass10 = []
ScoreClass11 = []
ScoreClass12 = []
ScoreClass13 = []
ScoreClass14 = []
ScoreClass15 = []
ScoreClass16 = []
ScoreClass17 = []
ScoreClass18 = []
groups = []

data = np.genfromtxt('/mx/input.csv', delimiter=',', usecols=(1,2,3,4,5,6,7))



def TotalScore(Student):
    Total = 0
    for x in range(0,6):
        Total = np.add(Student[x],Total)
#    print (" total", Total)
    return Total

for index in range(len(data)):
    dict[index] = TotalScore(data[index])


#for key in sorted(dict):
#    print "%s: %s" % (key, dict[key])

def GH(vec1,vec2,vec3,vec4):
    vec1max = np.amax(vec1) 
    vec1min = np.amin(vec1)

    vec2max = np.amax(vec2) 
    vec2min = np.amin(vec2)

    vec3max = np.amax(vec3) 
    vec3min = np.amin(vec3)

    vec4max = np.amax(vec4) 
    vec4min = np.amin(vec4)

    AD = ((vec1max + vec2max + vec3max + vec4max) + (vec1min + vec2min + vec3min + vec4min)) / 2

    total =  (TotalScore(vec2)-TotalScore(vec1))  / (1 + abs(AD-TotalScore(vec3))+ abs(AD-TotalScore(vec4)))
    
    return total

def diff(s1,s2):
    SquaredTotal = 0
    for x in range(0,6):
        SquaredTotal = np.power((s1[x]-s2[x]),2) + SquaredTotal
    d = np.sqrt(SquaredTotal)    
    print("Sum for %s and %d is %f ",s1, s2, d )
    return d


for index in range(len(data)):
    if dict[index] == 7:
        ScoreClass7.append(index)
print ("ScoreClass7: ", ScoreClass7)

for index in range(len(data)):
    if dict[index] == 8:
        ScoreClass8.append(index)
print ("ScoreClass8: ", ScoreClass8)

for index in range(len(data)):
    if dict[index] == 9:
        ScoreClass9.append(index)
print ("ScoreClass9: ", ScoreClass9)

for index in range(len(data)):
    if dict[index] == 10:
        ScoreClass10.append(index)
print ("ScoreClass10: ", ScoreClass10)

for index in range(len(data)):
    if dict[index] == 11:
        ScoreClass11.append(index)
print ("ScoreClass11: ", ScoreClass11)

for index in range(len(data)):
    if dict[index] == 12:
        ScoreClass12.append(index)
print ("ScoreClass12: ", ScoreClass12)

for index in range(len(data)):
    if dict[index] == 13:
        ScoreClass13.append(index)
print ("ScoreClass13: ", ScoreClass13)

for index in range(len(data)):
    if dict[index] == 14:
        ScoreClass14.append(index)
print ("ScoreClass14: ", ScoreClass14)

for index in range(len(data)):
    if dict[index] == 15:
        ScoreClass15.append(index)
print ("ScoreClass15: ", ScoreClass15)

for index in range(len(data)):
    if dict[index] == 16:
        ScoreClass16.append(index)
print ("ScoreClass16: ", ScoreClass16)

for index in range(len(data)):
    if dict[index] == 17:
        ScoreClass17.append(index)
print ("ScoreClass17: ", ScoreClass17)

#Weights are to be initialized to a random value between 7-18

weight11 = randrange(7,17)
weight12 = randrange(7,17)
weight13 = randrange(7,17)
weight14 = randrange(7,17)

print ("The weights are ",weight11, weight12, weight13, weight14)


# take four student numbers from the lists determined from the weights.
# using this number as an index we will access those student vectors from data
# apply student vectors to GH
# find the difference between GH and 0.5. This will be the error. Apply this error as a positive to two of the nodes and as a negative to the other two weights.
# IF GH > 0.5 then remove from the lists those numbers involved. Store numbers as string in groups with GH 

