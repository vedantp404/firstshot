import streamlit as st

# Configure the page
st.set_page_config(page_title="Welcome Dashboard", layout="wide")

# Optional custom CSS for table styling and centering
st.markdown("""
<style>
body {
    background-color: #ffffff;
    /* You can change background color if desired */
}
.table-class {
    border: 2px solid #000;
    border-collapse: collapse;
    margin: 20px auto; /* center the table horizontally */
    width: 600px;      /* adjust table width as needed */
}
.table-class th, .table-class td {
    border: 2px solid #000;
    padding: 8px;
    text-align: left;
    vertical-align: middle;
}
.centered-text {
    text-align: center;
    font-family: Arial, sans-serif;
}
h1, h2 {
    margin-bottom: 5px;
}
</style>
""", unsafe_allow_html=True)

# Left-aligned logo with width=200 (double the original 100)
st.image("bharatilogo.png", width=200)

# Main heading - replicate the look of your doc
st.markdown("<h1 class='centered-text'>BHARATI VIDYAPEETH COLLEGE OF ENGINEERING, NAVI MUMBAI</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='centered-text'>Department of Information Technology</h2>", unsafe_allow_html=True)

# Now replicate the table from your PDF
st.markdown("""
<table class="table-class">
  <tr>
    <th>ACADEMIC<br>YEAR</th>
    <td>2024-2025</td>
  </tr>
  <tr>
    <th>CLASS</th>
    <td>S.E.</td>
  </tr>
  <tr>
    <th>SEM</th>
    <td>IV</td>
  </tr>
  <tr>
    <th>NAME OF FACULTY</th>
    <td>Prof.S.S Kadam</td>
  </tr>
  <tr>
    <th>DESIGNATION</th>
    <td>Assistant Professor</td>
  </tr>
  <tr>
    <th>BRANCH</th>
    <td>Information Technology</td>
  </tr>
  <tr>
    <th>COURSE CODE</th>
    <td>ITC404</td>
  </tr>
  <tr>
    <th>NAME OF SUBJECT</th>
    <td>Computer Organization and Architecture</td>
  </tr>
</table>
""", unsafe_allow_html=True)

# Optional text below the table
st.write("""
This page replicates the official Course File cover with all essential details.
Use the sidebar to navigate to other sections and start editing or viewing content.
""")
