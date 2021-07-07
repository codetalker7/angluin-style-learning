
from automata.fa.dfa import DFA
import language_dfa
import answer_vector
import new_answer_vector


A = DFA(
    states={'0', '1', '2', '3'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '2', '1': '2'},
        '1': {'0': '2', '1': '3'},
        '2': {'0': '1', '1': '2'},
        '3': {'0': '0', '1': '2'}
    },
    initial_state='0',
    final_states={'1'}
)

B = DFA(
    states={'0', '1', '2', '3'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '2', '1': '2'},
        '1': {'0': '3', '1': '0'},
        '2': {'0': '1', '1': '2'},
        '3': {'0': '1', '1': '0'}
    },
    initial_state='0',
    final_states={'1'}
)

v_A_2n = new_answer_vector.get_vector(A,4,max_length=8,no_of_primes=5)
v_B_2n = new_answer_vector.get_vector(B,4,max_length=8,no_of_primes=5)

v_A_2n1 = new_answer_vector.get_vector(A,4,max_length=9,no_of_primes=5)
v_B_2n1 = new_answer_vector.get_vector(B,4,max_length=9,no_of_primes=5)

v_A_2n2 = new_answer_vector.get_vector(A,4,max_length=10,no_of_primes=5)
v_B_2n2 = new_answer_vector.get_vector(B,4,max_length=10,no_of_primes=5)

v_A_2n3 = new_answer_vector.get_vector(A,4,max_length=11,no_of_primes=5)
v_B_2n3 = new_answer_vector.get_vector(B,4,max_length=11,no_of_primes=5)

v_A_3n = new_answer_vector.get_vector(A,4,max_length=12,no_of_primes=5)
v_B_3n = new_answer_vector.get_vector(B,4,max_length=12,no_of_primes=5)


print ("2n:")
print (v_A_2n)
print (v_B_2n)

print ("2n+1:")
print (v_A_2n1)
print (v_B_2n1)

print ("2n+2:")
print (v_A_2n2)
print (v_B_2n2)

print ("2n+3:")
print (v_A_2n3)
print (v_B_2n3)

print ("3n:")
print (v_A_3n)
print (v_B_3n)