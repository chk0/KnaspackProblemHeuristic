#!/usr/bin/env python3
from itertools import chain 
import sys
from operator import itemgetter
from time import time
import time
from multiprocessing.pool import ThreadPool
from datetime import datetime
# from threading import Thread


# heuristic algorithm 1

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
        
        for i in range(len(arrVW )):
            arrV.append(arrVW[i][0])
            
        for j in range(len(arrVW)):
            arrW.append(arrVW[j][0])

        arrVW = sorted(arrVW, key=lambda x: x[0], reverse=True)
        recorrer = int(n/4)
        split_list.append(0)
        for i in range(3):
            split_list.append(recorrer)
            recorrer += int(n/4)

        res = [arrVW[i : j] for i, j in zip([0] + 
          split_list, split_list + [None])] 
          
        arrVW1 = res[1]
        arrVW2 = res[2]
        arrVW3 = res[3]
        arrVW4 = res[4]
        return recorrer, W, arrVW1, arrVW2 ,arrVW3 ,arrVW4 
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
    t2 = pool.apply_async(heristic, (n, W2, X2,  arrVW3))
    X3, W3 = t2.get()
    time.sleep(0.0001)
    t3 = pool.apply_async(heristic, (n, W3, X3,  arrVW4))

    Xfinal, W4 = t3.get()
    
    elapsed_time = time.time() - start_time
    print("Heuristic con Hilos time: %0.10f seconds." % elapsed_time)

    print("f(x) = {}".format(Xfinal))

 
