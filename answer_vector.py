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
    upper_bound = (1 << (max_length+1)) - 1

    # setting no_of_primes if it is None
    if (no_of_primes == None):
        no_of_primes = n

    # getting the required vector
    ans_vector = ()

    # loop through each of the n primes in the list
    for i in range(0 , no_of_primes):
        p = int(primes_list[i])
        for j in range(0 , p):
            # look at numbers which are j mod p
            # loop starts at j, goes till upper bound, takes p steps a time
            count = 0
            for k in range(j , upper_bound + 1 , p):
                # skip k = 0 to avoid checking empty string twice
                if (k == 0):
                    continue
                bin_string = bin(k)[3:]
                if (A.accepts_input(bin_string)):
                    count = count + 1
                # also check strings starting with a 0
                #while(len(bin_string) < max_length):
                #    bin_string = '0' + bin_string
                #    if (A.accepts_input(bin_string)):
                #        count = count + 1
            ans_vector = ans_vector + (count,)

    return ans_vector

def print_dfa(A, n):
    """
        Input is a DFA A and n - it's number 
        of states. It outputs the answer vector 
        for the DFA A, along with A's information.
    """
    # printing the transitions in the DFA
    print("number of states: " + str(n))
    print("transitions:")
    print (json.dumps(A.transitions, indent=2, default=str))
    print("initial state: " + str(A.initial_state))
    print("final states: " + str(A.final_states))

