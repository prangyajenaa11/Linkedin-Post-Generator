import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
from PIL import Image

# Set page configuration
st.set_page_config(page_title="LinkedIn Post Generator", page_icon="✍️", layout="wide")

# Load a banner image (optional, replace 'banner.jpg' with your image path)
# banner = Image.open("banner.jpg")
# st.image(banner, use_column_width=True)

# Sidebar customization
st.sidebar.title("Options")
st.sidebar.markdown("Customize your LinkedIn post settings below:")

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

# Initialize FewShotPosts
fs = FewShotPosts()
tags = fs.get_tags()

# Sidebar options
selected_tag = st.sidebar.selectbox("Select a Topic", options=tags)
selected_length = st.sidebar.selectbox("Select Length", options=length_options)
selected_language = st.sidebar.selectbox("Select Language", options=language_options)

# Main layout
st.title("LinkedIn Post Generator")
st.write("Generate engaging LinkedIn posts effortlessly with AI-powered suggestions!")

# Generate Button
if st.button("✨ Generate Post"):
    post = generate_post(selected_length, selected_language, selected_tag)
    
    # Display post in a styled container
    st.subheader("📝 Generated Post:")
    st.markdown(
        f"""
        <div style="background-color:#f4f4f4;padding:10px;border-radius:10px;margin-top:10px;">
            <p style="font-size:16px;">{post}</p>
        </div>
        """, unsafe_allow_html=True
    )

    # Provide copy button
    st.code(post, language='text')
    st.button("📋 Copy to Clipboard")

# Footer
st.markdown("---")
st.markdown("Made by Prangya")
