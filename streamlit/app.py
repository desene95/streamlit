import streamlit as st 
import requests
import os
import json

class App:
    def __init__(self):
        self.available_collections = ["test1"]
        self.available_models = ["Flan T5"]
        st.set_page_config(page_title="Cloud chatbot")
        self.sidebar()
    def sidebar(self) -> None:
        with st.sidebar:
            st.markdown(
                "#How to use\n"
                "1. Choose collection \n"
                "2. Ask a question"
            )
            collection_option = st.selectbox(
                'Choose your collection', self.available_collections, key="collection_option"
            )
            if collection_option:
                if st.session_state.collection_selected != collection_option:
                    st.session_state["collection_selected"] = collection_option
            
            model_option = st.selectbox(
                'Choose model', self.available_models, key="model_option"
            )
            if model_option:
                if st.session_state.model_selected != model_option:
                    st.session_state['model_selected'] = model_option
    def run(self):
        def qa_api(self, user_input:str):
            collection_selected = st.session_state['collection_selected']
            if not collection_selected:
                st.warning(
                    "choose a colection"
                )
            model_selected = st.session_state['model_selected']
            if not model_selected:
                st.warning(
                    "choose a model"
                )
            chain_qa = st.session_state['qa']
            if chain_qa is not 'None':
                user_input = st.text_input(
                    "ask a question"
                )

if __name__ =="__main__":
    app = App()
    app.run()