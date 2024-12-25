import os
import django
os.environ.setdefault('DJANGO_SETTING_MODULE','lesrning_users.setting')
django.setup()


from django.shortcuts import render
from django.contrib.auth.models import User
from basic_admin.models import UserProfileInfoForm,UserForm



def index(request):
    return render(request,'base.html')

def register(request):


    registered = False

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form  = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():


            user = user_form.save()
            user.set_password(user.password)
            user.save()


            profile = profile_form.save(commit = False)
            profile.user = user



            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]


            profile.save()

            register = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,"registration.html",{'user_form': user_form,
                                               "profile_form" : profile_form,
                                               "registered" : registered
                                               })

     
  

