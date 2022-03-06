#Ariel Tynan
#Euler Problem 050 Solved in Python
#Consecutive prime sum
#Started and solved 5 March 2022
#Current compile time ~53s

from numpy import sqrt

#Prime number sieve up to 1000000
def prime_Sieve(n): #Function modified from Geeksforgeeks
     
    primes = [] # initial empty list of primes
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers
    for p in range(n + 1):
        if prime[p]:
            primes.append(p)
    return primes

max_primes = [0]*1000000 #maximum length of primes list for each prime

primes = prime_Sieve(1000000) #all primes below 1000000... 78498 primes under a million
for i in range(len(primes)-1,1,-1):
    tempMaxPrime = 0 #temp variable for max prime for each prime of interest
    #143 value derived from finding max number that still allowed results.
    for j in range(int(i/143)-1,1,-1): #iterate from i position to start of primes list (backwards) #143 is arbitrary
        temp = primes[i] #temp value of prime of interest
        tempListLen = 0 #length of primes generated given starting prime in list
        while temp > 0 and j > -1:
            temp = temp - primes[j] #temp value of prime of interest
            j = j - 1
            #print(primes[j])
            tempListLen = tempListLen + 1
        if j == -1 and temp > 0: #lower cutoff
            break
        if tempListLen > tempMaxPrime and temp == 0: #checks to make sure values are equal
            tempMaxPrime = tempListLen
    max_primes[i] = tempMaxPrime
    #print(primes[i], tempMaxPrime)

print(max(max_primes),primes[max_primes.index(max(max_primes))])  #list length and prime of interest
