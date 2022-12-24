from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from .forms import UserRegistrationform,UserEditForm
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm
from django.contrib.auth import login,authenticate,update_session_auth_hash, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# from django.views.generic import CreateView

# class based view for user registration
def signUPView(request):
    if request.method=="POST":
        form=UserRegistrationform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/auth/register")
    else:
        form=UserRegistrationform()
    return render(request,'poll/signup.html',{'form':form})

#this view function is for login the register user
def user_Login(request):
    if request.method=="POST":
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            pwd1=form.cleaned_data['password']
            user_data=authenticate(username=uname, password=pwd1)
            if user_data is not None:
                login(request, user_data)
                return HttpResponseRedirect("/auth/profile/")
    else:
        form=AuthenticationForm()
    return render(request,'poll/loginform.html',{'form':form})

def logout_view(request):
    logout(request=request)
    return redirect("/login-view/")

# user profile view
@login_required
def user_profile(request):
    if request.user.is_superuser:
        users=User.objects.order_by('id')
        paginator = Paginator(users,5) # Show 5 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    elif request.user.is_authenticated:
        # return HttpResponse("Welcome To dashboard!!")
        return HttpResponse("""
        <html>
            <center><h2>Welcome To dashboard!!</h2></center>    
            <a href="/auth/login">Logout</a>
        </html>
        """)
    else:
        return HttpResponse('create profile please first!!!')
    return render(request,'poll/profile.html',{'users':page_obj,"username":request.user})

#view for deleting a user
def delete_user_view(request, pk):
    if request.user.is_superuser:
        try:
            new_user=User.objects.get(id=pk)
            new_user.delete()
        except User.DoesNotExist as err:
            return HttpResponse("""
                    <html> 
                        <h2>User does not exist!!</h2> 
                        <a href="/auth/profile/">Go To Admin</a>
                    </html>
                    """)
        return HttpResponse("User Deleted!!")
        

#User Edit view
def usereditview(request,pk):
    object=User.objects.get(id=pk)
    if request.user.is_superuser:
        if request.method=="POST":
            form=UserEditForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/auth/profile/")
        else:
            form=UserEditForm(instance=object)
        return render(request,"poll/editprofile.html",{'form':form})
    else:
        return HttpResponseRedirect("/auth/login")