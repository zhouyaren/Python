#!-*-coding:utf-8-*-
from django import forms

"""  
实现博客的评论功能
"""

class CommentForm(forms.Form):
    name = forms.CharField(max_length=16)

    email = forms.EmailField()

    content = forms.CharField(max_length=128)