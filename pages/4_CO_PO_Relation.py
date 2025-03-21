import streamlit as st
import json
import os

DATA_FILE = "course_data.json"

# Default numeric table for CO vs. PO1..PO12
DEFAULT_CO_PO_TABLE = [
    {
        "CO": "ITC404.1",
        "PO1": "3", "PO2": "", "PO3": "", "PO4": "", "PO5": "", "PO6": "",
        "PO7": "", "PO8": "", "PO9": "", "PO10": "", "PO11": "", "PO12": ""
    },
    {
        "CO": "ITC404.2",
        "PO1": "", "PO2": "", "PO3": "", "PO4": "", "PO5": "", "PO6": "",
        "PO7": "", "PO8": "", "PO9": "", "PO10": "", "PO11": "", "PO12": ""
    },
    {
        "CO": "ITC404.3",
        "PO1": "", "PO2": "", "PO3": "", "PO4": "", "PO5": "", "PO6": "",
        "PO7": "", "PO8": "", "PO9": "", "PO10": "", "PO11": "", "PO12": ""
    },
    {
        "CO": "ITC404.4",
        "PO1": "", "PO2": "", "PO3": "", "PO4": "", "PO5": "", "PO6": "",
        "PO7": "", "PO8": "", "PO9": "", "PO10": "", "PO11": "", "PO12": ""
    },
    {
        "CO": "ITC404 (AVG)",
        "PO1": "2.5", "PO2": "3", "PO3": "3", "PO4": "2", "PO5": "", "PO6": "",
        "PO7": "", "PO8": "", "PO9": "", "PO10": "", "PO11": "", "PO12": ""
    },
    {
        "CO": "ITC404 (AVG)",
        "PO1": "2.6", "PO2": "3", "PO3": "3", "PO4": "2", "PO5": "", "PO6": "",
        "PO7": "", "PO8": "", "PO9": "", "PO10": "", "PO11": "", "PO12": ""
    }
]

# Default justification table
DEFAULT_CO_PO_JUSTIFICATION = [
    {
        "CO": "ITC404.1",
        "PO": "PO1",
        "Justification": "In this case, students are expected to learn the basic working of components inside CPU..."
    },
    {
        "CO": "ITC404.2",
        "PO": "PO2",
        "Justification": "In this case, students are expected to learn the syntax and structure of assembly language..."
    },
    {
        "CO": "ITC404.2",
        "PO": "PO4",
        "Justification": "During execution of different programs, students understand which flags and registers are affected..."
    },
    {
        "CO": "ITC404.3",
        "PO": "PO1",
        "Justification": "In this case, students are expected to understand how the memory unit is organized..."
    },
    {
        "CO": "ITC404.3",
        "PO": "PO2",
        "Justification": "Also students understand the importance of each memory type used in computer organization..."
    },
    {
        "CO": "ITC404.4",
        "PO": "PO3",
        "Justification": "In this case, students are expected to understand interfacing of different components..."
    },
    {
        "CO": "ITC404.4",
        "PO": "PO4",
        "Justification": "Students are expected to see how it is carried out with required tests. Substantial mapping..."
    }
    # Add more rows if needed
]

def load_data():
    """Load from course_data.json or return defaults if missing."""
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    # If section4_co_po doesn't exist, create it
    if "section4_co_po" not in data:
        data["section4_co_po"] = {
            "mapping": DEFAULT_CO_PO_TABLE,
            "justification": DEFAULT_CO_PO_JUSTIFICATION
        }
    else:
        # Make sure subkeys exist
        if "mapping" not in data["section4_co_po"]:
            data["section4_co_po"]["mapping"] = DEFAULT_CO_PO_TABLE
        if "justification" not in data["section4_co_po"]:
            data["section4_co_po"]["justification"] = DEFAULT_CO_PO_JUSTIFICATION

    return data

def save_data(data):
    """Write data to course_data.json."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    st.set_page_config(page_title="CO-PO Relation", layout="wide")
    st.title("4. Program Outcome (PO & PSO) related to Lab Outcomes (LO)")

    data = load_data()
    section4 = data["section4_co_po"]

    st.write("### CO vs. PO Table")
    st.write("Below is the numeric table showing how each CO maps to PO1–PO12.")
    # Show data_editor for "mapping"
    edited_mapping = st.data_editor(
        section4["mapping"],
        num_rows="dynamic",
        use_container_width=True,
        key="co_po_mapping_editor"
    )

    st.write("### CO-PO Justification")
    st.write("Below is a justification table describing each CO-PO link in words.")
    # Show data_editor for "justification"
    edited_justification = st.data_editor(
        section4["justification"],
        num_rows="dynamic",
        use_container_width=True,
        key="co_po_justification_editor"
    )

    if st.button("Save CO-PO Data"):
        # Update data in memory
        data["section4_co_po"]["mapping"] = edited_mapping
        data["section4_co_po"]["justification"] = edited_justification

        # Save to JSON
        save_data(data)
        st.success("CO-PO Data saved successfully!")

if __name__ == "__main__":
    main()
