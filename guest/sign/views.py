from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
#def index(request):
   # return HttpResponse("Hello Django!")
def index(request):
    return render(request,"index.html")

#登陆
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)#登陆
            response = HttpResponseRedirect('/event_manage/')
           # response.set_cookie('user', username, 3600) #添加浏览器cookie
            request.session['user'] = username #将session信息记录到浏览器
            return response
        else:
            return render(request,'index.html',{'error':'username or password error!'})

#发布会管理
@login_required
def event_manage(request):
    # username = request.COOKIES.get('user','')#读取浏览器cookie
    username = request.session.get('user', '')  # 读取浏览器session
    event_list =Event.objects.all()
    return render(request,"event_manage.html",{"user":username,"events":event_list})

@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get('name', '')
    event_list = Event.objects.filter(name=search_name)
    return render(request, "event_manage.html", {"user": username, "events": event_list})

@login_required
def guest_manage(request):
    # username = request.COOKIES.get('user','')#读取浏览器cookie
    username = request.session.get('user', '')  # 读取浏览器session
    guest_list =Guest.objects.all()
    paginator = Paginator(guest_list,2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        #如果page不是整数，取第一页的数据
        contacts = paginator.page(1)
        # 如果page不是整数，取第一页的数据
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request,"guest_manage.html",{"user":username,"guests":guest_list})
