import streamlit as st
import json
import os

DATA_FILE = "course_data.json"

# Default data for Section 6
DEFAULT_ASSESSMENT_INSTRUMENTS = [
    {
        "Course Outcome": "ITC404.1 Describe basic organization of computer and the architecture of 8086 microprocessor",
        "Assessment Tool Direct": "Test 1",
        "Maximum Marks": "10",
        "Assessment Tool Indirect": "Course Exit Survey"
    },
    {
        "Course Outcome": "ITC404.2 Implement assembly language program for given task and perform computer arithmetic operations on integer and real numbers",
        "Assessment Tool Direct": "Test 1",
        "Maximum Marks": "10",
        "Assessment Tool Indirect": "Course Exit Survey"
    },
    {
        "Course Outcome": "ITC404.3 Categorize memory organization and explain the function of each element of a memory hierarchy",
        "Assessment Tool Direct": "Test 2",
        "Maximum Marks": "10",
        "Assessment Tool Indirect": "Course Exit Survey"
    },
    {
        "Course Outcome": "ITC404.4 Identify and compare different methods for computer I/O mechanisms",
        "Assessment Tool Direct": "Test 2",
        "Maximum Marks": "10",
        "Assessment Tool Indirect": "Course Exit Survey"
    },
    {
        "Course Outcome": "All Course Outcomes",
        "Assessment Tool Direct": "Internal Assessment",
        "Maximum Marks": "20",
        "Assessment Tool Indirect": ""
    },
    {
        "Course Outcome": "University Examination",
        "Assessment Tool Direct": "",
        "Maximum Marks": "80",
        "Assessment Tool Indirect": ""
    }
]

def load_data():
    """
    Load or create default data for assessment_instruments.
    """
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    # If "assessment_instruments" not in data, add the default structure
    if "assessment_instruments" not in data:
        data["assessment_instruments"] = DEFAULT_ASSESSMENT_INSTRUMENTS

    return data

def save_data(data):
    """Write data to course_data.json."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    st.set_page_config(page_title="Assessment Instruments", layout="wide")
    st.title("6. Assessment Instruments used for attainment of COs")

    data = load_data()
    instruments_table = data["assessment_instruments"]

    st.write("Below is the table for each Course Outcome, the direct and indirect assessment tools, and their marks.")

    # Display the table as an editable data editor
    edited_instruments = st.data_editor(
        instruments_table,
        num_rows="dynamic",
        use_container_width=True,
        key="assessment_instruments_editor"
    )

    # Save button
    if st.button("Save Assessment Instruments"):
        data["assessment_instruments"] = edited_instruments
        save_data(data)
        st.success("Assessment Instruments saved successfully!")

if __name__ == "__main__":
    main()
