from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, LoginForm

class RegisterView(View):
  def get(self, request):
    form = UserRegisterForm()
    return render(request,'register.html',{'form':form})
  
  def post(self, request):
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Account created for {username}!')
      return redirect('login')
    else:
      form = UserRegisterForm()
      return render(request,'register.html',{'form':form})

class ProfileView(View):
  def get(self, request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
      'u_form':u_form,
      'p_form':p_form,
    }
    return render(request,'profile.html',context)
  def post(self, request):
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      messages.success(request, 'Your profile has been updated!')
      return redirect('profile')

def logout_view(request):
  logout(request)
  return redirect('login')


class LoginView(View):
  def get(self, request):
    form = LoginForm()
    return render(request, 'login.html',{'form':form})
  
  def post(self, request):
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      
      user = authenticate(username=username, password=password)
      if user:
        login(request, user)
        return redirect('home')
      else:
        form = LoginForm()
        return render(request,'login.html',{'form':form})