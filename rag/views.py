
import os
from django.core.files.storage import default_storage
from django.shortcuts import render
from .vector_builder import build_vectorstore_from_file
from .agent_engine import run_agent
from .rag_engine import get_answer_with_memory

# View for home page where user can ask questions
def home(request):
    answer = None
    if request.method == "POST":
        query = request.POST.get("query")
        if query:
            try:
                answer = get_answer_with_memory(query)
            except Exception as e:
                answer = f"Error: {str(e)}"
    return render(request, "rag/index.html", {"answer": answer})

# View for file upload and vectorstore creation
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

# View to handle questions using the agent
def agent_view(request):
    result = None
    if request.method == "POST":
        query = request.POST.get("query")
        if query:
            try:
                result = run_agent(query)
            except Exception as e:
                result = f"❌ Error: {str(e)}"
    return render(request, "rag/agent.html", {"result": result})

