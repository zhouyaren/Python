from django.db import models

# Create your models here.

class Catagory(models.Model):
    """  博客分类 """
    name = models.CharField(max_length=32,verbose_name="分类名称")

    class Meta:
        verbose_name = "分类表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Tag(models.Model):
    """ 博客 tag"""
    name = models.CharField(max_length=32,verbose_name="tag名称")

    class Meta:
        verbose_name = "标签表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Blog(models.Model):
    """  博客 """
    title = models.CharField(max_length=32,verbose_name="标题")
    author = models.CharField(max_length=16,verbose_name="作者")
    content = models.TextField(verbose_name="博客正文")
    created = models.DateTimeField(auto_now_add=True,verbose_name="发布时间")
    tags = models.ManyToManyField(Tag,verbose_name="标签")
    catagory = models.ForeignKey(Catagory,verbose_name="分类",on_delete = models.SET_NULL,null=True,blank=True)

    class Meta:
        verbose_name = "博客表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(models.Model):
    """ 评论 """
    name = models.CharField(max_length=32,verbose_name="评论人")
    email = models.EmailField(verbose_name="邮箱")
    content = models.CharField(max_length=240,verbose_name="评论内容")
    created = models.DateTimeField(auto_now_add=True,verbose_name="发布时间")
    blog = models.ForeignKey(Blog,verbose_name="博客",on_delete = models.CASCADE)

    class Meta:
        verbose_name = "评论表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content