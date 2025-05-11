from django.shortcuts import render
from .rag_engine import get_answer_with_memory

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


