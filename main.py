import streamlit as st
import itertools
import yaml

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

if st.button("Generate Combinations"):
    if items_input:
        # Split the input string into a list of items
        items = [item.strip() for item in items_input.split(',')]

        # Generate all combinations
        all_combinations = generate_combinations(items)

        # Generate and display YAML output
        yaml_output = format_yaml_output(all_combinations)
        st.subheader("YAML Output:")
        st.code(yaml_output, language="yaml")

        st.info("To copy the output, click the copy button in the top-right corner of the code block above.")
    else:
        st.warning("Please enter some items.")