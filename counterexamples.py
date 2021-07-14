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

# 33

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

# 33

'''
    counter examples for data:
    states = 4
    primes = 4
    max_length = 9 (2n + 1) 
'''
# counterexample1 for 2n+1
# It is a counter example for length 9, 13, 15, 19, 21 (which is surprising, as it is not exactly periodic (rather semi-linear)).
'''
A = DFA(
    states={'0', '1', '2', '3'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '2', '1': '3'},
        '1': {'0': '2', '1': '3'},
        '2': {'0': '3', '1': '0'},
        '3': {'0': '2', '1': '1'}
    },
    initial_state='0',
    final_states={'1'}
)
B = DFA(
    states={'0', '1', '2', '3'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '2', '1': '3'},
        '1': {'0': '3', '1': '2'},
        '2': {'0': '3', '1': '2'},
        '3': {'0': '2', '1': '1'}
    },
    initial_state='0',
    final_states={'1'}
)
# to see whether these DFAs are different, see if their
# answer vectors are different for different primes
print(new_answer_vector.get_vector(A, 4, max_length=9, no_of_primes=4))
print(new_answer_vector.get_vector(B, 4, max_length=9, no_of_primes=4))
if (new_answer_vector.get_vector(A, 4, max_length=9, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=9, no_of_primes=4)):
    print("true for 9")
if (new_answer_vector.get_vector(A, 4, max_length=10, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=10, no_of_primes=4)):
    print("true for 10")
if (new_answer_vector.get_vector(A, 4, max_length=11, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=11, no_of_primes=4)):
    print("true for 11")
if (new_answer_vector.get_vector(A, 4, max_length=12, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=12, no_of_primes=4)):
    print("true for 12")
if (new_answer_vector.get_vector(A, 4, max_length=13, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=13, no_of_primes=4)):
    print("true for 13")
if (new_answer_vector.get_vector(A, 4, max_length=14, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=14, no_of_primes=4)):
    print("true for 14")
if (new_answer_vector.get_vector(A, 4, max_length=15, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=15, no_of_primes=4)):
    print("true for 15")
if (new_answer_vector.get_vector(A, 4, max_length=16, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=16, no_of_primes=4)):
    print("true for 16")
if (new_answer_vector.get_vector(A, 4, max_length=17, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=17, no_of_primes=4)):
    print("true for 17")
if (new_answer_vector.get_vector(A, 4, max_length=18, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=18, no_of_primes=4)):
    print("true for 18")
if (new_answer_vector.get_vector(A, 4, max_length=19, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=19, no_of_primes=4)):
    print("true for 19")
if (new_answer_vector.get_vector(A, 4, max_length=20, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=20, no_of_primes=4)):
    print("true for 20")
if (new_answer_vector.get_vector(A, 4, max_length=21, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=21, no_of_primes=4)):
    print("true for 21")
'''

# counter-example 2 for 2n+1
# Same as above (it seems that most counter-examples for the same values have similar behaviours.)
'''
A = DFA(
    states={'0', '1', '2', '3'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '2', '1': '2'},
        '1': {'0': '2', '1': '2'},
        '2': {'0': '3', '1': '1'},
        '3': {'0': '3', '1': '0'}
    },
    initial_state='0',
    final_states={'1'}
)
B = DFA(
    states={'0', '1', '2', '3'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '2', '1': '2'},
        '1': {'0': '3', '1': '2'},
        '2': {'0': '3', '1': '1'},
        '3': {'0': '3', '1': '2'}
    },
    initial_state='0',
    final_states={'1'}
)
# to see whether these DFAs are different, see if their
# answer vectors are different for different primes
print(new_answer_vector.get_vector(A, 4, max_length=9, no_of_primes=4))
print(new_answer_vector.get_vector(B, 4, max_length=9, no_of_primes=4))
if (new_answer_vector.get_vector(A, 4, max_length=9, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=9, no_of_primes=4)):
    print("true for 9")
if (new_answer_vector.get_vector(A, 4, max_length=10, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=10, no_of_primes=4)):
    print("true for 10")
if (new_answer_vector.get_vector(A, 4, max_length=11, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=11, no_of_primes=4)):
    print("true for 11")
if (new_answer_vector.get_vector(A, 4, max_length=12, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=12, no_of_primes=4)):
    print("true for 12")
if (new_answer_vector.get_vector(A, 4, max_length=13, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=13, no_of_primes=4)):
    print("true for 13")
if (new_answer_vector.get_vector(A, 4, max_length=14, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=14, no_of_primes=4)):
    print("true for 14")
if (new_answer_vector.get_vector(A, 4, max_length=15, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=15, no_of_primes=4)):
    print("true for 15")
if (new_answer_vector.get_vector(A, 4, max_length=16, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=16, no_of_primes=4)):
    print("true for 16")
if (new_answer_vector.get_vector(A, 4, max_length=17, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=17, no_of_primes=4)):
    print("true for 17")
if (new_answer_vector.get_vector(A, 4, max_length=18, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=18, no_of_primes=4)):
    print("true for 18")
if (new_answer_vector.get_vector(A, 4, max_length=19, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=19, no_of_primes=4)):
    print("true for 19")
if (new_answer_vector.get_vector(A, 4, max_length=20, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=20, no_of_primes=4)):
    print("true for 20")
if (new_answer_vector.get_vector(A, 4, max_length=21, no_of_primes=4) == new_answer_vector.get_vector(B, 4, max_length=21, no_of_primes=4)):
    print("true for 21")
'''
