import streamlit as st
from langchain.llms import OpenAI

# for a parrot, we can use this character 🦜
# for a chain, we can use this character 🔗
# for a doctor, we can use this character 👨‍⚕️
# for an Engineer, we can use this character 👨‍🔧
# for A.I., we can use this character 🤖


st.title('👨‍⚕️ A.I. Assistant for Doctors')

openai_api_key = st.sidebar.text_input('What is the Magic Word?')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'please respond in 20 lines: What is an Aspirin Good for?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('That is not the right Magic word!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)