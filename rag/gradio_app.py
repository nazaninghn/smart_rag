import gradio as gr
from rag_engine import get_answer

def ask(query):
    return get_answer(query)

gr.Interface(fn=ask, inputs="text", outputs="text", title="RAG Assistant").launch()
