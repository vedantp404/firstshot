import streamlit as st
import json
import os

DATA_FILE = "course_data.json"

# Default data
DEFAULT_MODES_LIST = [
    {"ID": "i",   "Mode": "Class Room Teaching"},
    {"ID": "ii",  "Mode": "Tutorial"},
    {"ID": "iii", "Mode": "Remedial Coaching"},
    {"ID": "iv",  "Mode": "Lab Experiment"},
    {"ID": "v",   "Mode": "Self-Learning Online Resources"},
    {"ID": "vi",  "Mode": "Slides"},
    {"ID": "vii", "Mode": "Simulations/Demonstrations"},
    {"ID": "viii","Mode": "Expert Lecture/video lecture"},
    {"ID": "ix",  "Mode": "Industry Visit"},
    {"ID": "x",   "Mode": "Group Discussion"},
    {"ID": "xi",  "Mode": "Seminar"},
    {"ID": "xii", "Mode": "Case Study/Mini Project"}
]

DEFAULT_CO_MAPPING = [
    {
        "Sr. No": "1",
        "Lab Outcome": "ITC404.1",
        "i": "X", "ii": "", "iii": "", "iv": "X", "v": "X", "vi": "",
        "vii": "", "viii": "X", "ix": "", "x": "", "xi": "", "xii": ""
    },
    {
        "Sr. No": "2",
        "Lab Outcome": "ITC404.2",
        "i": "", "ii": "X", "iii": "", "iv": "", "v": "", "vi": "X",
        "vii": "", "viii": "", "ix": "", "x": "", "xi": "", "xii": ""
    },
    {
        "Sr. No": "3",
        "Lab Outcome": "ITC404.3",
        "i": "", "ii": "", "iii": "X", "iv": "", "v": "", "vi": "",
        "vii": "X", "viii": "", "ix": "", "x": "", "xi": "", "xii": ""
    },
    {
        "Sr. No": "4",
        "Lab Outcome": "ITC404.4",
        "i": "", "ii": "", "iii": "", "iv": "", "v": "", "vi": "",
        "vii": "", "viii": "", "ix": "X", "x": "", "xi": "", "xii": "X"
    }
]

def load_data():
    """
    Load from JSON or create 'modes_content_delivery' if missing.
    """
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    if "modes_content_delivery" not in data:
        data["modes_content_delivery"] = {
            "modes_list": DEFAULT_MODES_LIST,
            "co_mapping": DEFAULT_CO_MAPPING
        }
    else:
        # Ensure sub-keys exist if missing
        if "modes_list" not in data["modes_content_delivery"]:
            data["modes_content_delivery"]["modes_list"] = DEFAULT_MODES_LIST
        if "co_mapping" not in data["modes_content_delivery"]:
            data["modes_content_delivery"]["co_mapping"] = DEFAULT_CO_MAPPING

    return data

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    st.set_page_config(page_title="Modes of Content Delivery", layout="wide")
    st.title("8. Modes of Content Delivery")

    data = load_data()
    mcd = data["modes_content_delivery"]

    # 1) Table for i, ii, iii, etc.
    st.subheader("List of Modes")
    modes_list = mcd["modes_list"]
    edited_modes_list = st.data_editor(
        modes_list,
        num_rows="dynamic",
        use_container_width=True,
        key="modes_list_editor"
    )

    # 2) Table for CO Mapping with i, ii, ...
    st.subheader("COs Mapping with Content Delivery")
    co_mapping = mcd["co_mapping"]
    edited_co_mapping = st.data_editor(
        co_mapping,
        num_rows="dynamic",
        use_container_width=True,
        key="co_mapping_editor"
    )

    if st.button("Save Modes & CO Mapping"):
        data["modes_content_delivery"]["modes_list"] = edited_modes_list
        data["modes_content_delivery"]["co_mapping"] = edited_co_mapping
        save_data(data)
        st.success("Modes and CO mapping saved successfully!")

if __name__ == "__main__":
    main()
