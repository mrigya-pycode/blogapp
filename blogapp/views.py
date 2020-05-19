from django.shortcuts import render
from blogapp.forms import blogform,signupform
from blogapp.models import blog
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail

def welcome(request):
    return render(request,'mfolder/welcome.html');

@login_required
def viewblogs(request):
    list1=blog.objects.all().order_by('-blogger_date')
    mdict1={'list1':list1}
    return render(request,'mfolder/viewblogs.html',context=mdict1);

@login_required
def createblog(request):
     list2=blogform();
     mdict2={'list2':list2}
     if request.method == 'POST':
         list2=blogform(request.POST,request.FILES);
         if list2.is_valid():
             data=list2.save()
             data.author=request.user
             data.save()
             mdict2.update({'msg': 'New blog registerd successfully'})
     return render(request,'mfolder/createblog.html',context=mdict2);


def signuppage(request):
    list3=signupform();
    mdict3={'list3':list3}
    if request.method == 'POST':
        list3=signupform(request.POST);
        if list3.is_valid():
            user=list3.save();
            user.set_password(user.password)
            user.save()
            subject='welcome new user!'
            message='welcome '+user.first_name+', to the mindblogger.Now you can explore more!.THANK YOU FOR REGISTERING HERE'
            recipient_list=[user.email]
            email_from=settings.EMAIL_HOST_USER
            send_mail(subject,message,email_from,recipient_list)
            mdict3.update({'msg': 'your access is registerd successfully'})
    return render(request,'mfolder/signup.html',context=mdict3);



@login_required
def detailfile(request,bloger_about):
    list4=blog.objects.get(bloger_about=bloger_about)
    mdic={'list4':list4}
    return render(request,'mfolder/detailfile.html',context=mdic);


def dltblock(request,bloger_about):
    list4=blog.objects.filter(bloger_about=bloger_about)
    list4.delete();
    list4=blog.objects.all().order_by('-blogger_date')
    return render(request,'mfolder/createblog.html',{'list4':list4,'msg':'blog deleted successfully!'});
