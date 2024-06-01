import fitz
import streamlit as st
import google.generativeai as genai

genai.configure(api_key="YOUR_API_HERE")
model = genai.GenerativeModel(
model_name="gemini-1.0-pro")
convo = model.start_chat(history=[])  


def pdf_text_extractor(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def gemini_response(text):
    convo.send_message("You are a Text summerizer.You will read entire a text and answer me to  quesions which I'll ask to you.\n"+text)
    st.write("Analyzed succefully")

def ask_question(question):
    #question=input("Enter question : ")
    convo.send_message(question)
    response=str(convo.last.text)
    return response

st.title("PDF Summarizer")
path=st.text_input("Enter path of PDF : ")
if path:
    text=pdf_text_extractor(path)
    gemini_response(text)
st.markdown("## Ask Question :")
question=st.text_input("Type your question here :")
if question:
        response=ask_question(question)
        st.markdown("## Answer : ")
        st.write(response)

    
    




