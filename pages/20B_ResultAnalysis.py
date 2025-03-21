import streamlit as st
import json
import os

DATA_FILE = "course_data.json"

# Default data for Section 20 (B)
DEFAULT_RESULT_ANALYSIS = [
    {
        "Category": "No. of students",
        "No. of students appeared": "66",
        "Fail": "10",
        "Pass class": "24",
        "Second Class": "17",
        "First Class": "12",
        "First Class with Distinction": "02"
    },
    {
        "Category": "% of students",
        "No. of students appeared": "100",
        "Fail": "15.15",
        "Pass class": "36.36",
        "Second Class": "25.76",
        "First Class": "18.18",
        "First Class with Distinction": "0.03"
    },
    {
        "Category": "Result in %",
        "No. of students appeared": "84.84%",
        "Fail": "",
        "Pass class": "",
        "Second Class": "",
        "First Class": "",
        "First Class with Distinction": ""
    }
]

def load_data():
    """
    Load or create default data for 'result_analysis_2017_18'.
    """
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    # If 'result_analysis_2017_18' not in data, add default structure
    if "result_analysis_2017_18" not in data:
        data["result_analysis_2017_18"] = DEFAULT_RESULT_ANALYSIS

    return data

def save_data(data):
    """Write data to course_data.json."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    st.set_page_config(page_title="Result Analysis 2017-2018", layout="wide")
    st.title("20. B. Result Analysis Year: 2017-2018")

    data = load_data()
    result_table = data["result_analysis_2017_18"]

    st.write("Below is the table showing the result analysis for the year 2017-2018.")

    # Editable table
    edited_result = st.data_editor(
        result_table,
        num_rows="dynamic",
        use_container_width=True,
        key="result_analysis_2017_18_editor"
    )

    # Save button
    if st.button("Save Result Analysis"):
        data["result_analysis_2017_18"] = edited_result
        save_data(data)
        st.success("Result Analysis data saved successfully!")

if __name__ == "__main__":
    main()
