from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import Blog
from .forms import Blog_form,Registerationform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
# Create your views here.
def Blog_list(request):
    blogs=Blog.objects.all().order_by('-created_at')
    return render(request,'blog_list.html',{'blogs':blogs})

def Blog_page(request,blog_id):
    blog=get_object_or_404(Blog,id=blog_id)
    return render(request,'blog_page.html',{'blog':blog})

@login_required
def Blog_create(request):
    if request.method=='POST':
        form=Blog_form(request.POST,request.FILES)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.user=request.user
            blog.save()
            return redirect('blog_list')
    else:
        form=Blog_form()
    return render(request,'blog_form.html',{'form':form})

@login_required
def Blog_edit(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id,user=request.user)
    if request.method=='POST':
        form=Blog_form(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.user=request.user
            blog.save()
            return redirect('blog_list')
    else:
        form=Blog_form(instance=blog)
    return render(request,'blog_form.html',{'form':form})

@login_required
def Blog_delete(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id,user=request.user)
    if request.method=='POST':
        blog.delete()
        return redirect('blog_list')
    return render(request,'blog_delete.html',{'blog':blog})

# def Register(request):
#     if request.method ==' POST':
#         form = Registerationform(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password1'])
#             user.save()
#             login(request, user)
#             return redirect('blog_list')
#         else:
#             form = Registerationform()
#         return render(request, 'registration/register.html', {'form':form})
def Register(request):
    if request.method == 'POST':
        form = Registerationform(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()

            login(request, user)

            return redirect('blog_list')
    else:
        form = Registerationform()

    return render(request, 'registration/register.html', {'form': form})

def Profile(request,username):
    profile_user=get_object_or_404(User,username=username)
    profile_blog=Blog.objects.filter(user=profile_user).order_by('-created_at')
    context={
        'profile_user':profile_user,
        'profile_blog':profile_blog,
    }
    return render(request,'profile.html',context)
