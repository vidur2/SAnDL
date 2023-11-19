# source .venv/bin/activate
# streamlit run <>.py

import streamlit as st
import app_utils as util
from pathlib import Path
from PIL import Image
from io import BytesIO
import requests
import time

st.set_page_config(page_title="SAnDL", page_icon="🩴", layout="wide", initial_sidebar_state="collapsed")

# Example URL
image_url = "https://media.discordapp.net/attachments/1013678935231442944/1175575324210249740/sandll2.png?ex=656bbad6&is=655945d6&hm=d8f4a93a7c3ae90978f820093e2e7c17c18b6125546255afaaeca8ed6716bd4d&=&width=2268&height=486"

# Open image from URL
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))

# close taskbar, page margin, ...
st.markdown("""
<style>
    .st-emotion-cache-1yeub2j {
      display: none;
    }
    .st-emotion-cache-79elbk {
      margin-top: -45px;
    }
    .slogan-font {
      font-size:18px !important;
      margin-bottom: 40px;
      margin-top: 0px;
      text-align: center;
    }
    .bolded {
      font-weight: 1000;   
    }
    [data-testid="stSidebarNav"] {
      background-image: url(https://media.discordapp.net/attachments/1013678935231442944/1175577023574454402/sandlsmall_2.png?ex=656bbc6b&is=6559476b&hm=c920463c2062c3c42e555224fb0dc0afc5188e9451b45c9eb62c64f297c1a1f1&=&width=596&height=127);
      background-repeat: no-repeat;
      margin-top: 20px;
      background-position: 20px 20px;
    }
    section[data-testid="stSidebar"][aria-expanded="true"]{
      display: none;
    }
</style>
""", unsafe_allow_html=True)

logincol1, logincol2, logincol3 = st.columns([1, 8, 1])

with logincol2:
    
    # logo
    st.image(img)
    # caption
    st.markdown('<p class="slogan-font">' + "Developing <span class = \"bolded\">anomaly detection</span> systems for filtration of <span class = \"bolded\">large language model</span> prompts." + '</p>', unsafe_allow_html=True)

    #login form
    profilecontainer = st.container()
    login_form = profilecontainer.form('Login')
    username = login_form.text_input('Username').lower()
    st.session_state['username'] = username
    password = login_form.text_input('Password', type='password')
    if login_form.form_submit_button('Login'):
        st.session_state.pop('FormSubmitter:Login-Login', None)

        # deletes all keys from previous logins
        for key in st.session_state.keys():
            if (key != 'username'):
                st.session_state.pop(key)

        res = requests.post("https://sandl-backend-ny3lmzb4dq-uc.a.run.app/login", json={"email": username, "password": password})
        error = res.status_code

        # login validation
        if error == 200:
          st.session_state['userdata'] = res.json()["jwt"]
          st.success('Login Successful!', icon="✅")
          util.switch_page("query")
        # username exists in db, but password is incorrect
        elif error == 400:
          st.error('Incorrect Password.', icon="🚨")
        # makes new account
        elif error == 500: 
          st.info('Account Not Found: New account created.', icon="ℹ️")
          res = requests.post("https://sandl-backend-ny3lmzb4dq-uc.a.run.app/sign_up", json={"email": username, "password": password})
          res = requests.post("https://sandl-backend-ny3lmzb4dq-uc.a.run.app/login", json={"email": username, "password": password})
          st.session_state['userdata'] = res.json()["jwt"]
          requests.post("https://sandl-backend-ny3lmzb4dq-uc.a.run.app/add_api_key", json={"jwt": st.session_state['userdata']})
          time.sleep(.5)
          util.switch_page("query")