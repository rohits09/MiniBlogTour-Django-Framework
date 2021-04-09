from django.shortcuts import render, HttpResponseRedirect
from .forms import CustomUserForm, CustomLoginForm, PostForm, AdminProfileForm, UserProfileForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Post
from django.contrib.auth.models import Group

# Create your views here.
def home(request):
    pst = Post.objects.all()
    return render(request, "blog/home.html", {"post": pst})

def about(request):
    return render(request, "blog/about.html")

def contact(request):
    return render(request, "blog/contact.html")

def user_signup(request):
    if request.method == "POST":
        spf = CustomUserForm(request.POST)
        if spf.is_valid():
            user = spf.save()
            group = Group.objects.get(name="Author")
            user.groups.add(group)
            # name = request.user.first_name
            messages.success(request, "Congratulations !!!. You are an Author")
            spf = CustomUserForm()
    else:
        spf = CustomUserForm()
    return render(request, "blog/signup.html", {"spform": spf})


def user_login(request):
    if request.user.is_authenticated != True:
        if request.method == "POST":
            lf = CustomLoginForm(request=request, data=request.POST)
            if lf.is_valid():
                uname = lf.cleaned_data["username"]
                upass = lf.cleaned_data["password"]
                user = authenticate(username=uname, password=upass)
                if user:
                    login(request, user)
                    fname = request.user
                    fn = fname.get_short_name()
                    messages.success(request, f"Welcome {fn}")
                    return HttpResponseRedirect("/profile/")
                else:
                    return HttpResponseRedirect("/signup/")
        else:
            lf = CustomLoginForm()
        return render(request, "blog/login.html", {"lfform": lf})
    else:
        return HttpResponseRedirect("/dashboard/")

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Successfully... Logout !!!")
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")

def profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                upf = AdminProfileForm(request.POST, instance=request.user)
            else:
                upf = UserProfileForm(request.POST, instance=request.user)
            if upf.is_valid():
                upf.save()
        else:
            if request.user.is_superuser == True:
                upf = AdminProfileForm(instance=request.user)
            else:
                upf = UserProfileForm(instance=request.user)
        return render(request, "blog/profile.html", {"form": upf, "name": request.user.first_name})
    else:
        return HttpResponseRedirect("/")

def dashboard1(request):
    if request.user.is_authenticated:
        post = Post.objects.all()
        usr = request.user
        name = usr.get_full_name()
        gps = usr.groups.all()
        return render(request, "blog/dashboard.html", {"fname":name, "groups":gps, "post":post})
    else:
        return HttpResponseRedirect("/login/")

def add_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            pf = PostForm(request.POST)
            if pf.is_valid():
                title = pf.cleaned_data["title"]
                descpt = pf.cleaned_data["descpt"]
                uname = request.user.get_username()
                pst = Post(uname=uname, title=title, descpt=descpt)
                pst.save()
                messages.success(request, "Successfully... Post Added !!!")
                pf = PostForm()
        else:
            pf = PostForm()
        return render(request, "blog/addpost.html", {"pform":pf})
    else:
        return HttpResponseRedirect("/login/")

def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pid = Post.objects.get(pk=id)
            uf = PostForm(request.POST, instance=pid)
            if uf.is_valid():
                uf.save()
                messages.success(request, "Successfully... Updated !!!")
                uf = PostForm()
        else:
            pid = Post.objects.get(pk=id)
            uf = PostForm(instance=pid)
        return render(request, "blog/updatepost.html", {"uform":uf})
    else:
        return HttpResponseRedirect("/login/")

def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pid = Post.objects.get(pk=id)
            pid.delete()
            messages.success(request, "Deleted !!!")
            return HttpResponseRedirect("/dashboard/")
    else:
        return HttpResponseRedirect("/login/")