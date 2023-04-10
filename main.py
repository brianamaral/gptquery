"""Python file to serve as the frontend"""
import streamlit as st
from streamlit_chat import message

from langchain.chains import ConversationChain
from langchain.llms import OpenAI

import sqlite3

from custom_chain import load_chain

import pandas as pd

import re

chain = load_chain()

# From here down is all the StreamLit UI.
st.set_page_config(page_title="PhQuery", page_icon=":robot:")
st.header("PhQuery")

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []


def get_text():
    input_text = st.text_input("You: ", "How many orders do we have?", key="input")
    return input_text

def get_query(query):
    print(query)
    pattern = r'"SQLQuery":\s+"(.*?)"'
    match = re.search(pattern, query).group(1)

    conn = sqlite3.connect('olistdata.db')

    df = pd.read_sql_query(match,conn)

    return df


user_input = get_text()

if user_input:
    
    output = chain.run(input=user_input)
    output_result = get_query(output)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)
    st.session_state.generated.append(st.table(output_result))


