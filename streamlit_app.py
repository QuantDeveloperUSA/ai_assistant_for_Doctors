import streamlit as st
from langchain.llms import OpenAI
# https://github.com/imartinez/privateGPT

st.title('👨‍⚕️ A.I. Assistant for Doctors')
# openai_api_key will be read preferably from config.txt if the file exists, otherwise, it will be read from the enviroment variable API_TOKEN
# Open the file config.txt and read the API_TOKEN from it

openai_api_key = ''
#try:
#  with open('config.txt') as f:
#    openai_api_key = f.readline()
#except:
#  pass
#try:
#  if openai_api_key == '': 
#    openai_api_key = st.secrets["API_TOKEN"]  
#except:
#  pass
if openai_api_key=='':
  openai_api_key = st.sidebar.text_input('OpenAI API Key')

#openai_api_key = st.sidebar.text_input('What is the Magic Word?')


Context_for_assistant_Prompt = "A Medical doctor is talking to his assistant about a medical task. The doctor asks: "
Contextualize_the_Assistant_Answer = "The assistant (who happens to be a Medical PHD with several masters and deeply understands Human Medicine) replies: "

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('Doctors_form'):
  assistant_text = Context_for_assistant_Prompt + st.text_area('Enter text:', 'What is an Aspirin Good for?')  + Contextualize_the_Assistant_Answer
  #the color of the submit button is blue
  submitted_to_assistant = st.form_submit_button('Ask the Assistant 👨‍💼', help='Once you write your query, Click on this button')
  if not openai_api_key.startswith('sk-'):
    st.warning( openai_api_key + ' is not the right Magic word!', icon='⚠')
  if submitted_to_assistant and openai_api_key.startswith('sk-'):
    generate_response(assistant_text)


# to change the color of the submit button to green, we can use this code
# submitted_to_assistant = st.form_submit_button('Ask the Assistant 👨‍💼', help='Click to submit the form')   
# to run this app on the cloud, navigate to https://ai-assistant-for-doctors.streamlit.app/
# to run this app locally, run this command: streamlit run streamlit_app.py 

#https://stripe.com/docs/development/quickstart?lang=python
# https://marketplace.visualstudio.com/items?itemName=seunlanlege.action-buttons
#https://github.com/Sven-Bo/sell-digitial-products-using-streamlit-stripe