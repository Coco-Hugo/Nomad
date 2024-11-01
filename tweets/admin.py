from django.contrib import admin
from .models import Tweet, Like

# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                "payload",
                "user",
            ),
        }),
    )
    

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                "user",
                "tweet",
            ),
        }),
    )
    