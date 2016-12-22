import numpy
# Number being tested
X = 3
# Starting List for primes
Primes = [2]
#Outer Loop : Runs indefinitely
try:
    while True:
        Y = 1
        M = 1
        if X <= 100:
            while Y < X:
                Y = Y + 1
                M = M + 1
                if X % M == 0: # composite
                    X = X + 1
                    Y = X
                elif Y + 1 >= X:
                    Primes.append(X)
                    print(X)
                    X = 1 + X
                    Y = X
                    M = 1          
        elif X > 100:  
            M = -1
            while Y < X: 
                Y = Y + 1
                M = M + 1
                if X < Primes[M] * Primes[M]:
                    Primes.append(X)
                    print(X)
                    X = 1 + X
                    Y = X
                    M = 1          
                elif X % Primes[M] == 0: # composite
                    X = X + 1
                    Y = X         
                elif Y + 1 >= X:       
                    Primes.append(X)
                    print(X)
                    X = 1 + X
                    Y = X                 
                  
except KeyboardInterrupt:
    numpy.savetxt("Primeslist.csv", Primes, delimiter=',')
    print("Primes tucked away!")
    Primeslist.close()
