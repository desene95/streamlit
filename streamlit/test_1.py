import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = "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"

class ChatBotApp:
    def __init__(self):
        self.chat_history = []

    def run(self):
        st.title("OpenAI Chat Bot")

        # Display chat history
        st.header("Chat History")
        for message in self.chat_history:
            st.write(message)

        # Text input for user to type a message
        user_message = st.text_input("Your Message")

        # Button to send a message to the chatbot
        if st.button("Send"):
            if user_message:
                self.add_to_chat_history(f"You: {user_message}")
                bot_response = self.get_bot_response(user_message)
                self.add_to_chat_history(f"Bot: {bot_response}")

        # Button to clear chat history
        if st.button("Clear Chat History"):
            self.clear_chat_history()

    def add_to_chat_history(self, message):
        self.chat_history.append(message)

    def clear_chat_history(self):
        self.chat_history = []

    def get_bot_response(self, user_message):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"You: {user_message}\nBot:",
            max_tokens=50
        )
        return response.choices[0].text.strip()

if __name__ == "__main__":
    app = ChatBotApp()
    app.run()
