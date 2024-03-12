import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from pandasai.llm.openai import OpenAI
from pandasai import SmartDataframe
from pandasai import Agent
from htmlTemplates import css, bot_template, user_template


load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
os.environ["PANDASAI_API_KEY"] = os.getenv('YOUR_PANDASAIAPI_KEY')
# with open('styles.css') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
st.set_page_config(page_title="CSV-GPT",layout='wide',page_icon=":bar_chart:")

def chat_wtih_csv(df,prompt):
    llm =OpenAI(temperature=1)
    # pandas_ai = SmartDataframe(df=df,config={"llm":llm})

    pandas_ai = Agent(dfs=df,config={"llm":llm},memory_size=10)
    # pandas_ai.train(docs="The data for January starts from row 2 till row 7489")

    # response = pandas_ai.chat("How many rows are considered for January?")
    # print(response)
    

    result = pandas_ai.chat(prompt)
    print(result)
    
    return result


st.markdown("<h1 style='text-align: center; color: #927fe6; padding:0px 100px 20px 100px;font-size:4rem'>CSV Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #927fe6; padding:0px 100px 80px 100px;font-size:2rem;'>Interact with your Data, Seamlessly</h2>", unsafe_allow_html=True)



col1, col2 =st.columns([5, 2])

with col2:
    st.header("Upload the .csv file here",divider="violet")
    input_csv = st.file_uploader("Upload here",type=['csv'])
    
with col1:
    if input_csv is not None:
        st.success("CSV Uploaded Successfully, reference shown below", icon="✅")
        data = pd.read_csv(input_csv)

        st.dataframe(data)
    

        st.info("Interact with your Data")
        input_text = st.text_area("Enter your query")
        if input_text is not None:
            if st.button("Enquire"):
                st.write(user_template.replace("{{MSG}}", input_text), unsafe_allow_html=True)
                
                # st.info("Your query: "+input_text)

                result = chat_wtih_csv(data,input_text)
                if isinstance(result, pd.DataFrame):
                    st.dataframe(result)
                else:
                    st.success(result)
                # st.write(bot_template.replace(
                # "{{MSG}}", result), unsafe_allow_html=True)
        

     


                  

