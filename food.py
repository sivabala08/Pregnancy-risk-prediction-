import streamlit as st

# Add page title with custom styling
st.markdown("<h1 style='color: #5D9E7F;'>Healthy Food During Pregnancy</h1>", unsafe_allow_html=True)

# Define pastel green colors
primary_green = "#8FBC8F"  # Dark Sea Green (pastel)
secondary_green = "#C1E1C1"  # Light pastel green
hover_green = "#A9D0A9"  # Medium pastel green
bg_color = "#F0FFF0"  # Honeydew (very light pastel green)

# Custom CSS for styling
st.markdown(f"""
<style>
    .main .block-container {{
        padding-top: 2rem;
        padding-bottom: 2rem;
        background-color: {bg_color};
    }}
    
   
    
    /* Additional element styling */
    h1, h2, h3, h4 {{
        color: #3A5F3A;
    }}
    
    img {{
        border-radius: 6px;
    }}
</style>
""", unsafe_allow_html=True)

# Define healthy food recommendations
healthy_foods = [
    {
        "topic": "Leafy Greens",
        "content": "Leafy greens like spinach, kale, and broccoli are rich in folate, iron, and calcium. Folate is essential for preventing neural tube defects in the baby.",
        "image": "https://via.placeholder.com/200x150?text=Leafy+Greens"
    },
    {
        "topic": "Whole Grains",
        "content": "Whole grains like oats, quinoa, and brown rice provide fiber, B vitamins, and energy. They help maintain stable blood sugar levels and prevent constipation.",
        "image": "https://via.placeholder.com/200x150?text=Whole+Grains"
    },
    {
        "topic": "Lean Proteins",
        "content": "Lean proteins like chicken, fish, eggs, and legumes are crucial for the baby's growth and development. Fish like salmon also provide omega-3 fatty acids.",
        "image": "https://via.placeholder.com/200x150?text=Lean+Proteins"
    },
    {
        "topic": "Dairy Products",
        "content": "Dairy products like milk, yogurt, and cheese are excellent sources of calcium and protein, which are vital for the baby's bone development.",
        "image": "https://via.placeholder.com/200x150?text=Dairy+Products"
    },
    {
        "topic": "Fruits",
        "content": "Fruits like oranges, bananas, and berries are packed with vitamins, minerals, and fiber. They help boost immunity and provide natural energy.",
        "image": "https://via.placeholder.com/200x150?text=Fruits"
    },
    {
        "topic": "Nuts and Seeds",
        "content": "Nuts and seeds like almonds, walnuts, and chia seeds are rich in healthy fats, protein, and fiber. They support the baby's brain development.",
        "image": "https://via.placeholder.com/200x150?text=Nuts+and+Seeds"
    }
]

# Display healthy food cards
st.markdown("<h2 style='color: #5D9E7F; margin-top: 20px;'>Top Healthy Foods for Pregnancy</h2>", unsafe_allow_html=True)

# Create a container for the food cards
food_container = st.container()

with food_container:
    for food in healthy_foods:
        with st.container():
            st.markdown(f"<div class='stContainer'>", unsafe_allow_html=True)
            
            # Display the image
            st.image(food["image"], use_container_width=True)
            
            # Display the topic and content
            st.markdown(f"#### {food['topic']}")
            st.markdown(food["content"])
            
            # Add a "Read More" button (placeholder link)
            #st.markdown(f'<a href="#" class="read-more-btn">Read More</a>', unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)