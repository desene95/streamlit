import streamlit as st 
import requests
import os
import json
from flask import Flask
import openai

#app = Flask(__name__)
class App():
    st.set_page_config(page_title="Cloud chatbot")
    def clear_chat():
        st.session_state.chat_history = []

    def run(self):
        
        
        with st.sidebar:
            #st.button("clear chat", on_click=clear_chat())
            openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
            "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
            "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
            "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

        
        openai.api_key = openai_api_key
        if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])
        if 'chat_history' not in st.session_state:
            st.session_state["chat_history"] = []
        for user_msg in st.session_state.chat_history:
            
            st.chat_message(user_msg["role"]).write(user_msg["content"])

        
        
        #bot_msg = st.chat_message("assistant")
        #bot_msg.write("How May I help you today?")
        
        
        user_input = st.chat_input(
                            "ask a question", key="user_input")
        
        
     
        #st.session_state.clicked = False
        
        
            #st.button('Clear Chat', on_click=st.session_state.chat_history.clear())
            #user_chat = True
            #while user_chat:
        #reset_butt = st.button('Clear',on_click=st.session_state.chat_history.clear())
        if st.session_state.user_input:
            
            #st.session_state.messages.append({"role":"user","content":user_input})
            
            st.session_state.chat_history.append({"role":"user","content":user_input})
            #st.session_state.user_input = ""
            st.chat_message("user").write(user_input)
            
            #bot_reply = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages )
            bot_reply = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.chat_history )
            #messages=st.session_state.messages))
            msg = bot_reply.choices[0].message
            #st.session_state.messages.append(msg)
            st.session_state.chat_history.append(msg)
            st.chat_message("assistant").write(msg.content)
    with st.sidebar:

       if st.button('clear chat'):
            clear_chat()
        
        
        #if reset_butt:
            #st.button('Clear chat',on_click=st.session_state.chat_history.clear())
            #st.session_state.chat_history=[]
    #def clear_chat(self):
   
        #if st.button('Clear Chat'):
        #st.button("Clear Chat", on_click=st.session_state.chat_history.clear())
                #reset_butt = st.button('Clear chat',on_click=st.session_state.chat_history.clear())


        
        #if reset_butt:
                #st.button('Clear chat', on_click=st.session_state.messages.clear())
            
            #if reset_butt:
             #   st.session_state.chat_history.clear()
            


        #clear_hist = st.session_state.chat_history = []
        
        
    
        
            #def clear_chat():
        #st.session_state.messages = st.session_state.messages[1:]
                #st.button('Clear Chat', on_click=st.session_state.chat_history.clear())
            #clear_chat()
        
        #clear_chat = del st.session_state[messages]

        # reset_chat = st.button("clear chat")
        # if reset_chat:
        #     st.session_state.messages = None

       # def clear_chat():
            #del st.session_state["chat_history"]

        #    st.session_state.messages =  None
             
        #st.button('Clear Chat', on_click=clear_chat())
        
        #if user_input:

        #st.session_state.my_text.append()
        #if "messages" not in st.session_state:
         #   st.session_state["messages"] = [{"role": "assistant", "content": "how can i help you?"}]

  

if __name__ =="__main__":
 
    app = App()
    app.run()
    
