import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
import openai

load_dotenv()



def free_edition_llm(company:str, job_title:str, cv_pdf, job_des:str, temperature:int):
    openai_api_key = os.getenv('OPENAI_API_KEY')
    temperature = temperature
    
    llm = OpenAI(model_name = "text-ada-001", 
                 temperature = temperature, 
                 openai_api_key=openai_api_key)

    return llm("Hello, please in max 10 words tell me about AI")