import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader, UnstructuredWordDocumentLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter

def load_document(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    print(f"Detected file extension: {ext}")

    if ext == ".pdf":
        loader = PyPDFLoader(filepath)
    elif ext == ".txt":
        loader = TextLoader(filepath)
    elif ext == ".docx":
        loader = UnstructuredWordDocumentLoader(filepath)
    else:
        raise ValueError(f"Unsupported file format '{ext}'. Supported formats: .pdf, .txt, .docx.")

    return loader.load()

def build_vectorstore_from_file(filepath, persist_path="vectorstore"):
    documents = load_document(filepath)
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(persist_path)
