from typing import final
import json
from automata.fa.dfa import DFA
import math

# opening the primes list
primes_file = open("primes.txt" , "r")
llist = primes_file.read()
primes_list = list(llist[:len(llist) - 1].split())

def get_vector(A, n):
    """
    Input is a DFA A and a positive integer n, which 
    is equal to the number of states of A. Output is 
    a list of size 1 + p_1 + p_2 + ... + p_n, where 
    p_i is the ith prime number.
    """
    # strings of length atmost 2*n - 2
    max_length = 2*n - 2
    upper_bound = (1 << max_length) - 1
    

    # getting the required vector
    ans_vector = []

    # loop through each of the n primes in the list
    for i in range(0 , n):
        p = int(primes_list[i])
        for j in range(0 , p):
            # look at numbers which are j mod p
            # loop starts at j, goes till upper bound, takes p steps a time
            count = 0
            for k in range(j , upper_bound + 1 , p):
                bin_string = bin(k)[2:]
                if (A.accepts_input(bin_string)):
                    count = count + 1
                # also check strings starting with a 0
                while(len(bin_string) < max_length):
                    bin_string = '0' + bin_string
                    if (A.accepts_input(bin_string)):
                        count = count + 1
            ans_vector.append(count)

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
    for i in range(0 , n):
        print("\t" + str(i) + ": " + str(A.transitions[str(i)]))
    print("initial state: " + A.initial_state)
    print("final states: " + str(A.final_states))

