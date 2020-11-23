from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser
from .serializers import ProfilesSerializer


class ProfileDetail(APIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfilesSerializer

    def get(self, request, pk, format=None):
        obj = get_object_or_404(CustomUser, pk=pk)
        serializer = ProfilesSerializer(obj)
        return Response(serializer.data)
