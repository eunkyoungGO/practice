import streamlit as st
import os

upload_dir = 'files'

uploaded_file=st.file_uploader("업로드하숑")

if uploaded_file is not None:
    try:
        if not os.path.exists(upload_dir):
            os.mkdir(upload_dir)
        with open(os.path.join('files',uploaded_file.name),'wb') as f:
            f.write(uploaded_file.getbuffer())
        st.success('업로드성공')
    except OSError:
        st.error('업로드에러')