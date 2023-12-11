
#@author: iceland, modified by @mcdouglasx


import secp256k1 as ice
import bit
import time
import random
import os
from fastecdsa import curve
from fastecdsa.point import Point
from bitstring import BitArray
import numpy as np

#Pk: 33185509 puzzle #30

Target = '03057fbea3a2623382628dde556b2a0698e32428d3cd225f3bd034dca82dd7455a'

start= 0                                        
end=   33554431                                                              

m = 2000000 # Keys number in Binary Babystep

Add = 1
Add_pub= ice.scalar_multiplication(Add)
Cm= 64


public_key = ice.pub2upub(Target).hex()

bs_file = 'baby_steps__binary.bin'

def Pub2Point(public_key):
    x = int(public_key[2:66],16)
    if len(public_key) < 70:
        y = bit.format.x_to_y(x, int(public_key[:2],16)%2)
    else:
        y = int(public_key[66:],16)

    return Point(x, y, curve=curve.secp256k1)

Q = Pub2Point(public_key)
G = curve.secp256k1.G

#find baby step file

valid = os.path.isfile(bs_file)
if valid == True:
    print('\nFound the Baby Steps Table file: '+bs_file+'. Will be used directly')
    
    file = bytes(np.fromfile(bs_file))

    baby_steps= BitArray(file)
        
if valid == False:
    print('\nNot Found '+bs_file+'. you must Create This File Now.' )


k1 = random.randint(start, end)
#k1 =1      
k2 = k1 + m*m
print('Checking {0} keys from {1}'.format(m*m, hex(k1)))
# m = math.floor(math.sqrt(k2-k1))

# start time
st = time.time()

k1G = k1 * G
mG = m * G

#find key

def findkey(onePoint):
    S = onePoint - k1G
    if S == Point.IDENTITY_ELEMENT: return k1    # Point at Infinity
    found = False
    step = 0
    while found is False and step<(1+k2-k1):
        Sx_0= ice.pub2upub("04"+(str(hex(int(str(S.x))))[2:])+(str(hex(int(str(S.y))))[2:]))
        Sx_1= ice.point_sequential_increment(Cm, Sx_0)
        binary = ''
        
        for t in range (Cm):

            h= (Sx_1[t*65:t*65+65]).hex()
            hc= int(h[2:], 16)
                
                
            if str(hc).endswith(('0','2','4','6','8')):
                A="0"
                binary+= ''.join(str(A))
                    
            if str(hc).endswith(('1','3','5','7','9')):
                A="1"
                binary+= ''.join(str(A))

                
        
        b = BitArray(bin=binary)            
        c = bytes(b)
        Sw =c
        
        
        if b in baby_steps:
            #
            s = c
            f = BitArray(baby_steps)
            inx = f.find(s)
            inx_1=str(inx).replace(",", "")
            inx_0=str(inx_1).replace("(", "")
            inx_2=str(inx_0).replace(")", "")
            b = int(inx_2) 
            found = True
            break
        else:
            # Giant step
            S = S - mG
            step = step + m
    if found == True:
        #print("k1:",k1)
        #print("step:",step)
        #print("b:",b)
        
        final_key = (k1 + step + b + 1)-1
        
    else:
        final_key = -1
    return final_key


final_key = findkey(Q)

if final_key >0: 
    print("BSGS FOUND PrivateKey  :",str(final_key))
    data= open("win.txt", "a")
    data.write("private key = "+str(final_key)+"\n")
    data.write(str("Time Spent : {0:.2f} seconds".format(time.time()-st))+ "\n")
    data.close()
else:
    print('PrivateKey Not Found')


print(str("Time Spent : {0:.2f} seconds".format(time.time()-st)))
