from django.shortcuts import render,render_to_response
# Create your views here.
from Blog.models import *
from django.http import Http404
from Blog.forms import CommentForm

def get_blogs(request):
    blogs = Blog.objects.all().order_by('-created')
    return render_to_response('Blog/blog_list.html',{'blogs':blogs})


def get_blogs_details(request,blog_id):
    try:
        blog = Blog.objects.get(id = blog_id)
    except Blog.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)

    ctx= {
        'blog':blog,
        'commets':blog.comment_set.all().order_by('-created'),
        'form':form
    }

    return render(request,'Blog/blog_details.html',ctx)

#
# forms组件
# django中的Form组件有以下几个功能：
# 生成HTML标签
# 验证用户数据（显示错误信息）
# HTML Form提交保留上次提交数据
# 初始化页面显示内容

#forms组件最大的作用，就是做数据校验
# 校验字段，校验功能都写在 view.py 中
# 网页校验，
#
