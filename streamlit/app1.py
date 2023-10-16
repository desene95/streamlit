import streamlit as st 
import requests
import os
import json
from flask import Flask
import openai

#app = Flask(__name__)
class App():
    def run(self):
        st.set_page_config(page_title="Cloud chatbot")
        with st.sidebar:
            openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
            "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
            "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
            "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

        
        openai.api_key = openai_api_key
        if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
        #bot_msg = st.chat_message("assistant")
        #bot_msg.write("How May I help you today?")
        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])
        user_input = st.chat_input(
                            "ask a question", key="user_input")
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        if st.session_state.user_input:
            st.session_state.chat_history.append(("response", st.session_state.user_input))
            #st.session_state.user_input = ""
            st.chat_message("user").write(user_input)
            bot_reply = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages )
            #messages=st.session_state.messages))
            msg = bot_reply.choices[0].message
            st.session_state.messages.append(msg)
            st.chat_message("assistant").write(msg.content)
        #if user_input:

        #st.session_state.my_text.append()
        #if "messages" not in st.session_state:
         #   st.session_state["messages"] = [{"role": "assistant", "content": "how can i help you?"}]


if __name__ =="__main__":
    app = App()
    app.run()