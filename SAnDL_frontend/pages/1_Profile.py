import requests
import streamlit as st;
import app_utils as util

st.set_page_config(page_title="sandl", page_icon="🩴", layout="wide", initial_sidebar_state="collapsed")

# goes to login page if not logged in
try:
  set = st.session_state['username']
except:
  util.switch_page('app')
#        position: relative;

st.markdown("""
  <style>
    .st-emotion-cache-79elbk {
      margin-top: -65px;
    } 
    .st-emotion-cache-1wmy9hl {
      margin-top: -32px;
    }
            
    .circle-image {
        width: 200px;
        height: 200px;
        border-radius: 25px;
        overflow: hidden;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
    }
    
    .circle-image img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    [data-testid="stSidebarNav"] {
      background-image: url(https://media.discordapp.net/attachments/1013678935231442944/1175577023574454402/sandlsmall_2.png?ex=656bbc6b&is=6559476b&hm=c920463c2062c3c42e555224fb0dc0afc5188e9451b45c9eb62c64f297c1a1f1&=&width=596&height=127);
      background-repeat: no-repeat;
      margin-top: 20px;
      background-position: 20px 20px;
    }
  </style>
""", unsafe_allow_html=True)

profilecol1, profilecol2, profilecol3 = st.columns([1, 8, 1])

with profilecol1:
  # goes to prompt page
  if st.button('◀  Back'):
    util.switch_page('query')

with profilecol2:
  # pfp
  st.write('')
  st.markdown("<div class=\"circle-image\"><img src=\"https://img.pikbest.com/png-images/qiantu/blue-hand-drawn-rounded-socks-cartoon-icon_2687993.png!sw800\"></div>", unsafe_allow_html=True)

  st.header(st.session_state['username'], divider='gray', anchor=False)

  st.write("")
  if st.button('Show API Key'):
    # gets the api key
    res = requests.post("https://sandl-backend-ny3lmzb4dq-uc.a.run.app/get_api_keys", json={"jwt": st.session_state['userdata']})
    # # test code
    # print(res.status_code)
    apikey = res.json()["keys"][0]
    
    st.text(apikey)
  
  st.write('')
  if st.button('Logout'):
    util.switch_page('app')
  
