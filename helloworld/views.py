from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
import random

def index(request):
	default_msg = "你能夠一次打這麼多個html tag嗎？ 我猜不行，試試看寫迴圈吧!"
	msgs = [default_msg for i in range(len(default_msg))]
	imgids = [random.randint(1, 500) for i in range(len(default_msg))]
	imgurls = ["https://picsum.photos/200/200/?image={}".format(imgid) for imgid in imgids]
	return render(request, 'guestbookver1.html', locals())