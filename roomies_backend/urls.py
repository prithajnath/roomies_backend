"""roomies_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rest_framework_views
from django.conf import settings
from django.conf.urls.static import static
from roomies import views
from rest_framework.response import Response

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^get_profile', views.ProfileStuff.as_view()),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    url(r'sign_up', views.SignUp.as_view()),
    url(r'profile_pic', views.ProfilePicture.as_view()),
    url(r'get_matches', views.GetMatches.as_view()),
    url(r'get_match_profile', views.GetMatchProfile.as_view()),
    url(r'^$', views.index )
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)