#!/usr/bin/env python3

import numpy as np
import scipy.linalg
from scipy.spatial import distance

def vector_angles(X, Y):
    length = X.shape[0]
    result = np.zeros((length))
    
    for i in range(length):
        result[i] = (np.dot(X[i], Y[i])/scipy.linalg.norm(X[i])/scipy.linalg.norm(Y[i]))
        
    clip = np.clip(result, -1, 1)
    
    angles = np.arccos(clip)
    return np.degrees(angles)
    
    
def main():
    a = np.array([[0,0,1],[-1,1,0]])
    b = np.array([[0,1,0], [1,1,0]])
    print(vector_angles(a,b))

if __name__ == "__main__":
    main()
