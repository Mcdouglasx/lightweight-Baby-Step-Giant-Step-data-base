#by mcdouglasx
import secp256k1 as ice
from bitstring import BitArray

print("creating Baby Step")


#create baby step

num = 2000000 # Keys number in Binary Babystep. same m in search script

Low_m= 20

lm= num // Low_m

Add = 1
Add_pub= ice.scalar_multiplication(Add)

res= ice.point_sequential_increment(lm, Add_pub)

binary = ''
for t in range (lm):

    h= (res[t*65:t*65+65]).hex()
    hc= int(h[2:], 16)
        
        
    if str(hc).endswith(('0','2','4','6','8')):
        A="0"
        binary+= ''.join(str(A))
            
    if str(hc).endswith(('1','3','5','7','9')):
        A="1"
        binary+= ''.join(str(A))
        

my_str = (BitArray(bin=binary))#bin=binary

binary_file = open('baby_steps__binary.bin', 'ab')
my_str.tofile(binary_file)
binary_file.close()

for i in range (1,Low_m):
    print("stage: "+ str(i+1)+"/"+str(20))
    
    lm_upub= ice.scalar_multiplication((lm*i))

    res= ice.point_sequential_increment(lm, lm_upub)

    binary = ''
    for t in range (lm):

        h= (res[t*65:t*65+65]).hex()
        hc= int(h[2:], 16)
            
            
        if str(hc).endswith(('0','2','4','6','8')):
            A="0"
            binary+= ''.join(str(A))
                
        if str(hc).endswith(('1','3','5','7','9')):
            A="1"
            binary+= ''.join(str(A))
            

    my_str = (BitArray(bin=binary))#bin=binary

    binary_file = open('baby_steps__binary.bin', 'ab')
    my_str.tofile(binary_file)
    binary_file.close()
