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
# counterexample1
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

# counterexample2
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
# counterexample1
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

# counterexample2
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

# counterexample3
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

# counterexample4
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

# counterexample5
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


