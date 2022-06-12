from rest_framework.response import Response
from rest_framework.decorators import api_view
from website.models import Data
from .serializers import DataSerializer

@api_view(["GET"])
def get_data(request):
    link = Data.objects.all()
    serializer = DataSerializer(link, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def post_data(request):
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)