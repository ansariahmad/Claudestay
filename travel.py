# import all necessary libraries
import os
import requests
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores.faiss import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# load api keys
load_dotenv()

# load models
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
chat = ChatAnthropic(temperature=0, anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"), model_name="claude-3-opus-20240229")

# Define the API endpoint
url = "https://api.deepgram.com/v1/speak?model=aura-asteria-en"

# Set your Deepgram API key

# Define the headers
api_key = os.getenv("AURA_API_KEY")
headers = {
    "Authorization": f"Token {api_key}",
    "Content-Type": "application/json"
}

# Define the payload


def get_embeddings(user_query):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")    
    new_db = FAISS.load_local("faiss_index", embeddings)
    docs = new_db.similarity_search(user_query)
    return docs


# Function to generate response based on user query
def get_response(chat, prompt, user_query):
    system = (
    "You are world best travel advisor. Advice the user in best possible"
    )
    human = prompt
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
    docs = get_embeddings(user_query)
    chain = prompt | chat
    output = chain.invoke(
        {
            "context": docs,
            "question" : user_query
        }
    )
    return output.content

# Streamlit app layout
def main():
    st.title("Claudestay")
    
    # api_key = st.text_input("Enter Anthropic API Key....")
    # chat = ChatAnthropic(temperature=0, anthropic_api_key=api_key, model_name="claude-3-opus-20240229")

    
    prompt = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer.
    You must provide answer in markdown table format.\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
"""

    
    # Input box for user query
    user_query = st.text_input("Enter your travel query:")
    
    if st.button("Submit"):
        with st.spinner("Fetching data..."):
            text_response = get_response(chat, prompt, user_query)
            payload = {
            "text": text_response
            }

            # Make the POST request
            st.markdown(f"**Response:** {text_response}")
            # Check if the request was successful
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 200:
                # Save the response content to a file
                with open("your_output_file.mp3", "wb") as f:
                    f.write(response.content)
                st.audio(response.content)
                print("File saved successfully.")
            else:
                print(f"Error: {response.status_code} - {response.text}")
                    

if __name__ == "__main__":
    main()
