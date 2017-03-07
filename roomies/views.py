from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer
# Create your views here.

class ProfileStuff(APIView):
    def get(self,request):
        return Response(ProfileSerializer(request.user).data)