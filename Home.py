import pandas
import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")

col1, col2= st.columns(2)
with col1:
    st.image('images/photo.png',width=470)
with col2:
    st.title("Giuseppe D'Aiello")
    contest="""
    Mi chiamo Giuseppe D'Aiello,
     sono un appassionato di informatica con un forte interesse per 
     la programmazione e sto attualmente studiando Python,
      con l'obiettivo di diventare un esperto 
      specializzato in intelligenza artificiale. 
      Questo sito è una raccolta dei miei progetti in Python, 
      una sorta di repository per esplorare le app che ho sviluppato 
      lungo il mio percorso di apprendimento e crescita.
    
    """

    st.markdown(f"<p style='font-size:15px; font-family:courier;background-color:#F0F8FF;padding:5px;'><b>{contest}",unsafe_allow_html=True)
    #st.info(contest)

descrizione=("Qui sotto puoi trovare le app che ho creato in Python. Sentiti libero di contattarmi!")
st.markdown(f"<p style='font-size:17px;font-family:georgia;'>{descrizione}", unsafe_allow_html=True)


col3, empty_col,col4= st.columns([1.5,0.5,1.5])

df = pandas.read_csv('data.csv', sep=';')

with col3:
    for index,row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index,row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")
