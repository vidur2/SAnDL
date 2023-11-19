import app_utils as util
import streamlit as st
import time
from pathlib import Path
from datetime import datetime
import requests

st.set_page_config(page_title="sandl", page_icon="🩴", layout="wide", initial_sidebar_state="collapsed")
# sidebar, page, sidebar
#    margin-bottom: 30px;
st.markdown("""
  <style>
  .prompt-font {
    font-size:18px !important;
    margin-bottom: 10px;
    margin-top: 20px;
  }
  .percent-font {
    font-size:30px !important;
    margin-top: 50px;
  }
  
  .st-emotion-cache-79elbk {
    margin-top: -65px;
  }
  .st-emotion-cache-1wmy9hl {
    margin-top: -32px;
  }
            
  [data-testid="stSidebarNav"] {
      background-image: url(https://media.discordapp.net/attachments/1013678935231442944/1175577023574454402/sandlsmall_2.png?ex=656bbc6b&is=6559476b&hm=c920463c2062c3c42e555224fb0dc0afc5188e9451b45c9eb62c64f297c1a1f1&=&width=596&height=127);
      background-repeat: no-repeat;
      margin-top: 20px;
      background-position: 20px 20px;
  }
  </style>
""", unsafe_allow_html=True)


# Create a row with 3 columns
col1, col2, col3 = st.columns([1, 8, 1])

with col3:
    if st.button('👤 Profile'):
        util.switch_page('profile')
        
with col2:
    
    # tab bar 
    query = r"$\textsf{\large Query}$"
    recents = r"$\textsf{\large History}$"
    q, searches = st.tabs([query, recents])

    # query tab
    with q:
      
      st.write('')
      
      st.markdown('<p class="prompt-font">Prompt:</p>', unsafe_allow_html=True)
      promptcontainer = st.container()
      
      user_input = promptcontainer.text_area("", height=50, on_change=None)
      
      container2 = st.container()
      
      if (user_input == ''):
        container2.write('')
        container2.write('')
      else:
        # TO-DO:
        # call api to get value (this would be added to value put into the dict (prob at first pos. hopefully its a set num of chars))
        # Verify Login **
        if 'userdata' not in st.session_state.keys():
          st.info('Not Logged In: Redirecting to Login page...')
          time.sleep(.5)
          util.switch_page('app')
        else: 
          res = requests.post("https://sandl-backend-ny3lmzb4dq-uc.a.run.app/get_intent", json={"jwt": st.session_state['userdata'], "prompt": user_input})
        value = round(res.json()["certaintyValue"] * 100)
        if (value < 10):
           value = '0' + str(value)
        else:
           value = str(value)
        
        # visualization (loading bar)
        container2.markdown("<p class='percent-font'>" + value + "%</p>", unsafe_allow_html=True)
        my_bar = container2.progress(0, text='')
        for percent_complete in range(int(value)):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text='')
        container2.text('Your prompt has a ' + value + "% chance to be non-malicious.")
        
      container2.text('')
      container2.text('')
      container2.text("SAnDL: Sophisticated Anomaly Detection for LLMs")
      now = datetime.now()
      current_time = now.strftime("%H:%M:%S")
      
      if (user_input != ''):
        st.session_state[value + user_input + " " + current_time] = value + user_input + " " + current_time

    # Searches Tab:
    with searches:
      st.write('')
      x = st.header('Recent Searches:', divider='grey', anchor=False)
      
      containerx = st.container()
      containerx.write('')
      containerx.write('')
      
      # sorts dict by reverse time stamp
      t = dict(sorted(st.session_state.items(), key=lambda item: item[1][len(item[1]) - 8:], reverse = True))
      for key in t.keys():
          if (key == st.session_state[key]):
              # everything besides the time stamp 
              tempstring = st.session_state[key][2:len(st.session_state[key]) - 8]
              
              percent = st.session_state[key][:2]
              
              # adds ... if tempstring too long
              if len(tempstring) > 110:
                  tempstring = st.session_state[key][2:112] + "..."
              containerx.text(tempstring + ' — ' + percent + '%')
    