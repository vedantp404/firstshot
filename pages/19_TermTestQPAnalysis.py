import streamlit as st
import json
import os

DATA_FILE = "course_data.json"

# Default data for Section 19
DEFAULT_TERM_TEST_QP = [
    {
        "Module": "1",
        "No. of Hours": "7",
        "Total Credit Assigned": "(07/25)*2=0.56",
        "Total Marks Assigned": "(07*32)/25=8.96",
        "% of Weightage": "(07*100)/25=28",
        "TT Actually Mark Allotted": "8",
        "TT 2017-18 EVEN SEM": "25",
        "TT % of Weightage": "25"
    },
    {
        "Module": "2",
        "No. of Hours": "10",
        "Total Credit Assigned": "0.8",
        "Total Marks Assigned": "12.8",
        "% of Weightage": "12",
        "TT Actually Mark Allotted": "12",
        "TT 2017-18 EVEN SEM": "32",
        "TT % of Weightage": "37.5"
    },
    {
        "Module": "3",
        "No. of Hours": "11",
        "Total Credit Assigned": "0.88",
        "Total Marks Assigned": "14.08",
        "% of Weightage": "8.8",
        "TT Actually Mark Allotted": "12",
        "TT 2017-18 EVEN SEM": "32",
        "TT % of Weightage": "37.5"
    },
    {
        "Module": "Total",
        "No. of Hours": "28",
        "Total Credit Assigned": "2.24",
        "Total Marks Assigned": "34.84",
        "% of Weightage": "48",
        "TT Actually Mark Allotted": "32",
        "TT 2017-18 EVEN SEM": "89",
        "TT % of Weightage": "100"
    }
]

def load_data():
    """
    Load or create default data for 'term_test_qp_analysis'.
    """
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    # If 'term_test_qp_analysis' not in data, add default structure
    if "term_test_qp_analysis" not in data:
        data["term_test_qp_analysis"] = DEFAULT_TERM_TEST_QP

    return data

def save_data(data):
    """Write the data to course_data.json."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    st.set_page_config(page_title="Term Test Q. Paper Analysis", layout="wide")
    st.title("19. Term Test Question Paper Analysis")

    data = load_data()
    table_data = data["term_test_qp_analysis"]

    st.write("Below is the table showing module, hours, total credits, marks assigned, weightage, and term test QP analysis details.")

    # Editable table
    edited_data = st.data_editor(
        table_data,
        num_rows="dynamic",
        use_container_width=True,
        key="term_test_qp_editor"
    )

    # Save button
    if st.button("Save Term Test QP Analysis"):
        data["term_test_qp_analysis"] = edited_data
        save_data(data)
        st.success("Term Test Question Paper Analysis saved successfully!")

if __name__ == "__main__":
    main()
