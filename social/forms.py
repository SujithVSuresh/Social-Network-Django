from django import forms
from django.db import models
from django.db.models import fields
from . models import CommentReply, Post, Comment


class PostForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':'3', 'placeholder':'Say Something...'}))

    class Meta:
        model = Post
        fields = ['body']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':'3', 'placeholder':'Add Comments'}))

    class Meta:
        model = Comment
        fields = ['comment']   


class CommentReplyForm(forms.ModelForm):
    comment_reply = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder':'Add Comment Reply'}))
    
    class Meta:
        model = CommentReply
        fields = ['comment_reply']
