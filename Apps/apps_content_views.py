from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ContentItem
from apps.llm_engine.llm_service import analyze_content

@api_view(['POST'])
def create_content(request):
    title = request.data.get("title")
    description = request.data.get("description")

    analysis = analyze_content(description)

    content = ContentItem.objects.create(
        title=title,
        description=description
    )

    return Response({
        "message": "Content created",
        "llm_analysis": analysis
    })
