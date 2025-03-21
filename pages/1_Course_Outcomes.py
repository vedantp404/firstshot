import streamlit as st
import json
import os

DATA_FILE = 'course_data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    # Default structure if the file doesn't exist
    return {
        "course_outcomes": [
            {
                "co_code": "ITC404.1",
                "description": "Describe basic organization of computer and the architecture of 8086 microprocessor",
                "po_pso": "PO1",
                "bloom_level": "L1-Remembering, L2-Understanding"
            },
            {
                "co_code": "ITC404.2",
                "description": "Implement assembly language program for given task and perform computer arithmetic operations on integer and real numbers",
                "po_pso": "PO2, PO4",
                "bloom_level": "L1-Remembering, L2-Understanding, L4-Analyzing, L6-Creating"
            },
            {
                "co_code": "ITC404.3",
                "description": "Categorize memory organization and explain the function of each element of a memory hierarchy",
                "po_pso": "PO1, PO2",
                "bloom_level": "L2-Understanding, L3-Applying, L4-Analyzing"
            },
            {
                "co_code": "ITC404.4",
                "description": "Identify and compare different methods for computer I/O mechanisms",
                "po_pso": "PO3, PO4",
                "bloom_level": "L2-Understanding, L4-Analyzing"
            }
        ]
    }

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    st.set_page_config(page_title="Course Outcomes", layout="wide")
    st.title("1. Course Outcomes (CO)")
    st.write("At the end of the course, students will be able to:")

    # Load data and ensure the key exists
    data = load_data()
    if "course_outcomes" not in data:
        data["course_outcomes"] = []

    # Use st.data_editor to allow editing of the table data
    edited_co = st.data_editor(data["course_outcomes"], key="co_editor", num_rows="dynamic", use_container_width=True)

    if st.button("Save Course Outcomes"):
        data["course_outcomes"] = edited_co
        save_data(data)
        st.success("Course Outcomes saved successfully!")

if __name__ == "__main__":
    main()
