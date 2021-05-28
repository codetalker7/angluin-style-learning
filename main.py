from typing import final
from automata.fa.dfa import DFA
import math

primes_file = open("primes.txt" , "r")
llist = primes_file.read()
primes_list = list(llist[:len(llist) - 1].split())

# n represents the number of states in the DFA
n = 3
upper_bound = 1 << n

# defining the DFA A
A = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q1'}
    },
    initial_state='q0',
    final_states={'q1'}
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
        ans_vector.append(count)

# printing the final answer
print(ans_vector)





