from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def my_api(request):
    return Response({'result': 'ok'})
