### DO NOT USE THIS!!
### This is not how Hausdorff dimension works.
### I will need DIAMETER, not AREA contraction ratios.
### I left this here purely as a warning.
###
###
### I will revisit this module once I can compute diameter contraction ratios. My notebook is close.


import numpy as np
import numpy.linalg as la
import math
import matplotlib.pyplot as plt


#Matrix from pg 57 of Tucker paper, corresponding to local expansion/contraction of map at z = 1
expand = np.array(
[[11.8 - 0.29, -0.29],
 [0.29, 0.29 - 22.8]])
d =  np.linalg.det(expand)

print d

#Return Matrix from Guckenheimer paper, 1976 (pg  374)
#Used for injection of plane regions into each other
A = np.array(
[[0, 1, 0, 1],
 [0, 0, 0, 1],
 [1, 0, 0, 0],
 [1, 0, 1, 0]])


#Constant of volume contraction (rough start).
c = math.exp(d)
print c
c = 0.25



#The real key is to get the area construction from people or from Tucker's code.

def spectral_radius(matrix):
    return max(la.eigvals(matrix))

def Phi(alpha):
    return spectral_radius((c**alpha)*A)

def binary_search(start, finish, cutoff = 0.0000001):
    mid = (start + finish)/2.0
#    print mid
    f = Phi(mid)
    if finish - start < cutoff:
        return finish #Want upper bound
    if f == 1.0:
        return mid
    if f > 1:
        return binary_search(mid, finish, cutoff)
    if f < 1:
        return binary_search(start, mid, cutoff)


e = binary_search(0, 3)
print e
print c**e


#This is all great, but in this case, everything boils down quite nicely to a completely different problem:
def solution(contraction):
    return math.log((math.sqrt(5) - 1)/2)/math.log(contraction)

#In general, I will use the above algorithm for these "1 and 0" maps, because it will be so much faster.
#I will replace 1/phi with 1/spectral radius, of course.
