import streamlit as st

# Set page title and configure layout
st.set_page_config(page_title="Trimester Box Grid", layout="wide")

# Add page title with custom styling
st.markdown("<h1 style='color: #5D9E7F;'>Trimester Selection</h1>", unsafe_allow_html=True)

# Define pastel green colors
primary_green = "#8FBC8F"  # Dark Sea Green (pastel)
secondary_green = "#C1E1C1"  # Light pastel green
hover_green = "#A9D0A9"  # Medium pastel green
bg_color = "#F0FFF0"  # Honeydew (very light pastel green)

# Custom button styling with pastel green theme
button_style = f"""
<style>
    div.stButton > button {{
        background-color: {primary_green};
        color: white;
        border: none;
        padding: 10px 24px;
        border-radius: 4px;
        transition: background-color 0.3s;
    }}
    div.stButton > button:hover {{
        background-color: {hover_green};
    }}
    div.stButton > button:active {{
        background-color: {hover_green};
    }}
</style>
"""
st.markdown(button_style, unsafe_allow_html=True)

# Create three buttons in a horizontal layout
col1, col2, col3 = st.columns(3)

with col1:
    trimester1_button = st.button("Trimester 1", use_container_width=True)

with col2:
    trimester2_button = st.button("Trimester 2", use_container_width=True)

with col3:
    trimester3_button = st.button("Trimester 3", use_container_width=True)

# Custom CSS for styling the larger pastel green boxes
st.markdown(f"""
<style>
    body {{
        background-color: {bg_color};
    }}
    .box-container {{
        display: flex;
        flex-wrap: wrap;
        gap: 30px;
        margin-top: 30px;
    }}
    .box {{
        width: 350px;
        height: 400px;
        background-color: {secondary_green};
        border: 1px solid {primary_green};
        border-radius: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 24px;
        font-weight: bold;
        color: #4C7C4C;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: transform 0.2s, box-shadow 0.2s;
    }}
    .box:hover {{
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        background-color: {hover_green};
    }}
</style>
""", unsafe_allow_html=True)

# Function to create a row of 3 boxes
def create_box_row(start_num):
    # For large boxes, we'll create just one row with 3 boxes
    row_html = '<div style="display: flex; flex-wrap: wrap; justify-content: space-between; gap: 30px; margin-bottom: 30px;">'
    for i in range(3):
        box_num = start_num + i
        row_html += f'<div class="box">Box {box_num}</div>'
    row_html += '</div>'
    return row_html

# Function to display 12 boxes in a grid (4 rows of 3 boxes)
def display_boxes():
    # Create 4 rows with 3 boxes each
    for row in range(4):
        start_num = row * 3 + 1
        st.markdown(create_box_row(start_num), unsafe_allow_html=True)

# Create a container for the boxes
box_container = st.container()

# Store which trimester is active in session state
if 'active_trimester' not in st.session_state:
    st.session_state.active_trimester = None

# Handle button clicks
if trimester1_button:
    st.session_state.active_trimester = 1
elif trimester2_button:
    st.session_state.active_trimester = 2
elif trimester3_button:
    st.session_state.active_trimester = 3

# Display the appropriate set of boxes based on which trimester is active
with box_container:
    if st.session_state.active_trimester:
        st.markdown(f"<h2 style='color: #5D9E7F; margin-top: 20px;'>Trimester {st.session_state.active_trimester} Boxes</h2>", unsafe_allow_html=True)
        display_boxes()