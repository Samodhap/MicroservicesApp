from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def health_status(request):
    if request.method == 'GET':  # user requesting data
        return Response({"status":"UP"})
