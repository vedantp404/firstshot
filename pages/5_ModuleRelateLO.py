import streamlit as st
import json
import os

DATA_FILE = "course_data.json"

# Default data for Section 5
DEFAULT_MODULE_RELATE_LO = [
    {
        "Module": "1",
        "No. of Hours (theory)": "7",
        "Total Credit Assigned (theory)": "(07/50)*4=0.56",
        "Total Marks Assigned": "(07*120)/50=16.8",
        "Weightage (%)": "(07*100)/50=14",
        "PO No.": "PO1, PO2, PO3, PO4, PSO1",
        "C01": "√",
        "C02": "",
        "C03": "",
        "C04": ""
    },
    {
        "Module": "2",
        "No. of Hours (theory)": "10",
        "Total Credit Assigned (theory)": "0.8",
        "Total Marks Assigned": "24",
        "Weightage (%)": "20",
        "PO No.": "",
        "C01": "",
        "C02": "",
        "C03": "",
        "C04": ""
    },
    {
        "Module": "3",
        "No. of Hours (theory)": "11",
        "Total Credit Assigned (theory)": "0.88",
        "Total Marks Assigned": "26.4",
        "Weightage (%)": "22",
        "PO No.": "",
        "C01": "",
        "C02": "",
        "C03": "",
        "C04": ""
    },
    {
        "Module": "4",
        "No. of Hours (theory)": "10",
        "Total Credit Assigned (theory)": "0.8",
        "Total Marks Assigned": "24",
        "Weightage (%)": "20",
        "PO No.": "",
        "C01": "",
        "C02": "",
        "C03": "",
        "C04": ""
    },
    {
        "Module": "5",
        "No. of Hours (theory)": "7",
        "Total Credit Assigned (theory)": "0.56",
        "Total Marks Assigned": "16.8",
        "Weightage (%)": "14",
        "PO No.": "",
        "C01": "",
        "C02": "",
        "C03": "",
        "C04": ""
    },
    {
        "Module": "6",
        "No. of Hours (theory)": "5",
        "Total Credit Assigned (theory)": "0.4",
        "Total Marks Assigned": "12",
        "Weightage (%)": "10",
        "PO No.": "",
        "C01": "",
        "C02": "",
        "C03": "",
        "C04": ""
    },
    {
        "Module": "Total",
        "No. of Hours (theory)": "50",
        "Total Credit Assigned (theory)": "4",
        "Total Marks Assigned": "120",
        "Weightage (%)": "100",
        "PO No.": "",
        "C01": "",
        "C02": "",
        "C03": "",
        "C04": ""
    }
]

def load_data():
    """Load or create default data for module_relate_lo."""
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    # If "module_relate_lo" not in data, add the default
    if "module_relate_lo" not in data:
        data["module_relate_lo"] = DEFAULT_MODULE_RELATE_LO

    return data

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    st.set_page_config(page_title="Module Relate to Course Outcomes (LO)", layout="wide")
    st.title("5. Module Relate to Course Outcomes (LO)")

    data = load_data()
    module_table = data["module_relate_lo"]

    st.write("Below is the table showing module, hours, credit assigned, marks, weightage, PO No., and LO checks (C01–C04).")

    # Let user edit the table
    edited_table = st.data_editor(
        module_table,
        num_rows="dynamic",
        use_container_width=True,
        key="module_relate_lo_editor"
    )

    if st.button("Save Module-LO Data"):
        data["module_relate_lo"] = edited_table
        save_data(data)
        st.success("Module Relate to LO data saved successfully!")

if __name__ == "__main__":
    main()
