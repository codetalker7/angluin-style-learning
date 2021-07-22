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
# trying to see if a single prime separates the DFAs. Unfortunately, answer is no.
# all_one_dfa.all_one_dfa(3, init_state=0, minimalOnly=True, prime=7, max_length=6)

# call for multiple final states, n = 3
all_one_dfa.multiple_all_one_dfa(3, init_state=0, minimalOnly=True, no_of_primes=3, max_length=6)