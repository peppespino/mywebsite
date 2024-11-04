import pandas
import streamlit as st
from send_email import send_email
import pandas

st.header('Contact Me')

with st.form(key='email_forms'):

    user_email = st.text_input('Il tuo indirizzo Mail',placeholder='utente@esempio.com')

    topics = pandas.read_csv('topics.csv')

    opzioni = st.selectbox('Di cosa vuoi parlarmi?',topics['topic'])
    st.write(f"Hai selezionato: {opzioni}")

    message = st.text_area('IL tuo messaggio',placeholder='Ciao Giuseppe...')

    message=f"""\
Subject: New email from {user_email}

inviata da: {user_email}

Topic: {opzioni}.

{message}


"""
    button = st.form_submit_button('Submit')
    if button:
        send_email(message)
        st.success("Email inviata con successo!")