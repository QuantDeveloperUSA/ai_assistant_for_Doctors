import streamlit as st
from langchain.llms import OpenAI

# for a parrot, we can use this character 🦜
# for a chain, we can use this character 🔗
# for a doctor, we can use this character 👨‍⚕️
# for a PHD Professor, we can use this character 👨‍🏫
# for an assistant, we can use this character 👨‍💼
# for an Engineer, we can use this character 👨‍🔧
# for A.I., we can use this character 🤖


st.title('👨‍⚕️ A.I. Assistant for Doctors')

openai_api_key = st.sidebar.text_input('What is the Magic Word?')
Context_for_assistant_Prompt = "A Medical doctor is talking to his assistant about a medical task. The doctor asks: "
Contextualize_the_Assistant_Answer = "The assistant replies: "


Context_for_PHD_Prompt = "A Medical Doctor asks his PHD Professor: "
Contextualize_the_PHD_Answer = "The PHD Professor replies: "


def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('Doctors_form'):
  assistant_text = Context_for_assistant_Prompt + st.text_area('Enter text:', 'What is an Aspirin Good for?')  + Contextualize_the_Assistant_Answer
  submitted_to_assistant = st.form_submit_button('Ask the Assistant 👨‍💼')

  PHD_text = Context_for_PHD_Prompt + st.text_area('Enter text:', 'What is an Aspirin Good for?')  + Contextualize_the_PHD_Answer
  submitted_to_PHD = st.form_submit_button('Ask the PHD Professor 👨‍🏫')

  if not openai_api_key.startswith('sk-'):
    st.warning('That is not the right Magic word!', icon='⚠')
  if submitted_to_assistant and openai_api_key.startswith('sk-'):
    generate_response(assistant_text)