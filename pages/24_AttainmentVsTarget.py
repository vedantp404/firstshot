import streamlit as st
import json
import os

DATA_FILE = "course_data.json"

# Default data for Section 24
DEFAULT_ATTAINMENT_VS_TARGET = [
    {
        "CO Attainment Method": "University Examination",
        "Level 1": "45% student scoring more than 50% marks in the final examination",
        "Level 2": "55% student scoring more than 50% marks in the final examination",
        "Level 3": "65% student scoring more than 50% marks in the final examination"
    },
    {
        "CO Attainment Method": "Internal Assessment",
        "Level 1": "45% students score more than 60% in the internal assessment",
        "Level 2": "55% students score more than 60% in the internal assessment",
        "Level 3": "65% students score more than 60% in the internal assessment"
    },
    {
        "CO Attainment Method": "Course Exit Survey",
        "Level 1": "60% weightage average in course exit analysis",
        "Level 2": "70% weightage average in course exit analysis",
        "Level 3": "80% weightage average in course exit analysis"
    }
]

def load_data():
    """
    Load or create default data for 'attainment_vs_target'.
    """
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    # If 'attainment_vs_target' not in data, add default structure
    if "attainment_vs_target" not in data:
        data["attainment_vs_target"] = DEFAULT_ATTAINMENT_VS_TARGET

    return data

def save_data(data):
    """Write the data to course_data.json."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    st.set_page_config(page_title="Attainment level Vs Target", layout="wide")
    st.title("24. Attainment level Vs Target")

    data = load_data()
    table_data = data["attainment_vs_target"]

    st.write("Below is the table showing CO Attainment Method vs. Attainment Levels 1, 2, and 3.")

    # Editable table
    edited_data = st.data_editor(
        table_data,
        num_rows="dynamic",
        use_container_width=True,
        key="attainment_vs_target_editor"
    )

    # Save button
    if st.button("Save Attainment vs Target"):
        data["attainment_vs_target"] = edited_data
        save_data(data)
        st.success("Attainment vs Target data saved successfully!")

if __name__ == "__main__":
    main()
