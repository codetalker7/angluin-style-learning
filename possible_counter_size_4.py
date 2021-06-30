
from automata.fa.dfa import DFA
import language_dfa
import answer_vector


A = DFA(
    states={'0', '1', '2', '3'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '2', '1': '0'},
        '1': {'0': '1', '1': '2'},
        '2': {'0': '3', '1': '0'},
        '3': {'0': '1', '1': '0'}
    },
    initial_state='0',
    final_states={'1'}
)

B = DFA(
    states={'0', '1', '2', '3'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '2', '1': '2'},
        '1': {'0': '0', '1': '2'},
        '2': {'0': '3', '1': '2'},
        '3': {'0': '1', '1': '2'}
    },
    initial_state='0',
    final_states={'1'}
)

L_A = language_dfa.get_language(A,4)
L_B = language_dfa.get_language(B,4)

v_A = answer_vector.get_vector(A,4)
v_B = answer_vector.get_vector(B,4)

print (L_A)
print ("\n")
print (v_A)
print ("\n\n\n")
print (L_B)
print ("\n")
print (v_B)