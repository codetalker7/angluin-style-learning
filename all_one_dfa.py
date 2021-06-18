from automata.fa.dfa import DFA
import json
import answer_vector

def pretty_print(dict):
    print (json.dumps(dict, indent=2, default=str))

def all_one_dfa(n, count=None, init_state=None, final_state=None):
    """
        n is the number of states in the DFAs. This 
        method prints a list of all possible answer 
        vectors (over minimal DFAs only) along with 
        their frequencies. The flag minimal_only determines
        if the iteration is done only over minimal DFAs
        or all DFAs. If init_state is not None, the iteration
        is only done over DFAs having initial state equal to 
        init_state. If final_state is not None, the iteration 
        is done over only those DFAs whose final state is final_state.
    """
    # total count
    total_count = 0

    # dictionary of the frequencies of vectors
    freq_vectors = {}

    # creating the set of states
    states = []
    for i in range(0, n):
        states.append(str(i))

    # creating the set of input symbols
    input_symbols={'0', '1'}

    #iterating over all possible transitions, initial_state and final_states
    for i in range(0, n):
        # i is the initial state
        if (init_state != None and init_state != i):
            continue
        initial_state = str(i)

        for j in range(0, n):
            # j is the final state
            if (final_state != None and final_state != j):
                continue
            final_states = {str(j)}

            #iterating through all possible transitions
            transitions = {}
            iter_stack = [(0, 0)]
            while(len(iter_stack) > 0):
                if (len(iter_stack) <= n - 1):
                    # if the top element of the stack is > (n - 1, n - 1), pop it
                    if (iter_stack[len(iter_stack) - 1] > (n - 1, n - 1)):
                        iter_stack.pop()
                        continue

                    (x, y) = iter_stack[len(iter_stack) - 1]
                    transitions[str(len(iter_stack) - 1)] = {'0': str(x), '1': str(y)}

                    # updating (x, y)
                    if (y < n - 1):
                        y = y + 1
                    else:
                        x = x + 1
                        y = 0
                    iter_stack[len(iter_stack) - 1] = (x, y)

                    #push (0, 0) onto the stack
                    iter_stack.append((0, 0))
                else:
                    iter_stack.pop()
                    for p in range(0, n):
                        for q in range(0, n):
                            transitions[str(n - 1)] = {'0': str(p), '1': str(q)}

                            # at this point, we have enumerated a DFA
                            total_count = total_count + 1
                            A = DFA(
                                states = set(states),
                                input_symbols = input_symbols,
                                transitions = transitions,
                                initial_state = initial_state,
                                final_states = final_states
                            )
                            v = str(answer_vector.get_vector(A, n))
                            if v in freq_vectors.keys():
                                freq_vectors[v] = freq_vectors[v] + 1
                            else: 
                                freq_vectors[v] = 1
                            if (count != None and total_count == count):
                                # printing the dictionary
                                pretty_print(freq_vectors)
                                return
    
    # printing the dictionary
    pretty_print(freq_vectors)
