from rest_framework.views import APIView
from rest_framework.response import Response
from .rag_engine import get_answer

class RAGApi(APIView):
    def post(self, request):
        query = request.data.get("query")
        if not query:
            return Response({"error": "Query required"}, status=400)
        return Response({"answer": get_answer(query)})
