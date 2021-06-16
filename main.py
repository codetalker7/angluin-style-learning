from automata.fa.dfa import DFA
import answer_vector
import all_one_dfa

# iterating over all n state DFAs
# all_one_dfa.all_one_dfa(3, minimal_only=False, count=15000)

# n state DFAs with initial state 0
# all_one_dfa.all_one_dfa(3, minimal_only=False, count=10000, init_state=0)

all_one_dfa.all_one_dfa(3, minimal_only=False, count=10000, init_state=0)