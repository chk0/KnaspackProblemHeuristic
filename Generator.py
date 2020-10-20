#!/usr/bin/env python3

import sys
import random
import math

# function randoms w 

def wRandoms(n, _min, _max):
    l = list()

    for i in range(n):
        l.append( random.randint( _min, _max) )

    return l


# function randowm v

def vRandoms(n, _min, _max):
    l = list()

    for i in range(n):
        l.append( random.randint( _min, _max) )

    return l


# function calculate W

def getW(n, _min, _max):
    wAverage = float((_min + _max)/2)
    W = float(n*wAverage * 0.3)
    W = int(W)
    return W



# Main 

# input del generador [n, v-min - v-max, w-min - w-max, I]

n = int(sys.argv[1])

# v range
ran = (sys.argv[2])
if ran.count('-') != 1:
    raise ValueError('Error parsing cost range.')
vMin, vMax = int(ran.split('-')[0]), int(ran.split('-')[1])

# w range
ran = sys.argv[3]
if ran.count('-') != 1:
    raise ValueError('Error parsing cost range.')
wMin, wMax = int(ran.split('-')[0]), int(ran.split('-')[1])

I = int(sys.argv[4])

OUTPUT_DIR = '.'
if len( sys.argv) > 5: OUTPUT_DIR = str(sys.argv[5])

try:
    for i in range(I):
        fname = "{out_dir}/file{}.dat".format(i+1, out_dir = OUTPUT_DIR)
        fhandle = open(fname, 'w')

        W = getW(n, vMin, vMax)
        desc = '''{n} {W}\n'''.format(n = n, W = W)
        fhandle.write(desc)

        v = vRandoms(n, vMin, vMax)
        w = wRandoms(n, wMin, wMax)
        for i in range( len(v) ):
            fhandle.write( "{0} {1}\n".format(v[i], w[i]) )
            
        print('Generating instance {0}... '.format(fname), end='')
        print('Done!')
        fhandle.close()
except IOError as ex:
    print('Error while trying to write file')
    print(ex)
