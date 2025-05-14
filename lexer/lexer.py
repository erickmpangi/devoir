import sys


def load_dfa(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    symbols = lines[0].split(',')
    transitions = {}
    accept_states = set()

    for line in lines[1:]:
        state, trans = line.split(':')
        trans = trans.split(',')
        transitions[state] = trans

        if state.isupper():  # Convention: Uppercase states are accepting states
            accept_states.add(state)

    return symbols, transitions, accept_states


def tokenize(input_string, symbols, transitions, accept_states):
    state = '1'  # Initial state is always '1'
    token = ""
    tokens = []

    for char in input_string:
        if char not in symbols:
            raise ValueError(f"Unexpected character '{char}' in input")

        next_state = transitions[state][symbols.index(char)]

        if next_state == '8':  # '8' represents an error state
            raise ValueError(f"Unexpected character '{char}' at position {len(token)}")

        token += char
        state = next_state

        if state in accept_states:
            tokens.append(token)
            token = ""
            state = '1'  # Reset to initial state

    if token:
        raise ValueError("Unrecognized token at end of input")

    return tokens


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python lexer.py <dfa_file> <input_string>")
        sys.exit(1)

    dfa_file = sys.argv[1]
    input_string = sys.argv[2]

    symbols, transitions, accept_states = load_dfa(dfa_file)
    tokens = tokenize(input_string, symbols, transitions, accept_states)
    print("Tokens:", tokens)
