import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from pandasai.llm.openai import OpenAI
from pandasai import SmartDataframe
from pandasai import Agent
from htmlTemplates import css, bot_template, user_template


load_dotenv()

openai_api_key = os.getenv('OPEN_API_KEY')
st.set_page_config(page_title="CSV-GPT",layout='wide',page_icon=":bar_chart:")

st.write(css,unsafe_allow_html=True)
card1 ='''
<style>
.card {
  /* Add shadows to create the "card" effect */
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
    border-radius: 5px;
    height:200px;
    width:200px;
    background-color:#1e1f20;
    margin:20px;
}

/* On mouse-over, add a deeper shadow */
.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    background-color:#2f3133    ;

}

/* Add some padding inside the card container */
.container {
  padding: 2px 16px;
}
.cunt{
display:flex;
flex-direction:row;
    justify-content:center;
}
</style>
<div class="cunt">
    <div class="card">
  
  <div class="container">
    <span style='font-size:50px;'>&#128187;</span>
    <h4><b>Step 1</b></h4>    
    <p>Upload the .csv file in the sidebar</p>
  </div>
</div>


<div class="card">
  
  <div class="container">
  <span style='font-size:50px;'>&#128070;</span>
    <h4><b>Step 2</b></h4>
    <p>Click on "Browse files" button and wait</p>
  </div>
</div>
<div class="card">
  
  <div class="container">
  <span style='font-size:50px;'>🔍</span>
    <h4><b>Step 3</b></h4>
    <p>Ask questions from the CSV file</p>
  </div>
</div>
</div>

'''

def chat_wtih_csv(df,prompt):
    llm =OpenAI()
    # pandas_ai = SmartDataframe(df=df,config={"llm":llm})
    pandas_ai = Agent(dfs=df,config={"llm":llm},memory_size=10)
    

    result = pandas_ai.chat(prompt)
    print(result)
    
    return result


st.markdown("<h1 style='text-align: center; color: white;'>Chat to CSV powered by LLM</h1>", unsafe_allow_html=True)

# st.title("")
with st.sidebar:
    st.header("Upload the .csv file here",divider="rainbow")
    input_csv = st.file_uploader("Upload your CSV file",type=['csv'])


if input_csv is not None:
    col1,col2 =st.columns([1,2])
    with col1:
      st.success("CSV Uploaded Successfully")
      data = pd.read_csv(input_csv)
      st.dataframe(data)
    with col2:
        st.info("Chat with your CSV")
        input_text = st.text_area("Enter your query")
        if input_text is not None:
            if st.button("Chat with CSV"):
                st.write(user_template.replace(
                "{{MSG}}", input_text), unsafe_allow_html=True)
                
                # st.info("Your query: "+input_text)
                
                result = chat_wtih_csv(data,input_text)
                st.write(bot_template.replace(
                "{{MSG}}", result), unsafe_allow_html=True)
                # st.success(result)
else:
    st.markdown(card1, unsafe_allow_html=True)
                

