import streamlit as st
from PIL import Image
import pickle as pkl
import numpy as np

# class_list = {'2' : 'Positive', '0' : 'Negative', '1' : 'Neutral'}

input_ec = open('ec_vsfc.pkl', 'rb')
encoder = pkl.load(input_ec)

input_md = open('lrc_vsfc.pkl', 'rb')
model = pkl.load(input_md)

st.header('Write a feedback')
txt = st.text_area('', '')

if txt != '':
  if st.button('Predict'):
    feature_vector = encoder.transform([txt])
    label = str((model.predict(feature_vector))[0])
    
    st.header('Result')
    # st.text(label)
    st.text(class_list[label])
