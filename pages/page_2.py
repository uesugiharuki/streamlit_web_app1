import streamlit as st 
from PIL import Image



#動画テスト
video_file =open('./data/01.m4a','rb')
video_bytes=video_file.read()
st.video(video_bytes)