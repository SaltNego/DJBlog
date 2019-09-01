# -*- coding:utf-8-*-
from __future__ import unicode_literals

from django.shortcuts import render

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import markdown
from Blog.models import *
from Blog.forms import CommentForm
from django.http import Http404
from templatetags import custom_markdown
#from pygmentize import pygmentizer
def get_blogs(request):
    blogs = Blog.objects.all().order_by('-created')
    tags = Tag.objects.all()
    categories = Catagory.objects.all()
    ctx = {
        'blogs':blogs,
        'categories':categories,
        'tags':tags
    }
    return render(request,'blog_list.html',ctx)
    

def get_details(request,blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
        itscontent = blog.content
        '''
        blog.content = markdown.markdown(itscontent,
                                        extensions=[
                                        'markdown.extensions.extra',
                                        'markdown.extensions.codehilite',
                                        'markdown.extensions.toc',
                                    ])
        '''
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
    ctx = {
        'blog':blog,
        'comments':blog.comment_set.all().order_by('-created'),
        'form':form
    }
    return render(request,'blog_details.html',ctx)

def get_category(request,blog_cate):
    cate_str = blog_cate
    try:
        blogs = Blog.objects.filter(catagory__name__icontains=cate_str).order_by('-created')
        return render(request,'cate_list.html',{'blogs':blogs})
    except Blog.DoesNotExist:
        raise Http404


def get_tag(request,blog_tag):
    try:
        blogs = Blog.objects.filter(tags__name__icontains=blog_tag).order_by('-created')
        return render(request,'tag_list.html',{'blogs':blogs})
    except Blog.DoesNotExist:
        raise Http404    
# Create your views hre.
