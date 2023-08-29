import streamlit as st
from langchain.llms import OpenAI

# for a parrot, we can use this character 🦜
# for a chain, we can use this character 🔗
# for a doctor, we can use this character 👨‍⚕️
# for an Engineer, we can use this character 👨‍🔧
# for A.I., we can use this character 🤖


st.title('👨‍⚕️ A.I. Assistant for Doctors')

openai_api_key = st.sidebar.text_input('What is the Magic Word?')
Context_Prompt = "A Medical doctor is talking to his professional assistant (who happens to be also a PHD in Medicine), about a medical condition. The doctor asks: "
Contextualize_the_Answer = "The assistant replies: "
def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = Context_Prompt + st.text_area('Enter text:', 'What is an Aspirin Good for?')  + Contextualize_the_Answer
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('That is not the right Magic word!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)