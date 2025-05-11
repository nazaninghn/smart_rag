# vectorstore.py
import os
from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# Load the environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_api_key

# Load the vectorstore from the local directory with the dangerous deserialization flag set to True
embeddings = OpenAIEmbeddings()

vector_store = FAISS.load_local(
    "vectorstore",  # The folder where the FAISS vectorstore is saved
    embeddings,
    allow_dangerous_deserialization=True  # You trust the file source
)
print("✅ VectorStore has been loaded successfully.")

# Example usage: perform similarity search with the vectorstore
query = input("Enter a query: ")
docs = vector_store.similarity_search(query, k=3)
for i, doc in enumerate(docs, 1):
    print(f"[Result {i}] {doc.page_content[:200]}...\n")
