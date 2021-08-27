from django.contrib import admin
from .models import CommentReply, Post, UserProfile, Notification

# Register your models here.
admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(CommentReply)
admin.site.register(Notification)