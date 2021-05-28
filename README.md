# angluin-style-learning
The `primes.py` file is used to generate the first `N` primes. The `main.py` file does the main job: given a DFA with `N` states, it computes a vector of length `N+1` whose coordinates are as follows: the first coordinate is `N`. The subsequent coordinates are the cardinalities of the intersection of the language of the DFA with the languages corresponding to each remainder modulo each prime, till the first `N` primes. Also, we only consider binary strings of length atmost `N`.

# How to set up the virtual environment?
Just use `pipenv` to set up the virtual environment using the given configuration files. We only use the [automata-lib](https://github.com/caleb531/automata) library along with other standard libraries.
