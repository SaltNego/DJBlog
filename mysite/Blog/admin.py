# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from Blog.models import *
# 注册的目的就是为了让系统管理员能对注册的这些模型进行管理
admin.site.register([Catagory,Tag,Blog])
# Register your models here.
