from django.contrib import admin
from roomies.models import UserProfile
# Register your models here.

class ProfilepicAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserProfile, ProfilepicAdmin)