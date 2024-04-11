import streamlit as st
from PIL import Image
import cv2 
# Define the CSS style with a valid background image URL
st.title("It's Summer!")
img = Image.open("aiyla.jpeg")
st.image(img , width  = 400 , channels = "RGB" )

# Apply the CSS style to the Streamlit app


# Display a title on the Streamlit app


# Additional content can be added here...
