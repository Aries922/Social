from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile,post
# Create your views here.

def picbioe(request):
    if request.method=='POST':
        bio = request.POST.get('bios')
        pic = request.FILES.get('image')

        profile = Profile(user=request.user,pic=pic,bio=bio)
        print(bio)
        profile.save()
    return render(request,'profile.html')

def postimage(request):
    if request.method == 'POST':
        about = request.POST.get('about')
        image = request.FILES.get('image')

        most = post( user=request.user,about=about, image=image)
        most.save()

    return redirect('home')

def home(request):
    allposts =post.objects.all()

    context= {'allposts':allposts}
    return render(request, 'login.html',context)