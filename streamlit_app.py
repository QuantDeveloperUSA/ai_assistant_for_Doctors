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
# openai_api_key will be read preferably from config.txt if the file exists, otherwise, it will be read from the enviroment variable API_TOKEN
# Open the file config.txt and read the API_TOKEN from it
try:
  with open('config.txt') as f:
    openai_api_key = f.readline()
except:
  openai_api_key = st.secrets["API_TOKEN"]
#openai_api_key = st.sidebar.text_input('What is the Magic Word?')


Context_for_assistant_Prompt = "A Medical doctor is talking to his assistant about a medical task. The doctor asks: "
Contextualize_the_Assistant_Answer = "The assistant (who happens to be a Medical PHD with several masters ad deeply understands Medicine for humans) replies: "


Context_for_PHD_Prompt = "A Medical Doctor asks his PHD Professor: "
Contextualize_the_PHD_Answer = "The PHD Professor replies: "


def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('Doctors_form'):
  assistant_text = Context_for_assistant_Prompt + st.text_area('Enter text:', 'What is an Aspirin Good for?')  + Contextualize_the_Assistant_Answer
  #the color of the submit button is blue
  submitted_to_assistant = st.form_submit_button('Ask the Assistant 👨‍💼', help='Once you write your query, Click on this button')
  if not openai_api_key.startswith('sk-'):
    st.warning(openai_api_key + ' is not the right Magic word!', icon='⚠')
  if submitted_to_assistant and openai_api_key.startswith('sk-'):
    generate_response(assistant_text)


# to change the color of the submit button to green, we can use this code
# submitted_to_assistant = st.form_submit_button('Ask the Assistant 👨‍💼', help='Click to submit the form')    