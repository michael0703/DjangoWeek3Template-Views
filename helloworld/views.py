from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
	default_msg = "你能夠一次打這麼多個html tag嗎？ 我猜不行，試試看寫迴圈吧!"
	msgs = [default_msg for i in range(len(default_msg))]
	return render(request, 'guestbookver1.html', locals())