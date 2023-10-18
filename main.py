import openai
import streamlit as st
import utils
import numpy as np
from PIL import Image
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser

def main():
    print("Hello world")
    openai.api_key = st.secrets["openai_key"]

    model = ChatOpenAI(temperature=0, openai_api_key=st.secrets["openai_key"])
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You're a very knowledgeable historian who provides accurate and eloquent answers to historical questions."),
        ("human", "{question}"),
    ])
    runnable = prompt | model | StrOutputParser()

    for chunk in runnable.stream({"question": "How did Mansa Musa accumulate his wealth?"}):
        print(chunk, end="", flush=True)

if __name__ == "__main__":
    main()
