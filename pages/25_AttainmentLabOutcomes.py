import streamlit as st
import json
import os

DATA_FILE = "course_data.json"

# Default data for Section 25
DEFAULT_LAB_OUTCOMES_25 = [
    {
        "Course Outcome": "ITC404.1",
        "Test 1": "55",
        "Test 2": "46",
        "Assignments": "55",
        "Attendance": "57",
        "Avg (X1)": "56.4",
        "Univ. (X2)": "57",
        "Total CO Attainment": "56.7"
    },
    {
        "Course Outcome": "ITC404.2",
        "Test 1": "46",
        "Test 2": "78",
        "Assignments": "46",
        "Attendance": "57",
        "Avg (X1)": "56.7",
        "Univ. (X2)": "53.7",
        "Total CO Attainment": "55.2"
    },
    {
        "Course Outcome": "ITC404.3",
        "Test 1": "78",
        "Test 2": "58",
        "Assignments": "78",
        "Attendance": "57",
        "Avg (X1)": "67.8",
        "Univ. (X2)": "63.3",
        "Total CO Attainment": "65.6"
    },
    {
        "Course Outcome": "ITC404.4",
        "Test 1": "58",
        "Test 2": "58",
        "Assignments": "58",
        "Attendance": "57",
        "Avg (X1)": "57.3",
        "Univ. (X2)": "57",
        "Total CO Attainment": "57.2"
    },
    {
        "Course Outcome": "Average:-",
        "Test 1": "59.25",
        "Test 2": "63",
        "Assignments": "59.25",
        "Attendance": "57",
        "Avg (X1)": "59.2",
        "Univ. (X2)": "57.7",
        "Total CO Attainment": "58.5"
    }
]

def load_data():
    """
    Load or create default data for 'lab_outcomes_attainment_25'.
    """
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    # If 'lab_outcomes_attainment_25' not in data, add the default structure
    if "lab_outcomes_attainment_25" not in data:
        data["lab_outcomes_attainment_25"] = DEFAULT_LAB_OUTCOMES_25

    return data

def save_data(data):
    """Write the data to course_data.json."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    st.set_page_config(page_title="Attainment of Lab Outcomes (CO) - Section 25", layout="wide")
    st.title("25. Attainment of Lab Outcomes through Internal Direct Method (Internal Assessment and University Assessment)")

    data = load_data()
    table_data = data["lab_outcomes_attainment_25"]

    st.write("Below is the table showing Direct Method % (Year: 2017-2018) for each Course Outcome, plus the average and total CO attainment.")

    # Editable table
    edited_data = st.data_editor(
        table_data,
        num_rows="dynamic",
        use_container_width=True,
        key="lab_outcomes_25_editor"
    )

    # Save button
    if st.button("Save Lab Outcomes Attainment"):
        data["lab_outcomes_attainment_25"] = edited_data
        save_data(data)
        st.success("Lab Outcomes Attainment data saved successfully!")

if __name__ == "__main__":
    main()
