import streamlit as st
import json
import os

DATA_FILE = "course_data.json"

# Default GA mapping structure
DEFAULT_GA_MAPPING = [
    {
        "GA": "Engineering Knowledge",
        "PO1": "√", "PO2": "", "PO3": "", "PO4": "", "PO5": "", "PO6": "",
        "PO7": "", "PO8": "", "PO9": "", "PO10": "", "PO11": "", "PO12": ""
    },
    {
        "GA": "Problem Analysis",
        "PO1": "", "PO2": "√", "PO3": "", "PO4": "", "PO5": "", "PO6": "",
        "PO7": "", "PO8": "", "PO9": "", "PO10": "", "PO11": "", "PO12": ""
    },
    {
        "GA": "Design/Development of Solutions",
        "PO1": "", "PO2": "", "PO3": "√", "PO4": "", "PO5": "", "PO6": "",
        "PO7": "", "PO8": "", "PO9": "", "PO10": "", "PO11": "", "PO12": ""
    },
    {
        "GA": "Conduct Investigations of Complex Problems",
        "PO1": "", "PO2": "", "PO3": "", "PO4": "√", "PO5": "", "PO6": "",
        "PO7": "", "PO8": "", "PO9": "", "PO10": "", "PO11": "", "PO12": ""
    },
    {
        "GA": "Modern Tool Usage",
        "PO1": "", "PO2": "", "PO3": "", "PO4": "", "PO5": "√", "PO6": "",
        "PO7": "", "PO8": "", "PO9": "", "PO10": "", "PO11": "", "PO12": ""
    },
    {
        "GA": "The Engineer and Society",
        "PO1": "", "PO2": "", "PO3": "", "PO4": "", "PO5": "", "PO6": "√",
        "PO7": "", "PO8": "", "PO9": "", "PO10": "", "PO11": "", "PO12": ""
    },
    {
        "GA": "Environment and Sustainability",
        "PO1": "", "PO2": "", "PO3": "", "PO4": "", "PO5": "", "PO6": "",
        "PO7": "√", "PO8": "", "PO9": "", "PO10": "", "PO11": "", "PO12": ""
    },
    {
        "GA": "Ethics",
        "PO1": "", "PO2": "", "PO3": "", "PO4": "", "PO5": "", "PO6": "",
        "PO7": "", "PO8": "√", "PO9": "", "PO10": "", "PO11": "", "PO12": ""
    },
    {
        "GA": "Individual and Team Work",
        "PO1": "", "PO2": "", "PO3": "", "PO4": "", "PO5": "", "PO6": "",
        "PO7": "", "PO8": "", "PO9": "√", "PO10": "", "PO11": "", "PO12": ""
    },
    {
        "GA": "Communication",
        "PO1": "", "PO2": "", "PO3": "", "PO4": "", "PO5": "", "PO6": "",
        "PO7": "", "PO8": "", "PO9": "", "PO10": "√", "PO11": "", "PO12": ""
    },
    {
        "GA": "Project Management and Finance",
        "PO1": "", "PO2": "", "PO3": "", "PO4": "", "PO5": "", "PO6": "",
        "PO7": "", "PO8": "", "PO9": "", "PO10": "", "PO11": "√", "PO12": ""
    },
    {
        "GA": "Life Long Learning",
        "PO1": "", "PO2": "", "PO3": "", "PO4": "", "PO5": "", "PO6": "",
        "PO7": "", "PO8": "", "PO9": "", "PO10": "", "PO11": "", "PO12": "√"
    }
]

def load_data():
    """
    Load existing data from 'course_data.json'.
    If 'ga_mapping' is missing, insert the default.
    """
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    # If 'ga_mapping' doesn't exist, add default structure
    if "ga_mapping" not in data:
        data["ga_mapping"] = DEFAULT_GA_MAPPING

    return data

def save_data(data):
    """
    Write the updated data dictionary back to 'course_data.json'.
    """
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    st.set_page_config(page_title="Graduate Attributes Mapping", layout="wide")
    st.title("3. Graduate Attribute (GA) Relate to Program outcome (PO)")

    # Load data, ensuring 'ga_mapping' is present
    data = load_data()
    ga_mapping = data["ga_mapping"]  # Now guaranteed to exist

    st.write("Below is the table showing Graduate Attributes (GA) vs. Program Outcomes (PO1–PO12).")
    st.write("You can edit each cell (add or remove '√'), then click 'Save GA-PO Mapping'.")

    # Display data_editor for editing
    edited_ga_mapping = st.data_editor(
        ga_mapping,
        key="ga_mapping_editor",
        num_rows="dynamic",
        use_container_width=True
    )

    # Save button
    if st.button("Save GA-PO Mapping"):
        data["ga_mapping"] = edited_ga_mapping
        save_data(data)
        st.success("GA-PO Mapping saved successfully!")

if __name__ == "__main__":
    main()
