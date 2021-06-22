from automata.fa.dfa import DFA
import answer_vector
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
print(answer_vector.get_vector(A, 3))
print(A.transitions)
B = "" + str(A.transitions)
print(B)

C = DFA(
    states={'A', 'B', 'C', 'D'},
    input_symbols={'0', '1'},
    transitions={
        'A': {'0': 'A', '1': 'B'},
        'B': {'0': 'A', '1': 'C'},
        'C': {'0': 'C', '1': 'B'},
        'D': {'0': 'C', '1': 'A'}
    },
    initial_state='A',
    final_states={'B'}
)

AA = A.minify()
CC = C.minify()
print(AA == CC)
print(AA.transitions)
print(CC.transitions)
print(A == AA)
if(A.accepts_input("")): print("toto") 
else: print("tata")
print("an"[1:] + "oui")
print(bin(14))
print(bin(14)[2:])