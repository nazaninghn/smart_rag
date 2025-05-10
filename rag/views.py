from django.shortcuts import render
from .rag_engine import get_answer

def home(request):
    answer = None
    if request.method == "POST":
        query = request.POST.get("query")
        if query:
            answer = get_answer(query)
    return render(request, "rag/index.html", {"answer": answer})


