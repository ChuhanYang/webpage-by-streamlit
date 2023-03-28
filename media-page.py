# Data and Media Elements
import streamlit as st
import base64
from PIL import Image
import time

st.write("Seven and July")

st.image("img/cat-fight.jpg","Cat Fight")

# Add background

# Function to set Image as Background
def add_local_backgound_image_(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())
    st.write("Location: Mina port")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded_string.decode()});
            background-size: 100% 100%;
            background-repeat: no-repeat;
            background-position: center center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.write("Background Image")
# Calling Image in function
add_local_backgound_image_('img/moon-light.jpg')

# Resize the image
original_image = Image.open("img/cat-fight.jpg")
# Resizing Image to 600*400
resized_image = original_image.resize((200, 300))
#Displaying Resized Image
st.title("Resized Image")
st.image(resized_image)



# Audio
# Open Audio using filepath with filename
st.title("Song playing: Smoke by SoulProdMusic")
sample_audio = open("misc/smoke-143172.mp3", "rb")
#Reading Audio File
audio_bytes = sample_audio.read()
# Display Audio using st.audio() function with start time set to 0
st.audio(sample_audio, start_time = 0)
# Printing Audio Courtesy
st.write("Audio Courtesy: https://https://pixabay.com/music/beats-smoke-143172/")


# Open Audio using filepath with filename and read theaudio file
sample_url = st.audio("https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3")
st.write("Audio Courtesy: https://www.learningcontainer.com/sample-audio-file/")


# Video
# Displaying Video using youtube URL
st.video("https://www.youtube.com/watch?v=OMkEVX23BdM")
# Courtesy by youtube channel
st.write("Video Courtesy: National Geographic Channel")



# Animation
# Animated Snowflakes
st.balloons()

time.sleep(10) 

st.snow()


# Emojis with/without shortcodes
emojis = """:rain_cloud: :coffee: :love_hotel: :couple_with_heart: """
# Displaying Shortcodes
st.title(emojis)
