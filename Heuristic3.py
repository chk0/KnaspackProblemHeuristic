#!/usr/bin/env python3
from itertools import chain 
import sys
from operator import itemgetter
from time import time
import time
from multiprocessing.pool import ThreadPool
from datetime import datetime


# heuristic algorithm 3

def heristic(n, W, X, arrVW):

    _v = arrVW

    j = 0
    while len(_v) != 0:
        i = _v[j][0]        
        if _v[j][1] <= W:
            X += i
            W -= _v[j][1]
        _v.pop(j)
        ++j

    return X, W


#reading the .dat file

def readData(fname):
    try:
        split_list = [] 
        vBetweenw = list()
        arrV = list()
        arrW = list()
        listaDividida = list()

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
        
        for k in range(len(arrVW)):
            arrVW[k].append(arrVW[k][0]/arrVW[k][1])

        arrVW = sorted(arrVW, key=lambda x: x[2], reverse=True)

        travel = int(n/4)
        split_list.append(0)
        for i in range(3):
            split_list.append(travel)
            travel += int(n/4)

        outcome = [arrVW[i : j] for i, j in zip([0] + 
          split_list, split_list + [None])] 
          
        arrVW1 = outcome[1]
        arrVW2 = outcome[2]
        arrVW3 = outcome[3]
        arrVW4 = outcome[4]
        return travel, W, arrVW1, arrVW2 ,arrVW3 ,arrVW4
        fhandle.close()
    except IOError as ex:
        print('There was an error reading the instance')
        raise Exception
        sys.exit(1)

if __name__ == "__main__":

    fname = sys.argv[1]
    pool = ThreadPool(processes=1)

    n, W, arrVW1,arrVW2 ,arrVW3 ,arrVW4  = readData(fname)


    start_time = time.time()

    X = 0
    t = pool.apply_async(heristic, (n, W, X, arrVW1))
    X1, W1 = t.get()
    time.sleep(0.0001)
    t1 = pool.apply_async(heristic, (n, W1, X1, arrVW2))
    X2, W2 = t1.get()
    time.sleep(0.0001)
    t2 = pool.apply_async(heristic, (n, W2, X2, arrVW3))
    X3, W3 = t2.get()
    time.sleep(0.0001)
    t3 = pool.apply_async(heristic, (n, W3, X3, arrVW4))

    Xfinal, W4 = t3.get()
    
    elapsed_time = time.time() - start_time
    print("Heuristic con Hilos time: %0.10f seconds." % elapsed_time)

    print("f(x) = {}".format(Xfinal))

 
