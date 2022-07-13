import streamlit as st 
from PIL import Image

st.title('はるきのページ')
st.caption('これは、テストアプリです。')



#イメージテスト
image=Image.open('./data/img_2.gif')
st.image(image,width=200)