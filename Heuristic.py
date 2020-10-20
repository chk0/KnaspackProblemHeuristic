#!/usr/bin/env python3

import sys
import numpy as np
from operator import itemgetter
from time import time



# heuristic algorithm 1

def heristic(n, W, arrV, arrW, arrVW):

    _v = sorted(arrVW, key=lambda x: x[0], reverse=True)

    start_time = time()
    X = 0
    j = 0
    while len(_v) != 0:
        i = _v[j][0]        
        if _v[j][1] <= W:
            X += i
            W -= _v[j][1]
        _v.pop(j)
        ++j

    elapsed_time = time() - start_time
    print("Heuristic time: %0.10f seconds." % elapsed_time)

    print("f(x) = {}".format(X))




#reading the .dat file

def readData(fname):
    try:
        arrV = list()
        arrW = list()

        fhandle = open(fname, 'r')
        line = fhandle.readline()
        values = line.strip().split()
        arrVW  = list()
        n, W = int(values[0]), int(values[1])

        for y in range(n):
            arryVyW  = list()
            line = fhandle.readline()
            f = line.rstrip().split()
            for x in range( len(f) ):
                arryVyW .append( int(f[x]) )
            arrVW .append( arryVyW  )
        
        for i in range(len(arrVW )):
            arrV.append(arrVW[i][0])
            
        for j in range(len(arrVW)):
            arrW.append(arrVW[j][0])

        return n, W, arrV, arrW, arrVW
        fhandle.close()
    except IOError as ex:
        print('There was an error reading the instance')
        raise Exception
        sys.exit(1)

        

if __name__ == "__main__":

    fname = sys.argv[1]

    n, W, arrV, arrW, arrVW = readData(fname)

    heristic(n, W, arrV, arrW, arrVW)
