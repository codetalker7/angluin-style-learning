from automata.fa.dfa import DFA
import answer_vector

# n represents the number of states in the DFA
n = 3

# defining the DFA A
A = DFA(
    states={'0', '1', '2'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '1', '1': '1'},
        '1': {'0': '0', '1': '2'},
        '2': {'0': '1', '1': '1'}
    },
    initial_state='1',
    final_states={'2'}
)
A = [(0 , 0)]
print(A[len(A) - 1])

