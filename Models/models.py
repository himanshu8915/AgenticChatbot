from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings


reasoning_model=ChatGoogleGenerativeAI(model="gemini-2.5-pro")
embedding_model=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
chat_model=ChatGroq(model_name="openai/gpt-oss-120b")

from typing import List
class ModelKit:
    
    @staticmethod
    def return_models()->List:
        return [chat_model,reasoning_model,embedding_model]