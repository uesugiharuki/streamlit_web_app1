import streamlit as st  


with st.form(key='profile_form'):

    #textbox
    name=st.text_input('名前')
    address=st.text_input('住所')
    
    #selectbox
    age_category=st.selectbox(
        '年齢層',
        ('子供(18未満)','大人(18以上60未満)','シニア(60以上)')    )
    
    
    
    sumit_btn=st.form_submit_button('送信')
    cancel_btn=st.form_submit_button('キャンセル')
    if sumit_btn:
        st.text(f'{address}にお住みの{name}さん、こんにちは')
        st.text(f'年齢層　:  {age_category}')