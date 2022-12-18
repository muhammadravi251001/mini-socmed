from django.shortcuts import render,redirect
from .models import * 
from .forms import * 
# Create your views here.

def home(request):
    forums = forum.objects.all()
    count = forums.count()
    #if count == 0: count = "Belum Ada Forum Disini"
    discussions = []
    for i in forums:
        discussions.append(i.discussion_set.all())
    
    #if len(discussions) == 0: discussions = "Belum Ada Komentar Disini"
    
    context={'forums': forums,
              'count': count,
              'discussions': discussions}
    return render(request,'home.html', context)

def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'addInForum.html', context)

def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'addInDiscussion.html', context)