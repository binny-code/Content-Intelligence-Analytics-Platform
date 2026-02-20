from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import regression_analysis

@api_view(['GET'])
def stats_report(request):
    result = regression_analysis()
    return Response(result)
