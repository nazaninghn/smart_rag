import os
from dotenv import load_dotenv
load_dotenv()

from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory


memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

def get_chatbot():
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local("vectorstore", embeddings)
    retriever = db.as_retriever()
    llm = OpenAI(temperature=0)
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        verbose=False
    )
    return chain


def get_answer_with_memory(query):
    chain = get_chatbot()
    response = chain.run(query)
    return response
