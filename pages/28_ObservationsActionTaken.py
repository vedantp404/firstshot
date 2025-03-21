import streamlit as st
import json
import os

DATA_FILE = "course_data.json"

# Default data for Section 28
DEFAULT_SECTION_28 = [
    {
        "Category": "PO1",
        "Target Level": "2.6",
        "Attainment Level (Direct)": "1.86",
        "Observations/Analysis": "1.\n2."
    },
    {
        "Category": "Action",
        "Target Level": "",
        "Attainment Level (Direct)": "",
        "Observations/Analysis": "1.\n2."
    },
    {
        "Category": "PO2",
        "Target Level": "3",
        "Attainment Level (Direct)": "2.13",
        "Observations/Analysis": "1.\n2."
    },
    {
        "Category": "Action",
        "Target Level": "",
        "Attainment Level (Direct)": "",
        "Observations/Analysis": "1.\n2."
    },
    {
        "Category": "PO3",
        "Target Level": "3",
        "Attainment Level (Direct)": "2.13",
        "Observations/Analysis": "1.\n2."
    },
    {
        "Category": "Action",
        "Target Level": "",
        "Attainment Level (Direct)": "",
        "Observations/Analysis": "1.\n2."
    },
    {
        "Category": "PO4",
        "Target Level": "2",
        "Attainment Level (Direct)": "1.41",
        "Observations/Analysis": "1.\n2."
    },
    {
        "Category": "Action",
        "Target Level": "",
        "Attainment Level (Direct)": "",
        "Observations/Analysis": "1.\n2."
    },
    {
        "Category": "PSO1",
        "Target Level": "2",
        "Attainment Level (Direct)": "1.41",
        "Observations/Analysis": "1.\n2."
    },
    {
        "Category": "Action",
        "Target Level": "",
        "Attainment Level (Direct)": "",
        "Observations/Analysis": "1.\n2."
    }
]

def load_data():
    """
    Load or create default data for 'observations_actions_28'.
    """
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    # If 'observations_actions_28' not in data, set default
    if "observations_actions_28" not in data:
        data["observations_actions_28"] = DEFAULT_SECTION_28

    return data

def save_data(data):
    """Write data to course_data.json."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    st.set_page_config(page_title="Observations and Action Taken (Sec 28)", layout="wide")
    st.title("28. Observations and Action Taken (Year: 2017-2018)")

    data = load_data()
    obs_actions_table = data["observations_actions_28"]

    st.write("Below is the table showing each PO/PSO's Target Level, Attainment Level (Direct), and Observations/Analysis, plus an Action row.")

    # Editable table
    edited_table = st.data_editor(
        obs_actions_table,
        num_rows="dynamic",
        use_container_width=True,
        key="obs_actions_28_editor"
    )

    if st.button("Save Observations & Actions"):
        data["observations_actions_28"] = edited_table
        save_data(data)
        st.success("Observations & Actions data saved successfully!")

if __name__ == "__main__":
    main()
