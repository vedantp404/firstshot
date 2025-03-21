import streamlit as st
import json
import os

DATA_FILE = 'course_data.json'

def load_data():
    """Load JSON or return default structure if file doesn't exist."""
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    # Default structure if file is missing or empty
    return {
        "course_structure": {
            "credit_assigned": [
                {
                    "Theory": "4",
                    "Practical": "-",
                    "Tutorial": "-",
                    "Total": "4",
                    "Total Scheme": "26"
                }
            ],
            "percentage_weightage1": [
                {
                    "Theory": "15.38",
                    "Practical": "-",
                    "Tutorial": "-",
                    "Total": "15.38",
                    "Total Scheme": "100"
                }
            ],
            "examination_scheme": [
                {
                    "Test1": "20",
                    "Test2": "20",
                    "Avg": "20",
                    "Theory": "80",
                    "Practical/Oral": "-",
                    "TW": "-",
                    "Total": "-",
                    "Total Scheme": "750"
                }
            ],
            "percentage_weightage2": [
                {
                    "Test1": "2.67",
                    "Test2": "2.67",
                    "Avg": "2.67",
                    "Theory": "10.67",
                    "Practical/Oral": "-",
                    "TW": "-",
                    "Total": "-",
                    "Total Scheme": "100"
                }
            ]
        }
    }

def save_data(data):
    """Write data to course_data.json."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    st.set_page_config(page_title="Course Structure", layout="wide")
    st.title("2. Course Structure Scheme")

    # Load existing data or default
    data = load_data()

    # Ensure "course_structure" key exists
    if "course_structure" not in data:
        data["course_structure"] = {}

    cs = data["course_structure"]

    # ---------------------------
    # 1) CREDIT ASSIGNED
    # ---------------------------
    st.subheader("Credit Assigned")
    # Retrieve the single-row list for credit_assigned (or create default if missing)
    credit_assigned = cs.get("credit_assigned", [
        {
            "Theory": "4",
            "Practical": "-",
            "Tutorial": "-",
            "Total": "4",
            "Total Scheme": "26"
        }
    ])

    edited_credit_assigned = st.data_editor(
        credit_assigned,
        num_rows="dynamic",  # user can add rows if desired
        use_container_width=True,
        key="credit_assigned_editor"
    )

    # ---------------------------
    # 2) PERCENTAGE OF WEIGHTAGE (1st)
    # ---------------------------
    st.subheader("Percentage of Weightage (1st)")
    weightage1 = cs.get("percentage_weightage1", [
        {
            "Theory": "15.38",
            "Practical": "-",
            "Tutorial": "-",
            "Total": "15.38",
            "Total Scheme": "100"
        }
    ])

    edited_weightage1 = st.data_editor(
        weightage1,
        num_rows="dynamic",
        use_container_width=True,
        key="weightage1_editor"
    )

    # ---------------------------
    # 3) EXAMINATION SCHEME
    # ---------------------------
    st.subheader("Examination Scheme")
    exam_scheme = cs.get("examination_scheme", [
        {
            "Test1": "20",
            "Test2": "20",
            "Avg": "20",
            "Theory": "80",
            "Practical/Oral": "-",
            "TW": "-",
            "Total": "-",
            "Total Scheme": "750"
        }
    ])

    edited_exam_scheme = st.data_editor(
        exam_scheme,
        num_rows="dynamic",
        use_container_width=True,
        key="exam_scheme_editor"
    )

    # ---------------------------
    # 4) PERCENTAGE OF WEIGHTAGE (2nd)
    # ---------------------------
    st.subheader("Percentage of Weightage (2nd)")
    weightage2 = cs.get("percentage_weightage2", [
        {
            "Test1": "2.67",
            "Test2": "2.67",
            "Avg": "2.67",
            "Theory": "10.67",
            "Practical/Oral": "-",
            "TW": "-",
            "Total": "-",
            "Total Scheme": "100"
        }
    ])

    edited_weightage2 = st.data_editor(
        weightage2,
        num_rows="dynamic",
        use_container_width=True,
        key="weightage2_editor"
    )

    # ---------------------------
    # SAVE BUTTON
    # ---------------------------
    if st.button("Save Course Structure"):
        # Each editor returns a list of dicts; we assume one row each
        data["course_structure"] = {
            "credit_assigned": edited_credit_assigned,
            "percentage_weightage1": edited_weightage1,
            "examination_scheme": edited_exam_scheme,
            "percentage_weightage2": edited_weightage2
        }

        save_data(data)
        st.success("Course Structure saved successfully!")

if __name__ == "__main__":
    main()
