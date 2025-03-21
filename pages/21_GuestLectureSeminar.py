import streamlit as st
import json
import os

DATA_FILE = "course_data.json"

# Default data for Section 21
DEFAULT_GUEST_LECTURE = [
    {
        "Date": "01/01/2018",
        "Brief Description Of Lecture": "Introduction to AI",
        "Resource Person Details": "Dr. X (ABC University)",
        "No. Of Participants": "50",
        "Organized by": "IT Department",
        "Sponsors": "XYZ"
    }
]

DEFAULT_SEMINAR_DETAILS = [
    {
        "Roll No": "101",
        "Name": "Student A",
        "Topics": "Machine Learning Basics",
        "Dates": "02/02/2018"
    }
]

def load_data():
    """
    Load or create default data for 'guest_lecture_seminar'.
    """
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    # If 'guest_lecture_seminar' not in data, create it
    if "guest_lecture_seminar" not in data:
        data["guest_lecture_seminar"] = {
            "guest_lecture_details": DEFAULT_GUEST_LECTURE,
            "seminar_details": DEFAULT_SEMINAR_DETAILS
        }
    else:
        # If sub-keys are missing, add them
        if "guest_lecture_details" not in data["guest_lecture_seminar"]:
            data["guest_lecture_seminar"]["guest_lecture_details"] = DEFAULT_GUEST_LECTURE
        if "seminar_details" not in data["guest_lecture_seminar"]:
            data["guest_lecture_seminar"]["seminar_details"] = DEFAULT_SEMINAR_DETAILS

    return data

def save_data(data):
    """Write data to course_data.json."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    st.set_page_config(page_title="Guest Lecture & Seminar Details", layout="wide")
    st.title("21. A. Guest Lecture Details | B. Seminar Details")

    data = load_data()
    gls = data["guest_lecture_seminar"]

    # 1) Guest Lecture Details
    st.subheader("A. Guest Lecture Details")
    guest_lectures = gls["guest_lecture_details"]
    edited_guest_lectures = st.data_editor(
        guest_lectures,
        num_rows="dynamic",
        use_container_width=True,
        key="guest_lecture_editor"
    )

    # 2) Seminar Details
    st.subheader("B. Seminar Details (Year 2017-2018)")
    seminar_details = gls["seminar_details"]
    edited_seminar_details = st.data_editor(
        seminar_details,
        num_rows="dynamic",
        use_container_width=True,
        key="seminar_details_editor"
    )

    if st.button("Save Guest Lecture & Seminar"):
        data["guest_lecture_seminar"]["guest_lecture_details"] = edited_guest_lectures
        data["guest_lecture_seminar"]["seminar_details"] = edited_seminar_details
        save_data(data)
        st.success("Guest Lecture & Seminar details saved successfully!")

if __name__ == "__main__":
    main()
