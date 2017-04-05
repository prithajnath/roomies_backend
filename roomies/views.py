from django.shortcuts import render, get_object_or_404,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken import views as rest_framework_views
from rest_framework.decorators import api_view, permission_classes,renderer_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from roomies.models import UserProfile
from django.template import loader
from django.http import HttpResponse
# Create your views here.
@permission_classes((AllowAny, ))
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

class ProfileStuff(APIView):
    def get(self,request):
        return Response(ProfileSerializer(request.user).data)

@permission_classes((AllowAny, ))      
class SignUp(APIView):
    def post(self,request):
        username = request.POST.get("username")
        if User.objects.filter(username=username):
            return Response({'error':'username already taken'})
        else:
            password = request.POST.get("password")
            email = request.POST.get("email")
            user = User.objects.create_user(username,email,password)
            user.save()
            idx = User.objects.get(username=user.get_username()).pk
            token = Token.objects.raw('select * from authtoken_token where user_id={}'.format(idx))[0]
            return Response({'token':token.key})

class ProfilePicture(APIView):
    def get(self,request):
        user = request.user
        idx = user.pk
        profile = UserProfile.objects.get(user_id=idx)
        return Response({'url':'https://roomies-backend-prithajnath.c9users.io'+profile.avatar.url})
        
class GetMatches(APIView):
    def get(self,request):
        user = request.user
        users = User.objects.all()
        matches = {}
        for i in users:
            if i!=user:
                try:
                    matches[i.get_username()] = UserProfile.objects.get(user_id=i.pk).avatar.url
                except:
                    matches[i.get_username()] = ""
        return Response(matches)
        
class GetMatchProfile(APIView):
    def get(self,request):
        username = request.GET.get("username")
        user = User.objects.get(username=username)
        return Response(ProfileSerializer(user).data)
