from django.shortcuts import render, redirect
from django.conf import settings
from django.http import *
from django.template import loader
from .models import *
from .forms import *
from django.contrib import messages
import json
import random
import string

# Create your views here.
def post_list(request):
    srcs = []
    srcs.append(('/static/images/Vtq8Qp.jpg','#london','/post/Vtq8Qp'))
    srcs.append(('/static/images/DMyHTg.jpg','#autumn','/post/DMyHTg'))
    srcs.append(('/static/images/P5hhR3.jpg','#road','/post/P5hhR3'))
    srcs.append(('/static/images/taCU4B.jpg','#city','/post/taCU4B'))
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'NPFinal/index.html', {'srcs':srcs})

# return login html
def login(request):
    # srcs = ['/static/images/home-img-2.jpg', '/static/images/home-img-3.jpg', '/static/images/home-img-2.jpg', '/static/images/home-img-3.jpg']
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        m = form['account'].value()
        p = form['password'].value()
        user = Reg.objects.filter(mail=m)[0]
        if not user:
            return render(request, 'NPFinal/login_redirect.html', {'msg':'user not exist'})
        if not user.password == p:
            return render(request, 'NPFinal/login_redirect.html', {'msg':'oops, wrong password'})
        if form.is_valid():
            return render(request, 'NPFinal/login_redirect.html', {'msg':'login successfully'})
    else:
        form = LoginForm()           
    return render(request, 'NPFinal/login.html', {'form': form})

# return register html
def register(request):
    srcs = ['/static/images/home-img-2.jpg', '/static/images/home-img-3.jpg', '/static/images/home-img-2.jpg', '/static/images/home-img-3.jpg']
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'NPFinal/register_redirect.html', {'msg':'register successfully'})

        else:
            return render(request, 'NPFinal/register_redirect.html', {'msg':'register fail'})
    else:
        form = RegForm()        
    return render(request, 'NPFinal/register.html', {'form': form})

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
    #for c in com:
     #   if com.hash_tag == hash_name:
      #      comments[com.author] = com.comment
            return render(request, 'NPFinal/demo.html', {'src': '/static/images/'+p.img_name, 'tag': p.hash_tag})

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
    return HttpResponse('/thanks')
def mypage(request, id):
    pass

def base(request):
    return render(request, 'NPFinal/base.html', {})
	
def login_redirect(request):
    return render(request, 'NPFinal/login_redirect.html',{})






