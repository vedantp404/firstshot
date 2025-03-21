import streamlit as st
import json
import os

DATA_FILE = "course_data.json"

# Default data for Section 27
DEFAULT_SECTION_A = [
    {
        "Description": "Target level",
        "PO1": "2.6",
        "PO2": "3",
        "PO3": "3",
        "PO4": "2",
        "PSO1": "2",
        "PSO2": ""
    },
    {
        "Description": "Direct Method Level",
        "PO1": "1.8",
        "PO2": "2.1",
        "PO3": "2.1",
        "PO4": "1.4",
        "PSO1": "1.41",
        "PSO2": ""
    },
    {
        "Description": "Correlation Levels",
        "PO1": "1: Slightly",
        "PO2": "2: Moderately",
        "PO3": "3: Substantially",
        "PO4": "",
        "PSO1": "",
        "PSO2": ""
    }
]

DEFAULT_SECTION_B = [
    { "CO No.": "ITC404.1", "Attainment Level": "3" },
    { "CO No.": "ITC404.2", "Attainment Level": "3" },
    { "CO No.": "ITC404.3", "Attainment Level": "3" },
    { "CO No.": "ITC404.4", "Attainment Level": "3" }
]

def load_data():
    """
    Load or create default data for 'direct_indirect_assessment_27'.
    """
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    # If 'direct_indirect_assessment_27' not in data, create sub-keys
    if "direct_indirect_assessment_27" not in data:
        data["direct_indirect_assessment_27"] = {
            "sectionA": DEFAULT_SECTION_A,
            "sectionB": DEFAULT_SECTION_B
        }
    else:
        # If sectionA or sectionB is missing, add defaults
        if "sectionA" not in data["direct_indirect_assessment_27"]:
            data["direct_indirect_assessment_27"]["sectionA"] = DEFAULT_SECTION_A
        if "sectionB" not in data["direct_indirect_assessment_27"]:
            data["direct_indirect_assessment_27"]["sectionB"] = DEFAULT_SECTION_B

    return data

def save_data(data):
    """Write data to course_data.json."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    st.set_page_config(page_title="Direct & Indirect Assessment to PO/PSO (Sec 27)", layout="wide")
    st.title("27. Contribution through Direct and Indirect assessment to PO and PSO Attainment Level")

    data = load_data()
    di_assess = data["direct_indirect_assessment_27"]

    # Section A
    st.subheader("A. Contribution through Direct and Indirect assessment to PO and PSO Attainment Level")
    sectionA_table = di_assess["sectionA"]
    edited_sectionA = st.data_editor(
        sectionA_table,
        num_rows="dynamic",
        use_container_width=True,
        key="sectionA_editor"
    )

    # Section B
    st.subheader("B. Course Exit survey (Indirect assessment): (Year: 2017-2018)")
    sectionB_table = di_assess["sectionB"]
    edited_sectionB = st.data_editor(
        sectionB_table,
        num_rows="dynamic",
        use_container_width=True,
        key="sectionB_editor"
    )

    if st.button("Save Direct & Indirect Assessment"):
        di_assess["sectionA"] = edited_sectionA
        di_assess["sectionB"] = edited_sectionB
        save_data(data)
        st.success("Direct & Indirect assessment data saved successfully!")

if __name__ == "__main__":
    main()
