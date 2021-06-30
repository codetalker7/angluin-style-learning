from typing import final
import json
from automata.fa.dfa import DFA
import math

def get_language(A, n):
    """
    Input is a DFA A and a positive integer n, which 
    is equal to the number of states of A. Output is 
    a list containing all words of length up to 2n-n accepted by A (along their numerical interpretation).
    """
    # strings of length atmost 2*n - 2
    max_length = 2*n 
    upper_bound = (1 << (max_length+1)) - 1
    

    # getting the required vector
    language = ()

    # loop through each of the n primes in the list
    for i in range(1 , upper_bound):
        bin_string = bin(i)[3:]
        if(A.accepts_input(bin_string)):
            language = language + ((bin_string,i),)
    
    return language

