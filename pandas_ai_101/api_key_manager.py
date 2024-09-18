"""API Key Manager"""
import os
from dotenv import load_dotenv
import streamlit as st

class APIKeyManager:
    """API Key Manager"""

    def __init__(self):
        load_dotenv()
        self.api_keys = {
            "PANDASAI_API_KEY": os.getenv("PANDASAI_API_KEY"),
            "OPENAI_API_KEY": os.getenv("PLAYGROUND_API_KEY")
        }

    def check_api_keys(self):
        return [key for key, value in self.api_keys.items() if not value]

    def display_api_key_warning(self):
        missing_keys = self.check_api_keys()
        if missing_keys:
            st.warning("⚠️ API Key(s) not set: " + ", ".join(missing_keys))
            st.info("Please set up your API keys in the .env file or in the sidebar below.")

    def setup_api_key_inputs(self):
        st.sidebar.header("API Key Configuration")
        for key in self.api_keys:
            value = st.sidebar.text_input(f"{key}:", value=self.api_keys[key] or "", type="password")
            if value:
                self.api_keys[key] = value
                os.environ[key] = value

    def get_api_key(self, key_name):
        return self.api_keys.get(key_name)