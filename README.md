# 🧠 Smart RAG Assistant

Django + LangChain + OpenAI + FAISS web app with:

- 🔎 Vectorstore search
- 🧠 GPT-based answers
- 🌐 HTML frontend
- 📡 REST API
- 🎛️ Gradio UI

## ⚙️ Run

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python rag/build_vectorstore.py
python manage.py runserver
