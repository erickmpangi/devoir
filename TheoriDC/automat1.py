import os
import sys

# 1. Check command-line arguments
if len(sys.argv) != 3:
    raise Exception("Usage instructions:\npython automaton.py <definition_file_path> <input_string>")

definition_file = sys.argv[1]
input_string = sys.argv[2].lower()

# 2. Verify the definition file exists
if not os.path.isfile(definition_file):
    raise Exception("Automaton definition file not found at the specified path: {}".format(definition_file))

# 3. Read the file content
with open(definition_file, "r", encoding="utf-8") as f:
    file_data = f.readlines()

if len(file_data) < 3:
    raise Exception("Invalid automaton definition format (must have at least 3 lines)")

vocab = file_data[0].replace("\n", "").split(",")
accept_states_line = file_data[-1].replace("\n", "")

state_lines = file_data[1:-1]
if not accept_states_line.lower().startswith("f:"):
    raise Exception("Please specify final states using 'F:<s1>,<s2>,...'")

if len(state_lines) == 0:
    raise Exception("The file does not contain a valid list of states.")

accepted_states = accept_states_line[2:].split(",")
state_table = {}

# 4. Build transition table
for state_line in state_lines:
    cleaned_line = state_line.strip()
    parts = cleaned_line.split(":")
    state_id = parts[0]
    transitions = parts[1].split(",")
    transition_dict = {symbol: transitions[idx] for idx, symbol in enumerate(vocab)}
    state_table[state_id] = transition_dict

# 5. Validate input string
input_symbols = list(input_string.strip())
invalid_symbols = list(set(input_symbols) - set(vocab))
if len(invalid_symbols) > 0:
    raise Exception("Input string contains symbols not in the vocabulary: {}".format(invalid_symbols))

# 6. Evaluate the string through the automaton
current_state = list(state_table.keys())[0]  # Start from the first defined state
for symbol in input_symbols:
    transitions = state_table.get(current_state)
    if not transitions:
        raise Exception("No transition defined for state '{}'.".format(current_state))
    next_state = transitions.get(symbol)
    if not next_state:
        raise Exception("Invalid transition from state '{}' using symbol '{}'.".format(current_state, symbol))
    current_state = next_state

# 7. Print result
if current_state in accepted_states:
    print("The string '{}' is accepted.".format(input_string))
else:
    print("The string '{}' is rejected.".format(input_string))
