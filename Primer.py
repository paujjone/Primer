##########################################################
#                     P R I M E R                        #
##########################################################
#       A simple python scipt to find prime numbers      #
#     Ideally this is a good script that can be added    #
#              to other future projects.                 #
#                                                        #
#             Copyright (c) 2017 Paul Jones              #
#                                                        #
##########################################################

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.



# Starting List for primes
Primes = [2]
# Number being tested
X = 3
while True:                                #Outer Loop : Runs indefinitely
    Y = -1
    while Y < X:                           #Inner Loop Runs until X is found to be Prime or Composite
        Y += 1
        if (X < Primes[Y] * Primes[Y])
            or (Y + 1 >= X):               #Prime
            Primes.append(X)
            X += 1
            Y = X
        elif X % Primes[Y] == 0:           # Composite
            X += 1
            Y = X
