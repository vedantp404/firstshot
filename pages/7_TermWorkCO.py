import streamlit as st
import json
import os

DATA_FILE = "course_data.json"

# Default data for Section 7
DEFAULT_TERM_WORK_CO = [
    {
        "T/W Name": "Test 1",
        "Total Marks Assigned": "20",
        "Average Marks": "20",
        "C01": "√",
        "C02": "",
        "C03": "",
        "C04": ""
    },
    {
        "T/W Name": "Test 2",
        "Total Marks Assigned": "20",
        "Average Marks": "20",
        "C01": "",
        "C02": "√",
        "C03": "",
        "C04": ""
    },
    {
        "T/W Name": "University Examination",
        "Total Marks Assigned": "80",
        "Average Marks": "80",
        "C01": "",
        "C02": "",
        "C03": "√",
        "C04": ""
    }
]

def load_data():
    """
    Load or create default data for term_work_co.
    """
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    # If "term_work_co" not in data, add the default structure
    if "term_work_co" not in data:
        data["term_work_co"] = DEFAULT_TERM_WORK_CO

    return data

def save_data(data):
    """Write data to course_data.json."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    st.set_page_config(page_title="Term Work/Assessment Relate to CO", layout="wide")
    st.title("7. Term Work/Assessment Relate to Course Outcomes (CO)")

    data = load_data()
    term_work_table = data["term_work_co"]

    st.write("Below is the table showing T/W Name, marks, average, and mapping to C01–C04.")

    # Editable table using st.data_editor
    edited_term_work = st.data_editor(
        term_work_table,
        num_rows="dynamic",
        use_container_width=True,
        key="term_work_co_editor"
    )

    if st.button("Save Term Work CO"):
        data["term_work_co"] = edited_term_work
        save_data(data)
        st.success("Term Work/Assessment data saved successfully!")

if __name__ == "__main__":
    main()
