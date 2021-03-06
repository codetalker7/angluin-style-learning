from automata.fa.dfa import DFA
import json
import answer_vector
import new_answer_vector

def pretty_print(dict):
    print (json.dumps(dict, indent=2, default=str))

def all_one_dfa(n, count=None, init_state=None, final_state=None, minimalOnly=False, max_length=None, no_of_primes=None, vec=None, prime=None):
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
                            A = DFA(
                                states = set(states),
                                input_symbols = input_symbols,
                                transitions = transitions,
                                initial_state = initial_state,
                                final_states = final_states
                            )

                            # if minimalOnly=True and A is not minimal, skip it
                            if (minimalOnly and len(A.minify().states) < n):
                                continue
                            
                            vec1 = ()
                            # if prime is not none, call get_vector_one_prime
                            if (prime != None):
                                vec1 = new_answer_vector.get_vector_one_prime(A, n, max_length=max_length, prime=prime)
                            # otherwise call get_vector
                            else:
                                vec1 = new_answer_vector.get_vector(A, n, max_length=max_length, no_of_primes=no_of_primes)
                            v = str(vec1)
                            if v in freq_vectors.keys():
                                freq_vectors[v] = freq_vectors[v] + 1
                            else: 
                                freq_vectors[v] = 1

                            # printing the DFA if its vector matches vec
                            if (vec != None and vec1 == vec):
                                answer_vector.print_dfa(A, n)
                                print("-----x-----x-----")

                            # incrementing total count
                            total_count = total_count + 1

                            ##For verbosity, prefer the following instead of the previous.
                            #if v in freq_vectors.keys():
                            #    freq_vectors[v] = freq_vectors[v] + " ::: " + "(" + str(A.transitions) + "F:" + str(A.final_states) + ")"
                            #else: 
                            #    freq_vectors[v] = "(" + str(A.transitions) + "F:" + str(A.final_states) + ")"
                            if (count != None and total_count >= count and vec == None):
                                # printing the dictionary
                                pretty_print(freq_vectors)
                                return
    
    # printing the dictionary if vec is None
    if (vec == None):
        pretty_print(freq_vectors)

def get_final_states(bitset, n):
    final_states = set()
    bit_string = bin(bitset)[2:]

    # append zeros at the front of bit_string
    while (len(bit_string) < n):
        bit_string = '0' + bit_string

    for i in range(0, n):
        if (bit_string[i] == '1'):
            final_states.add(str(i))
    return final_states

def multiple_all_one_dfa(n, count=None, init_state=None, minimalOnly=False, max_length=None, no_of_primes=None, vec=None, prime=None):
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

        for bitset in range(1, (1 << n)):
            #  bitset represents the set of final states
            final_states = get_final_states(bitset, n)

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
                            A = DFA(
                                states = set(states),
                                input_symbols = input_symbols,
                                transitions = transitions,
                                initial_state = initial_state,
                                final_states = final_states
                            )

                            # if minimalOnly=True and A is not minimal, skip it
                            if (minimalOnly and len(A.minify().states) < n):
                                continue
                            
                            vec1 = ()
                            # if prime is not none, call get_vector_one_prime
                            if (prime != None):
                                vec1 = new_answer_vector.get_vector_one_prime(A, n, max_length=max_length, prime=prime)
                            # otherwise call get_vector
                            else:
                                vec1 = new_answer_vector.get_vector(A, n, max_length=max_length, no_of_primes=no_of_primes)
                            v = str(vec1)
                            if v in freq_vectors.keys():
                                freq_vectors[v] = freq_vectors[v] + 1
                            else: 
                                freq_vectors[v] = 1

                            # printing the DFA if its vector matches vec
                            if (vec != None and vec1 == vec):
                                answer_vector.print_dfa(A, n)
                                print("-----x-----x-----")
                            
                            # incrementing total count
                            total_count = total_count + 1

                            ##For verbosity, prefer the following instead of the previous.
                            #if v in freq_vectors.keys():
                            #    freq_vectors[v] = freq_vectors[v] + " ::: " + "(" + str(A.transitions) + "F:" + str(A.final_states) + ")"
                            #else: 
                            #    freq_vectors[v] = "(" + str(A.transitions) + "F:" + str(A.final_states) + ")"
                            if (count != None and total_count >= count and vec == None):
                                # printing the dictionary
                                pretty_print(freq_vectors)
                                return
    
    # printing the dictionary if vec is None
    if (vec == None):
        pretty_print(freq_vectors)