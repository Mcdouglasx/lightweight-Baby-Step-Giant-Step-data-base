**The Baby Step Giant Step (BSGS)** algorithm is used to solve the discrete logarithm problem efficiently in a cyclic group. The algorithm works by breaking down the problem into two steps:




**Baby Steps**

In this step, we calculate a list of baby steps by iteratively raising the generator g to different powers. We start with j = 0 and calculate g^j for values of j from 0 up to m-1 , where m is typically chosen as the square root of the group order n . We store each calculation in 1 bit per key, this is the highlight because it considerably minimizes the size of our database.


**create binary baby step**

**using babyStep_db_v1.py**



**Giant Steps**

In this step, we perform giant steps by multiplying, this approach is efficient because it reduces the search space for the discrete logarithm from O(n) to O(sqrt(n)) , significantly speeding up the computation for large cyclic groups.


**search script**

**using binary_bsgs_v1.py**




I have used iceland's work on Bsgs to expose my lightweight database system.

secp256k1

https://github.com/iceland2k14/secp256k1

Download and place the files in the same folder as the scripts


bitcointalk post https://bitcointalk.org/index.php?topic=5477342

**Donate to: btc: bc1qxs47ttydl8tmdv8vtygp7dy76lvayz3r6rdahu**

