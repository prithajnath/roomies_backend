from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken import views as rest_framework_views
# Create your views here.

class ProfileStuff(APIView):
    def get(self,request):
        return Response(ProfileSerializer(request.user).data)
        
class SignUp(APIView):
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username,email,password)
        user.save()
        #return token for new user
        
            