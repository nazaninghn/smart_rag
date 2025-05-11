import os
from dotenv import load_dotenv
load_dotenv()

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.7)

def summarize_text(text):
    prompt = PromptTemplate.from_template(
        "Summarize the following text in 3 sentences:\n\n{text}"
    )
    return llm(prompt.format(text=text))

def paraphrase_text(text):
    prompt = PromptTemplate.from_template(
        "Paraphrase this in a different style:\n\n{text}"
    )
    return llm(prompt.format(text=text))

def expand_to_article(text):
    prompt = PromptTemplate.from_template(
        "Turn this into a full article with title, introduction, and conclusion:\n\n{text}"
    )
    return llm(prompt.format(text=text))
