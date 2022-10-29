from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Profile view in the admin panel
    """
    model = Profile
    list_display = ('id', 'username', 'email', 'date_joined')

    def id(self, obj):
        return obj.id

    def username(self, obj):
        return obj.user.username

    def email(self, obj):
        return obj.user.email

    def date_joined(self, obj):
        return obj.user.date_joined
