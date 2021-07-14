
from automata.fa.dfa import DFA
import answer_vector
import all_one_dfa

# iterating over all n state DFAs
# all_one_dfa.all_one_dfa(3, count=15000)

# n state DFAs with initial state 0
all_one_dfa.all_one_dfa(4, count=50000000, init_state=0,
                        minimalOnly=True, no_of_primes=4, max_length=9, vec=(0, 170, 54, 58, 58, 34, 34, 34, 34, 34, 25, 24, 24, 24, 24, 25, 24))

# A = DFA(
#    states={'0', '1', '2'},
#    input_symbols={'0', '1'},
#    transitions={
#        '0': {'0': '0', '1': '1'},
#        '1': {'0': '0', '1': '2'},
#        '2': {'0': '2', '1': '1'}
#    },
#    initial_state='0',
#    final_states={'1'}
# )
#print(answer_vector.get_vector(A, 3))
