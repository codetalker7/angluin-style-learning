from typing import final
import json
from automata.fa.dfa import DFA
import math

# opening the primes list
primes_file = open("primes.txt" , "r")
llist = primes_file.read()
primes_list = list(llist[:len(llist) - 1].split())

def get_vector(A, n, max_length=None, no_of_primes=None):
    """
    Input is a DFA A and a positive integer n, which 
    is equal to the number of states of A. Output is 
    a list of size 1 + p_1 + p_2 + ... + p_n, where 
    p_i is the ith prime number. max_length is the 
    maximum length of strings you want to check.
    """

    if (max_length == None):
        # strings of length atmost 2*n
        max_length = 2*n
    # setting upper bound
    upper_bound = (1 << max_length)

    # setting no_of_primes if it is None
    if (no_of_primes == None):
        no_of_primes = n

    # initialising the vector coordinates
    coord = []
    for j in range(0, no_of_primes):
        # append an empty list
        coord.append([])
        # in this list, append p zeros
        p = int(primes_list[j])
        for k in range(0, p):
            coord[j].append(0)

    # handling the boundary case of the empty string
    if (A.accepts_input('')):
        # append a 1 in front of the empty string
        curr_number = 1

        # update the coordinates for each prime
        for j in range(0, no_of_primes):
            p = int(primes_list[j])
            coord[j][curr_number % p] = coord[j][curr_number % p] + 1

    # iterating over all non-empty binary strings of length atmost maxlength
    for i in range(0, upper_bound):
        bin_string = bin(i)[2:]

        # appending zeros to bin_string if it's needed
        while (len(bin_string) <= max_length):
            if (A.accepts_input(bin_string)):
                # append a 1 in front of the binary string
                curr_number = (1 << len(bin_string)) + i

                # update the coordinates for each prime
                for j in range(0, no_of_primes):
                    p = int(primes_list[j])
                    coord[j][curr_number % p] = coord[j][curr_number % p] + 1

            # add a zero to the front of the string for the next iteration
            bin_string = '0' + bin_string
    
    # returning the answer vector 
    ans_vector = ()
    for j in range(0, no_of_primes):
        p = int(primes_list[j])
        for k in range(0, p):
            ans_vector = ans_vector + (coord[j][k], )

    return ans_vector


    

