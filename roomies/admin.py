from django.contrib import admin
from roomies.models import UserProfile, UserMatches
# Register your models here.

class ProfilepicAdmin(admin.ModelAdmin):
    pass

class UserMatchAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserProfile, ProfilepicAdmin)
admin.site.register(UserMatches, UserMatchAdmin)