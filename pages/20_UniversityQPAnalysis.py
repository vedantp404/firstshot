import streamlit as st
import json
import os

DATA_FILE = "course_data.json"

# Default data for Section 20
DEFAULT_UNIV_QP_ANALYSIS = [
    {
        "Module": "1",
        "No. of Hours": "7",
        "Total Credit Assigned": "0.5",
        "Total Marks Assigned": "18.27",
        "% of Weightage": "15.22",
        "Uni QP Actually Mark Allotted": "10",
        "Uni QP 2017-18 EVEN SEM": "35",
        "Uni QP % of Weightage": "8.33"
    },
    {
        "Module": "2",
        "No. of Hours": "10",
        "Total Credit Assigned": "0.72",
        "Total Marks Assigned": "26.08",
        "% of Weightage": "21.74",
        "Uni QP Actually Mark Allotted": "25",
        "Uni QP 2017-18 EVEN SEM": "40",
        "Uni QP % of Weightage": "20.83"
    },
    {
        "Module": "3",
        "No. of Hours": "11",
        "Total Credit Assigned": "0.79",
        "Total Marks Assigned": "28.70",
        "% of Weightage": "23.91",
        "Uni QP Actually Mark Allotted": "35",
        "Uni QP 2017-18 EVEN SEM": "50",
        "Uni QP % of Weightage": "29.17"
    },
    {
        "Module": "4",
        "No. of Hours": "10",
        "Total Credit Assigned": "0.71",
        "Total Marks Assigned": "26.08",
        "% of Weightage": "21.74",
        "Uni QP Actually Mark Allotted": "20",
        "Uni QP 2017-18 EVEN SEM": "30",
        "Uni QP % of Weightage": "16.67"
    },
    {
        "Module": "5",
        "No. of Hours": "7",
        "Total Credit Assigned": "0.5",
        "Total Marks Assigned": "18.27",
        "% of Weightage": "15.22",
        "Uni QP Actually Mark Allotted": "15",
        "Uni QP 2017-18 EVEN SEM": "20",
        "Uni QP % of Weightage": "12.50"
    },
    {
        "Module": "6",
        "No. of Hours": "5",
        "Total Credit Assigned": "0.36",
        "Total Marks Assigned": "13.04",
        "% of Weightage": "10.87",
        "Uni QP Actually Mark Allotted": "15",
        "Uni QP 2017-18 EVEN SEM": "25",
        "Uni QP % of Weightage": "12.50"
    },
    {
        "Module": "Total",
        "No. of Hours": "46",
        "Total Credit Assigned": "4",
        "Total Marks Assigned": "120",
        "% of Weightage": "100",
        "Uni QP Actually Mark Allotted": "120",
        "Uni QP 2017-18 EVEN SEM": "200",
        "Uni QP % of Weightage": "100"
    }
]

def load_data():
    """
    Load or create default data for 'university_qp_analysis'.
    """
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    # If 'university_qp_analysis' not in data, add default structure
    if "university_qp_analysis" not in data:
        data["university_qp_analysis"] = DEFAULT_UNIV_QP_ANALYSIS

    return data

def save_data(data):
    """Write data to course_data.json."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    st.set_page_config(page_title="University Q. Paper Analysis", layout="wide")
    st.title("20. A. University Q. Paper Analysis")

    data = load_data()
    univ_qp_data = data["university_qp_analysis"]

    st.write("Below is the table showing module, hours, total credits, marks assigned, weightage, and university QP mapping details.")

    # Editable table
    edited_data = st.data_editor(
        univ_qp_data,
        num_rows="dynamic",
        use_container_width=True,
        key="univ_qp_analysis_editor"
    )

    # Save button
    if st.button("Save University QP Analysis"):
        data["university_qp_analysis"] = edited_data
        save_data(data)
        st.success("University QP Analysis saved successfully!")

if __name__ == "__main__":
    main()
