from django.shortcuts import render
from app.models import MyChats
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    frnd_name = request.GET.get('user',None)
    mychats_data = None
    if frnd_name:
        if User.objects.filter(username=frnd_name).exists() and MyChats.objects.filter(me=request.user,frnd=User.objects.get(username=frnd_name)).exists():
            frnd_ = User.objects.get(username=frnd_name)
            mychats_data = MyChats.objects.get(me=request.user,frnd=frnd_).chats
    frnds = User.objects.exclude(pk=request.user.id)
    return render(request,'./index.html',{'my':mychats_data,'chats': mychats_data,'frnds':frnds})