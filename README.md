# angluin-style-learning
The `primes.py` file is used to generate the first `N` primes. The module 
`answer_vector.py` contains two methods: `get_vector`, which, given an 
input DFA `A` along with its number of states `n`, computes its answer 
vector. The second method, `print_dfa`, simply prints the DFA in a neat 
form. 

The module `all_one_dfa.py` contains a method `all_one_dfa` which is used 
to iterate over a list of DFAs and make a dictionary consisting of possible
answer vectors along with their frequencies. 

# A few results
As of now, a few (not all complete) results are contained in the four text files.

# How to set up the virtual environment?
Just use `pipenv` to set up the virtual environment using the given configuration files. We only use the [automata-lib](https://github.com/caleb531/automata) library along with other standard libraries.
