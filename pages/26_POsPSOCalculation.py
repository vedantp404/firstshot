import streamlit as st
import json
import os

DATA_FILE = "course_data.json"

# Default data for Section 26
DEFAULT_POS_PSO_26 = [
    {
        "LO No.": "ITC404.1 Direct",
        "Mapped": "57.68",
        "Attainment": "2.13",
        "PO1": "",
        "PO2": "",
        "PO3": "",
        "PO4": "",
        "PO5": "",
        "PO6": "",
        "PO7": "",
        "PO8": "",
        "PO9": "",
        "PO10": "",
        "PO11": "",
        "PO12": "",
        "PSO1": "",
        "PSO2": ""
    },
    {
        "LO No.": "ITC404.1 Level",
        "Mapped": "",
        "Attainment": "",
        "PO1": "2",
        "PO2": "",
        "PO3": "",
        "PO4": "",
        "PO5": "",
        "PO6": "",
        "PO7": "",
        "PO8": "",
        "PO9": "",
        "PO10": "",
        "PO11": "",
        "PO12": "",
        "PSO1": "2",
        "PSO2": ""
    },
    {
        "LO No.": "ITC404.2 Direct",
        "Mapped": "57.68",
        "Attainment": "2.13",
        "PO1": "",
        "PO2": "",
        "PO3": "",
        "PO4": "",
        "PO5": "",
        "PO6": "",
        "PO7": "",
        "PO8": "",
        "PO9": "",
        "PO10": "",
        "PO11": "",
        "PO12": "",
        "PSO1": "",
        "PSO2": ""
    },
    {
        "LO No.": "Weighted avg. Direct attainment",
        "Mapped": "",
        "Attainment": "",
        "PO1": "50.72",
        "PO2": "57.68",
        "PO3": "57.68",
        "PO4": "38.42",
        "PO5": "",
        "PO6": "",
        "PO7": "",
        "PO8": "",
        "PO9": "",
        "PO10": "",
        "PO11": "",
        "PO12": "",
        "PSO1": "38.42",
        "PSO2": ""
    },
    {
        "LO No.": "Weighted avg. Direct Level",
        "Mapped": "",
        "Attainment": "",
        "PO1": "1.86",
        "PO2": "2.13",
        "PO3": "2.13",
        "PO4": "1.41",
        "PO5": "",
        "PO6": "",
        "PO7": "",
        "PO8": "",
        "PO9": "",
        "PO10": "",
        "PO11": "",
        "PO12": "",
        "PSO1": "1.41",
        "PSO2": ""
    }
]

def load_data():
    """
    Load or create default data for 'pos_pso_calc_26'.
    """
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    # If 'pos_pso_calc_26' not in data, add default structure
    if "pos_pso_calc_26" not in data:
        data["pos_pso_calc_26"] = DEFAULT_POS_PSO_26

    return data

def save_data(data):
    """Write data to course_data.json."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    st.set_page_config(page_title="POs and PSO calculation (Weighted average)", layout="wide")
    st.title("26. POs and PSO calculation (Weighted average) (Year: 2017-2018)")

    data = load_data()
    pos_pso_table = data["pos_pso_calc_26"]

    st.write("Below is the table that calculates Weighted Average for POs and PSOs based on LO No. (direct/mapped/attainment).")

    # Editable table
    edited_table = st.data_editor(
        pos_pso_table,
        num_rows="dynamic",
        use_container_width=True,
        key="pos_pso_calc_26_editor"
    )

    if st.button("Save POs & PSOs Weighted Calculation"):
        data["pos_pso_calc_26"] = edited_table
        save_data(data)
        st.success("POs & PSOs Weighted Calculation data saved successfully!")

if __name__ == "__main__":
    main()
