import streamlit as st
import tensorflow as tf
import numpy as np

def model_predict_image(image):
    model = tf.keras.models.load_model('trained_model.h5')
    img = tf.keras.preprocessing.image.load_img(image, target_size=(64,64))
    input_arr = tf.keras.preprocessing.image.img_to_array(img)
    input_arr = np.array([input_arr])
    predictions = model.predict(input_arr)
    return np.argmax(predictions)


# Background image
original_title = '<h2 style="font-family:Poppins,sans-serif; color: #F2C18D; font-size: 40px;">Plant Palette</h2>'
st.markdown(original_title, unsafe_allow_html=True)
header = '<h3 style="font-family:Poppins,sans-serif; color: #337357; font-size: 35px;">A Fruit - Vegetable Classifier Model</h3>'
st.markdown(header, unsafe_allow_html=True)

# st.markdown('<link rel="stylesheet" href="styles.css">')
# st.markdown("""
#     <header class="header">
#         <a href="" class="logo">Portfolio.</a>
#         <nav class="navbar">
#             <a href="#HOME" class="nav-home">Home</a>
#             <a href="#ABOUT" class="nav-home">About</a>
#             <a href="#PREDICTION" class="nav-home">Prediction</a>
#         </nav>
#     </header>

# """, unsafe_allow_html = True)

# st.sidebar.title("Dashboard")
# st.sidebar.markdown(" ")
# st.sidebar.markdown(" ")
# home = st.sidebar.markdown("<a href='#' style='text-decoration: none; font-size: 20px; color: red;'>Home</a>",unsafe_allow_html=True)
# st.sidebar.markdown(" ")
# about = st.sidebar.markdown("<a href='#' style='text-decoration: none; font-size: 20px; color: red;'>About</a>",unsafe_allow_html=True)
# st.sidebar.markdown(" ")
# prediction = st.sidebar.markdown("<a href='#' style='text-decoration: none; font-size: 20px; color: red;'>Prediction</a>",unsafe_allow_html=True)

# if home:
#     st.markdown('<h2 style = "font-size: 30px;">I am a model built using Deep Learning which helps to classify Fruits and Vegetables.</h2>', unsafe_allow_html=True)

# elif about:
#     st.header("About Project")
#     st.subheader("About Dataset")
#     st.text("This dataset is taken from Kaggle. Here's the link below")
# st.sidebar.markdown("### Navigation")

# st.sidebar.title("Dashboard")
# selected_option = st.sidebar.selectbox("Navigation", ["Home", "About", "Prediction"])
# selected_option = st.sidebar.radio("", ["Home", "About", "Prediction"], key="sidebar_radio")


# # Content based on selected option
# if selected_option == "Home":
#     st.markdown(" ")
#     st.markdown('<h2 style="font-size: 30px;">I am a model built using Deep Learning which helps to classify Fruits and Vegetables.</h2>', unsafe_allow_html=True)
# elif selected_option == "About":
#     st.markdown(" ")
#     st.header("About Project")
#     st.subheader("About Dataset")
#     st.text("This dataset is taken from Kaggle. Here's the link below")
#     st.write("Insert Kaggle dataset link here")
# elif selected_option == "Prediction":
#     st.markdown(" ")
#     st.write("Prediction section content goes here")


image = st.file_uploader("Choose an Image")
# col1, col2, col3, col4 = st.columns(4)
# with col1:
#    pass
# with col2:
#     if(st.button('Show Image')):
#        st.image(image, width = 400)
# with col3:
#    pass
# with col4:
#     if(st.button('Predict')):
#        st.snow()
#     # st.write("Our Prediction")
#        result_index = model_predict_image(image)
#     # Reading Labels
#        with open("labels.txt") as f:
#         content = f.readlines()
#        label = []
#     # st.write(content)
#        for i in content:
#         label.append(i[:-1])
#        st.success("The given image is {}".format(label[result_index].capitalize()))
button_col1, button_col2 = st.columns(2)

with button_col1:
    if st.button('Show Image') and image:
        st.image(image, width=400)

with button_col2:
    if st.button('Predict'):
        st.spinner()
        if image is not None:
            image_placeholder = st.empty()
            # st.image(image, width=400)
            result_index = model_predict_image(image)
            with open("labels.txt") as f:
              content = f.readlines()
            label = [i for i in content]
            image_placeholder.image(image, width=400)
            st.success("The given image is {}".format(label[result_index].capitalize()))

# Adding CSS to create space between buttons
st.markdown(
    """
    <style>
    .stButton > button {
        margin-top: 20px;
        margin-left: 140px;
        background-color: #7DB862 !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)