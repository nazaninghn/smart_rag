import os
from django.core.files.storage import default_storage
from django.shortcuts import render
from .vector_builder import build_vectorstore_from_file
from .rag_engine import get_answer_with_memory
from .agent_engine import run_agent
from .text_writer import summarize_text, paraphrase_text, expand_to_article

def home(request):
    answer = None
    if request.method == "POST":
        query = request.POST.get("query")
        if query:
            try:
                answer = get_answer_with_memory(query)
            except Exception as e:
                answer = f"❌ Error: {str(e)}"
    return render(request, "rag/index.html", {"answer": answer})

def upload_file(request):
    message = ""
    if request.method == "POST":
        uploaded_file = request.FILES.get("document")
        if uploaded_file:
            filename = default_storage.save(f"temp/{uploaded_file.name}", uploaded_file)
            filepath = os.path.join("media", filename)
            try:
                build_vectorstore_from_file(filepath)
                message = "✅ Vectorstore created successfully!"
            except Exception as e:
                message = f"❌ Error: {str(e)}"
    return render(request, "rag/upload.html", {"message": message})

def agent_view(request):
    answer = None
    if request.method == "POST":
        query = request.POST.get("query")
        if query:
            try:
                answer = run_agent(query)
            except Exception as e:
                answer = f"❌ Error: {str(e)}"
    return render(request, "rag/agent.html", {"answer": answer})

def text_tools_view(request):
    output = ""
    if request.method == "POST":
        input_text = request.POST.get("input_text")
        action = request.POST.get("action")

        if input_text and action:
            try:
                if action == "summarize":
                    output = summarize_text(input_text)
                elif action == "paraphrase":
                    output = paraphrase_text(input_text)
                elif action == "expand":
                    output = expand_to_article(input_text)
            except Exception as e:
                output = f"❌ Error: {str(e)}"
    
    return render(request, "rag/text_tools.html", {"output": output})
