from rest_framework.views import APIView
from rest_framework.response import Response
from .rag_engine import get_answer_with_memory

class RAGApi(APIView):
    def post(self, request):
        query = request.data.get("query")
        if not query:
            return Response({"error": "Query is required"}, status=400)
        answer = get_answer_with_memory(query)
        return Response({"answer": answer})
