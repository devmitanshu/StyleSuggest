import streamlit as st
import json
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(
    page_title="Style-Suggest",
    page_icon="fa-digital-ocean"
)

st.title("Style-Suggest")
st.header('A Clothing Recommendation System')
st.sidebar.success("Select a page")


def load_lottiefile(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)


lottie_team = load_lottiefile("lottiefiles/Hello.json")
st_lottie(
    lottie_team,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",  # medium ; high
    # renderer="svg", # canvas
    height=300,
    width=None,
    key=None,
)


html_temp = """
    <div style="padding:10px">
    <h3 style="color:white;text-align:center;">This is a Cloth Recommendation App. Please go to the main Page to select any attire and get recommendations for the similar products</h3>
    </div>
    <div>
    <p>This application is used to detect the kind of garment,such as ladies tops, etc., and make correct suggestions for related items. We have used open-source computer vision libraries, such as TensorFlow and OpenCV, to make development and integration with the dataset given to us.</p>
    <p>The image dataset given to us consist of ladies clothing. Therefore uploading ladies garments will work for this model. The same model can be used for a huge dataset of garments for any gender.</p>

    </div>
    """
st.markdown(html_temp,  unsafe_allow_html=True)

image = Image.open('Screenshots/about.png')
st.image(image, caption='Tensorflow Resnet50 Model')


def load_lottiefile(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)
# if "input" not in  st.session_state:
#     st.session_state["input"] =
