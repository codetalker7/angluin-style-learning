from automata.fa.dfa import DFA
import answer_vector
import new_answer_vector
import all_one_dfa

'''
    counter examples for data:
    states = 3
    primes = 3
    max_length = 4 (2n - 2) 
'''
# counterexample1 for 2n-2
# Not periodic
'''
A = DFA(
    states={'0', '1', '2'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '0', '1': '1'},
        '1': {'0': '1', '1': '2'},
        '2': {'0': '2', '1': '0'}
    },
    initial_state='0',
    final_states={'0'}
)
B = DFA(
    states={'0', '1', '2'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '1', '1': '1'},
        '1': {'0': '2', '1': '2'},
        '2': {'0': '0', '1': '2'}
    },
    initial_state='0',
    final_states={'1'}
)
# to see whether these DFAs are different, see if their 
# answer vectors are different for different primes
print(new_answer_vector.get_vector(A, 3, max_length=4, no_of_primes=4))
print(new_answer_vector.get_vector(B, 3, max_length=4, no_of_primes=4))
print(new_answer_vector.get_vector(A, 3, max_length=4, no_of_primes=4) == new_answer_vector.get_vector(B, 3, max_length=4, no_of_primes=4))
'''

# counterexample2 for 2n-2
# Not periodic
'''
A = DFA(
    states={'0', '1', '2'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '1', '1': '0'},
        '1': {'0': '2', '1': '0'},
        '2': {'0': '2', '1': '0'}
    },
    initial_state='0',
    final_states={'1'}
)
B = DFA(
    states={'0', '1', '2'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '1', '1': '0'},
        '1': {'0': '2', '1': '2'},
        '2': {'0': '0', '1': '0'}
    },
    initial_state='0',
    final_states={'1'}
)
# to see whether these DFAs are different, see if their 
# answer vectors are different for different primes
print(new_answer_vector.get_vector(A, 3, max_length=4, no_of_primes=4))
print(new_answer_vector.get_vector(B, 3, max_length=4, no_of_primes=4))
print(new_answer_vector.get_vector(A, 3, max_length=4, no_of_primes=4) == new_answer_vector.get_vector(B, 3, max_length=4, no_of_primes=4))
'''

#########################################33

'''
    counter examples for data:
    states = 3
    primes = 3
    max_length = 5 (2n - 1) 
'''
# counterexample1 for 2n-1
# Does not seem periodic, but has some periodic feature (the number of words is the same for 3 consecutive length, then different for the 3 next, etc; when lengths are equal, vector for prime 5 as well)
'''
A = DFA(
    states={'0', '1', '2'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '0', '1': '1'},
        '1': {'0': '1', '1': '2'},
        '2': {'0': '2', '1': '0'}
    },
    initial_state='0',
    final_states={'0'}
)
B = DFA(
    states={'0', '1', '2'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '2', '1': '1'},
        '1': {'0': '2', '1': '0'},
        '2': {'0': '1', '1': '0'}
    },
    initial_state='0',
    final_states={'1'}
)
# to see whether these DFAs are different, see if their 
# answer vectors are different for different primes
print(new_answer_vector.get_vector(A, 3, max_length=5, no_of_primes=4))
print(new_answer_vector.get_vector(B, 3, max_length=5, no_of_primes=4))
print(new_answer_vector.get_vector(A, 3, max_length=5, no_of_primes=4) == new_answer_vector.get_vector(B, 3, max_length=5, no_of_primes=4))
'''

# counterexample2 for 2n-1
# So this one is funny. It is periodic with period 4. But, for length 13, the vectors are also equal for prime 7, but not for prime 11. Though for length 21, it is equal for prime 11 but not prime 7, and for length 17, it is different for both. It is of course difficult to explore further.
'''
A = DFA(
    states={'0', '1', '2'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '0', '1': '1'},
        '1': {'0': '0', '1': '2'},
        '2': {'0': '0', '1': '2'}
    },
    initial_state='0',
    final_states={'1'}
)
B = DFA(
    states={'0', '1', '2'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '2', '1': '1'},
        '1': {'0': '2', '1': '1'},
        '2': {'0': '2', '1': '0'}
    },
    initial_state='0',
    final_states={'1'}
)
# to see whether these DFAs are different, see if their 
# answer vectors are different for different primes
print(new_answer_vector.get_vector(A, 3, max_length=5, no_of_primes=4))
print(new_answer_vector.get_vector(B, 3, max_length=5, no_of_primes=4))
print(new_answer_vector.get_vector(A, 3, max_length=5, no_of_primes=4) == new_answer_vector.get_vector(B, 3, max_length=5, no_of_primes=4))
'''

# counterexample3 for 2n-1.
# It is exactly as the previous ones. Actually, the vectors are also almost the same (one word of difference in total, all positions equal but one).
'''
A = DFA(
    states={'0', '1', '2'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '0', '1': '2'},
        '1': {'0': '0', '1': '1'},
        '2': {'0': '0', '1': '1'}
    },
    initial_state='0',
    final_states={'1'}
)
B = DFA(
    states={'0', '1', '2'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '2', '1': '0'},
        '1': {'0': '2', '1': '0'},
        '2': {'0': '2', '1': '1'}
    },
    initial_state='0',
    final_states={'1'}
)
# to see whether these DFAs are different, see if their 
# answer vectors are different for different primes
print(new_answer_vector.get_vector(A, 3, max_length=5, no_of_primes=4))
print(new_answer_vector.get_vector(B, 3, max_length=5, no_of_primes=4))
print(new_answer_vector.get_vector(A, 3, max_length=5, no_of_primes=4) == new_answer_vector.get_vector(B, 3, max_length=5, no_of_primes=4))
'''

# counterexample4 for 2n-1
# It has exactly the same vectors as the previous one, but the even and odds are exchanged.
'''
A = DFA(
    states={'0', '1', '2'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '0', '1': '2'},
        '1': {'0': '0', '1': '2'},
        '2': {'0': '1', '1': '2'}
    },
    initial_state='0',
    final_states={'1'}
)
B = DFA(
    states={'0', '1', '2'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '2', '1': '0'},
        '1': {'0': '1', '1': '0'},
        '2': {'0': '1', '1': '0'}
    },
    initial_state='0',
    final_states={'1'}
)
# to see whether these DFAs are different, see if their 
# answer vectors are different for different primes
print(new_answer_vector.get_vector(A, 3, max_length=5, no_of_primes=4))
print(new_answer_vector.get_vector(B, 3, max_length=5, no_of_primes=4))
print(new_answer_vector.get_vector(A, 3, max_length=5, no_of_primes=4) == new_answer_vector.get_vector(B, 3, max_length=5, no_of_primes=4))
'''

# counterexample5 for 2n-1
# Exactly the same as the previous, but with one more word (same as between the 2nd and 3rd).
'''
A = DFA(
    states={'0', '1', '2'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '1', '1': '0'},
        '1': {'0': '2', '1': '0'},
        '2': {'0': '2', '1': '0'}
    },
    initial_state='0',
    final_states={'1'}
)
B = DFA(
    states={'0', '1', '2'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '1', '1': '2'},
        '1': {'0': '1', '1': '2'},
        '2': {'0': '0', '1': '2'}
    },
    initial_state='0',
    final_states={'1'}
)
# to see whether these DFAs are different, see if their 
# answer vectors are different for different primes
print(new_answer_vector.get_vector(A, 3, max_length=5, no_of_primes=4))
print(new_answer_vector.get_vector(B, 3, max_length=5, no_of_primes=4))
print(new_answer_vector.get_vector(A, 3, max_length=5, no_of_primes=4) == new_answer_vector.get_vector(B, 3, max_length=5, no_of_primes=4))
'''


