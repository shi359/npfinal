from django.shortcuts import render, redirect, render_to_response
from django.conf import settings
from django.http import *
from django.template import loader
from .models import *
from .forms import *
from django.contrib import messages
import json
import random
import string
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth

# Create your views here.
def post_list(request):

    if request.user != 'AnonymousUser':
        return render(request,'NPFinal/mypage.html')
    srcs = []
    srcs.append(('/static/images/Vtq8Qp.jpg','#london','/post/Vtq8Qp'))
    srcs.append(('/static/images/DMyHTg.jpg','#autumn','/post/DMyHTg'))
    srcs.append(('/static/images/P5hhR3.jpg','#road','/post/P5hhR3'))
    srcs.append(('/static/images/taCU4B.jpg','#city','/post/taCU4B'))
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'NPFinal/index.html', {'srcs':srcs})

# return login html
def login(request):
    if request.method == 'POST':
        
        form = LoginForm(request.POST)
        m = form['account'].value()
        p = form['password'].value()
        user = auth.authenticate(username=m, password=p)

        if user and user.is_active:
            auth.login(request, user)
            #request.user = user
            return render(request, 'NPFinal/login_redirect.html', {'msg':'login successfully'})
        elif not user:
            return render(request, 'NPFinal/login_redirect.html', {'msg':'user not exist'})
        elif not user.password == p:
            return render(request, 'NPFinal/login_redirect.html', {'msg':'oops, wrong password'})
        #if form.is_valid():
        #    request.user = user
        #    return render(request, 'NPFinal/login_redirect.html', {'msg':'login successfully'})
    else:
        print(request.user)
        print(request.user.is_authenticated())
        if request.user.is_authenticated():
            return render(request, 'NPFinal/login_redirect.html', {'msg':'login successfully'})
        form = LoginForm()           
    return render(request, 'NPFinal/login.html', {'form': form})

# return register html
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        #print(form)
        #print(form.cleaned_data.get('username'))
        #print(form.cleaned_data.get('password1'))
        #print(form.is_bound)
        print(form._errors)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return render(request, 'NPFinal/register_redirect.html', {'msg':'register successfully'})
        else:
            return render(request, 'NPFinal/register_redirect.html', {'msg':form._errors})
    else:
        if request.user.is_authenticated():
            return render(request, 'NPFinal/register_redirect.html', {'msg':'login successfully'})
        form = UserCreationForm()
    return render(request, 'NPFinal/register.html', {'form':form})
    #return render_to_response(request, 'register.html',locals())

def upload(request):
    if request.method == 'POST':
        # store file
        #print(settings.IMAGES_ROOT+request.FILES['image'].name)
        def rand_name():
            charset = string.ascii_uppercase + string.ascii_lowercase + string.digits
            return ''.join(random.choice(charset) for _ in range(6))

        file_exten = request.FILES['image'].name.split('.')[-1]
        imgname = rand_name() + '.' + file_exten
        destination_path = open(settings.IMAGES_ROOT+ imgname, "wb+")
        image = request.FILES['image']
        for chunk in image.chunks():
            destination_path.write(chunk)
        destination_path.close()
        Post.objects.create(
            img_name = imgname,
            hash_tag = request.POST.get('hash')
        )
        #handle_uploaded_file(request.FILES['file'])
        # return post with its hash
        return HttpResponse(json.dumps({'url':'/post/'+imgname.split('.')[0]}), content_type = "application/json")

def post(request, hash_name):
    posts = Post.objects.all()
    com = Comment.objects.all()
    comments = {}
    for p in posts:
        if p.img_name.split('.')[0] == hash_name:
            print('/static/images/'+p.img_name)
    for c in com:
        if c.hash_tag == hash_name:
            comments[c.author] = c.comment
    return render(request, 'NPFinal/demo.html', {'src': '/static/images/'+p.img_name,'tag': p.hash_tag, 'comments':comments.items()})

def search(request):
    keyword = request.POST.get('keyword')
    return HttpResponse(json.dumps({'url':'/result/'+keyword}), content_type="application/json")

def result(request, hash_name):
    post = Post.objects.all()
    results = []
    for p in post:
        if hash_name in p.hash_tag:
            results.append(('/static/images/'+p.img_name,p.hash_tag,'/post/'+p.img_name.split('.')[0]))
    return render(request,'NPFinal/index.html',{'srcs':results})

def comment(request):
    c = request.POST.get('comment')
    namelist = ['nigger','yellow monkey','big cock','9.2','red neck','white trash','douchebag','slutty cat','local mama']
    name = random.choice(namelist)
    hashtag = request.POST.get('hash')
    hashtag = hashtag.split('post/')[1]
    Comment.objects.create(
      hash_tag = hashtag,
      author = name,
      comment = c
    ) 
    return HttpResponse(json.dumps({'url':'/post/'+hashtag}),content_type = "application/json")

def favor(request):
    n = request.POST.get('user')
    i = request.POST.get('image')
    if not Favor.objects.all().filter(name=n,like=i).exists():
        Favor.objects.create(
            name = n,
            like = i
        )
    return render(request,'NPFinal/index.html',{})   
def mypage(request, id):
    return render(reuqest,'NPFinal/mypage.html',{})

def base(request):
    return render(request, 'NPFinal/base.html', {})
	
def login_redirect(request):
    return render(request, 'NPFinal/login_redirect.html',{})






