from make_galois_tables import *
import aes_utils as ut

x1 = range(256)
x2 = make2x()
x4 = makePowerOf2(2)
x8 = makePowerOf2(3)
x16 = makePowerOf2(4)
x32 = makePowerOf2(5)
x64 = makePowerOf2(6)
x128 = makePowerOf2(7)

fL = [x1,x2,x4,x8,x16,x32,x64,x128]

def multiply(a,b):
    rL = list()
    if a > b:
        a,b = b,a
        
    digits = list(bin(a)[2:])
    digits.reverse()
    for d,f in zip(digits,fL):
        if d == '1':
            rL.append(f[b])
    rem = ut.reducingXOR(rL)
    
    # this step is unnecessary
    # b/c we did it in making the tables!
    if rem > 127:
        return rem ^ 127
    return rem

def makeTable():
    D = dict()
    D[(0,0)] = 0
    
    for i in range(256):
        for j in range(256):
            r = multiply(i,j)
            t = (i,j)
            D[t] = r
            rt = (j,i)
            # a * b == b * a
            if rt in D:
                assert D[t] == D[rt] 
    return D

def printTuples(L):
    for i,t in enumerate(L):
        if i and i % 5 == 0:
            print
        print str(t).ljust(12),

def showInverses(D):
    invL = [t for t in D if D[t] == 1]
    invL.sort()
    printTuples(invL)

D = makeTable()                  
showInverses(D)

def test(D):
    # for any product p and multiplicand a, 
    # there is exactly one b such that
    # a * b = p
    pD = dict()
    for (i,j) in D.keys():
        if i == 0 or j == 0:
            continue
        p = D[(i,j)]
        # for every product, add the i to a list
        if not p in pD:
            # don't worry about j
            pD[p] = [i]
        else:
            pD[p].append(i)
            
    for p in pD.keys():
        iL = pD[p]
        iL.sort()
        sL = list(set(iL))
        print p, len(iL), len(sL), iL[:5]
        

test(D)

'''
Every number has a unique multiplicative inverse

> python galois_multiply.py 
(1, 1)       (2, 141)     (3, 246)     (4, 203)     (5, 82)     
(6, 123)     (7, 209)     (8, 232)     (9, 79)      (10, 41)    
..
(246, 3)     (247, 140)   (248, 221)   (249, 156)   (250, 125)  
(251, 160)   (252, 205)   (253, 26)    (254, 65)    (255, 28)   
> 

It appears that for every product p,
p can be generated by multiplying
every a by exactly one b

> python galois_multiply.py 
1 255 255 [1, 2, 3, 4, 5]
2 255 255 [1, 2, 3, 4, 5]
..
254 255 255 [1, 2, 3, 4, 5]
255 255 255 [1, 2, 3, 4, 5]
>
'''
    