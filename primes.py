import math
import sys

primes_file = open("primes.txt" , "w")

# getting the first N primes, where N is some input
N = int(sys.argv[1])

# we know that the first N primes are less than NlogN
K = int(N*math.log2(N))

# get the list of all N primes using the Sieve
is_prime = []
for i in range(0 , K + 1):
    is_prime.append(1)

for i in range(2 , K + 1):
    if is_prime[i] == 1: 
        primes_file.write(str(i) + " ")
        for j in range (2*i , K + 1 , i):
            is_prime[j] = 0



