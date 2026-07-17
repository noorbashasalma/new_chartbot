#My ChartBot
import streamlit as st
from openai import OpenAI
#________________________________________________________________________________
#Page Config
st.set_page_config(page_title="Mini ChatGPT - Mistral",page_icon="🤖",layout = "centered")
st.title("🤖Salma Mini ChatGPT - (Mistral AI)")
#_____________________________________________________________
#API 
api_key="CQJcS107J0ANQDXYRHIc2dloBYdk5oDi"
#___________________________________________________________
#Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages=[{"role":"system","content":"you are a healpful AI Assistant"}]
#_____________________________________________________________________
#Show Previous Messages
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
#__________________________________________________________________________
#chat Input
prompt=st.chat_input("Type your Message")
if prompt:
    if not api_key:
        st.error("Please Enter Mistral API key")
        st.stop()
    client=OpenAI(api_key=api_key,base_url="https://api.mistral.ai/v1")
    #display User Name
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role":"user","content":prompt})
#__________________________________________________________________________
#generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking......"):
            response=client.chat.completions.create(model="mistral-small-latest",messages=st.session_state.messages)
            reply=response.choices[0].message.content 
            st.markdown(reply)
    st.session_state.messages.append({"role":"assistant","content":"reply"})
#______________________________________________________________________
#side bar
with st.sidebar:
    st.header("Options")
    if st.button("Clear Chat"):
        st.session_state.messages=[{"role":"system","content":"you are a healpful AI"}]
        st.rerun()
    st.markdown("______")
    st.write("**Model:**Mistral/AI")
