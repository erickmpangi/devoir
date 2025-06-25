import os
import sys

from utils.common import load_automata_definition, update_vocab, print_table, qrip_input_trans, qrip_join_duplicate_paths

# Vérification des arguments
if len(sys.argv) != 2:
    raise Exception("Usage:\npython qrip_automatic.py <path_to_automaton_definition>")

definition_file = sys.argv[1]
if not os.path.isfile(definition_file):
    raise Exception("Automaton definition file not found at: {}".format(definition_file))

# Chargement de la définition de l'automate
vocab, accepted_states, states_definition = load_automata_definition(definition_file)

# Ajout des états de départ et de fin
all_states = list(states_definition.keys())
states_definition["qstart"] = {"€": all_states[0]}
states_definition["qend"] = {}

final_states = accepted_states[2:].split(",")
for fstate in final_states:
    states_definition[fstate]["€"] = "qend"

all_states = list(states_definition.keys())
vocab = update_vocab(states_definition)

print("Initial Transitions table")
print_table(vocab, states_definition)

# Copie de l'automate pour les modifications
states_definition_cpy = states_definition.copy()
node_elements = [x for x in states_definition_cpy.keys() if x not in ["qstart", "qend"]]

# Boucle de QRip
for idx, original_state in enumerate(node_elements):
    vocab = update_vocab(states_definition_cpy)
    out_trans = states_definition_cpy.pop(original_state)
    print("Iteration #{} - Node to delete: {}".format((idx + 1), original_state))
    print_table(vocab, states_definition_cpy)

    in_trans = qrip_input_trans(states_definition_cpy, original_state)

    for inc_state, inc_transitions in in_trans:
        base_transition = list(inc_transitions.keys())[0]
        for out_state in out_trans:
            if out_trans[out_state] == original_state:
                if "+" in out_state:
                    base_transition += "({})*".format(out_state)
                else:
                    base_transition += "({}*)".format(out_state)
        for out_state in out_trans:
            if out_trans[out_state] != original_state:
                str_transition = "({}{})".format(base_transition, out_state)
                states_definition_cpy[inc_state][str_transition] = out_trans[out_state]

    qrip_join_duplicate_paths(states_definition_cpy)

    for origin_state, transition in in_trans:
        del states_definition_cpy[origin_state][list(transition.keys())[0]]

    qstart_elements = states_definition_cpy["qstart"]
    transitions_to_delete = []
    transitions_to_append = []
    for qe in qstart_elements.values():
        tvalues = [x for x in qstart_elements.keys() if qstart_elements[x] == qe]
        if len(tvalues) > 1:
            merged_trans = "(" + "+".join(tvalues) + ")"
            transitions_to_append.append((merged_trans, qe))
            transitions_to_delete += tvalues

    transitions_to_delete = list(set(transitions_to_delete))
    for tdel in transitions_to_delete:
        del states_definition_cpy["qstart"][tdel]
    for tapp in transitions_to_append:
        states_definition_cpy["qstart"][tapp[0]] = tapp[1]

# Finalisation
vocab = update_vocab(states_definition_cpy)
print_table(vocab, states_definition_cpy)

qstart_keys = list(states_definition_cpy["qstart"].keys())
qstart_keys = sorted(qstart_keys)
regex = qstart_keys[0].replace("€", "")

print("Resulting REGEX")
print(regex)
