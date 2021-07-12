"""
    https://gitlab.inria.fr/cpaperma/compaut
    VincentPenelle
    sreejithavtvm
"""

from automata.fa.dfa import DFA
import answer_vector
import new_answer_vector
import all_one_dfa

# iterating over all n state DFAs
# all_one_dfa.all_one_dfa(3, count=15000)

# n state DFAs with initial state 0
# all_one_dfa.all_one_dfa(3, count=50000, init_state=0)

A = DFA(
    states={'0', '1', '2'},
    input_symbols={'0', '1'},
    transitions={
        '0': {'0': '0', '1': '1'},
        '1': {'0': '0', '1': '2'},
        '2': {'0': '2', '1': '1'}
    },
    initial_state='0',
    final_states={'1'}
)
all_one_dfa.all_one_dfa(4, init_state=0, minimalOnly=True, no_of_primes=4, max_length=6, vec=(0, 21, 6, 9, 6, 4, 4, 5, 4, 4, 3, 3, 3, 3, 3, 3, 3))