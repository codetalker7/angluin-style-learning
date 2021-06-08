from typing import final
import json
from automata.fa.dfa import DFA
import math

primes_file = open("primes.txt" , "r")
llist = primes_file.read()
primes_list = list(llist[:len(llist) - 1].split())

# n represents the number of states in the DFA
n = 3
# strings of length atmost 2*n
upper_bound = (1 << (2*n)) - 1

# defining the DFA A
A = DFA(
    states={'0', '1', '2'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '0', '1': '1'},
        '1': {'0': '2', '1': '1'},
        '2': {'0': '0', '1': '0'}
    },
    initial_state='0',
    final_states={'1'}
)

# getting the required vector of size n + 1
ans_vector = [n]

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
            while(len(bin_string) < 2*n):
                bin_string = '0' + bin_string
                if (A.accepts_input(bin_string)):
                    count = count + 1
        ans_vector.append(count)

# printing the transitions in the DFA
print("transitions:")
for i in range(0 , n):
    print("\t" + str(i) + ": " + str(A.transitions[str(i)]))
print("initial state: " + A.initial_state)
print("final states: " + str(A.final_states))
print("Answer vector: " + str(ans_vector))
print("----------x----------x----------")





