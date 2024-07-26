import streamlit as st
import itertools
import yaml
import pyperclip

def generate_combinations(items):
    all_combinations = []
    for r in range(1, len(items) + 1):
        combinations = list(itertools.combinations(items, r))
        all_combinations.extend([list(combo) for combo in combinations])
    return all_combinations

def format_yaml_output(combinations):
    yaml_dict = {"combination": combinations}
    return yaml.dump(yaml_dict, sort_keys=False, default_flow_style=False)


st.title("Combination Generator")

# Input field for items
items_input = st.text_input("Enter items (comma-separated):")

# Initialize session state for YAML output
if 'yaml_output' not in st.session_state:
    st.session_state.yaml_output = ""

if st.button("Generate Combinations"):
    if items_input:
        # Split the input string into a list of items
        items = [item.strip() for item in items_input.split(',')]

        # Generate all combinations
        all_combinations = generate_combinations(items)

        # Generate YAML output
        st.session_state.yaml_output = format_yaml_output(all_combinations)
    else:
        st.warning("Please enter some items.")

# Display YAML output
if st.session_state.yaml_output:
    st.subheader("YAML Output:")
    st.text_area("", st.session_state.yaml_output, height=300, key="output_area")

    # Add a copy button
    if st.button("Copy Output"):
        pyperclip.copy(st.session_state.yaml_output)
        st.success("Output copied to clipboard!")