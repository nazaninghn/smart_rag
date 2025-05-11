import os
from dotenv import load_dotenv
load_dotenv()

from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA

def create_faiss_tool():
    embeddings = OpenAIEmbeddings()
    
    # اضافه کردن allow_dangerous_deserialization به True
    db = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)
    retriever = db.as_retriever()
    
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=0),
        retriever=retriever,
        return_source_documents=False
    )
    
    return Tool(
        name="VectorSearch",
        func=qa.run,
        description="Use this tool to answer questions based on documents."
    )

def run_agent(query):
    faiss_tool = create_faiss_tool()

    agent = initialize_agent(
        tools=[faiss_tool],
        llm=OpenAI(temperature=0),
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    result = agent.run(query)
    return result

