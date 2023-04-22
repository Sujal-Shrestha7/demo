from django.shortcuts import render

from customuser.models import User
from .models import Experts, Categories
from .forms import ExpertForm

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# from .forms import ProfileForm, EducationForm, ExperienceForm, SkillForm, CourseForm
from .models import *
from .forms import CustomUserCreationForm


# Create your views here.
# Authentication and Authorization

def user_login(request):
    form_type = 'login'
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist !!!")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "User Logged in successfully !!!")
            return redirect(request.GET['next'] if 'next' in request.GET else "landing-page")

        else:
            messages.error(request, "Password Incorrect ")

        context = {'form_type': form_type}

        return render(request, 'forms.html', context)

    context = {'form_type': form_type}
    return render(request, 'forms.html', context)


def register_expert(request):
    form_type = "register expert"
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.info(request, "User has been registered !!! ")
            login(request, user)
            return redirect('landing-page')
        else:
            messages.error(request, "Something error occurred during user registration !!!")
    context = {'form_type': form_type, 'form': form}
    return render(request, 'forms.html', context)


def logout_user(request):
    logout(request)
    messages.success(request, "User logged out !!!")
    return redirect('landing-page')


# Landing page

def landing_page(request):
    queryset = Experts.objects.all()
    categories = Categories.objects.all()
    context = {'experts': queryset, 'categories': categories}
    return render(request, 'index.html', context)


@login_required(login_url='user-login')
def experts(request):
    queryset = Experts.objects.all()
    context = {'experts': queryset}
    return render(request, 'experts/expert_list.html', context)


@login_required(login_url='user-login')
def expert_details(request, pk):
    expert = Experts.objects.get(id=pk)
    context = {'expert': expert}
    return render(request, 'experts/expert_details.html', context)


def create_expert(request):
    form_type = "Expert"
    form = ExpertForm()
    if request.method == 'POST':
        form = ExpertForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Created Successfully !!!')
            return redirect(request.GET('next') if 'next' in request.GET else 'landing-page')

    context = {'form': form, 'form_type': form_type}
    return render(request, 'forms.html', context)


def edit_expert_profile(request, pk):
    form_type = 'Edit Expert'
    queryset = get_object_or_404(Experts, id=pk)
    form = ExpertForm(instance=queryset)
    if request.method == 'POST':
        form = ExpertForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
    context = {'form_type': form_type, 'form':form}
    return render(request, 'forms.html', context)




#
# @login_required(login_url='login')
# def delete_profile(request, pk):
#     queryset = get_object_or_404(Profile, id=pk)
#     if request.method == 'POST':
#         queryset.delete()
#         messages.success(request, 'Deleted Successfully !!!')
#         return redirect('profile-list')
#     return render(request, 'delete-project.html', context={'queryset': queryset})
#
# # End of Profile Functionality
#
#
# # CRUD Functionality of Education in function based views
#
# @login_required(login_url='login')
# def add_education(request):
#     profile = request.user.profile
#     education = profile.education.all()
#     form_type = 'Education'
#     form = EducationForm()
#     if request.method == 'POST':
#         form = EducationForm(request.POST, request.FILES)
#         if form.is_valid():
#             education = form.save(commit=False)
#             education.profile = profile
#             education.save()
#             messages.success(request, 'Created Successfully !!!')
#             return redirect('account')
#     context = {'form': form, 'form_type': form_type, 'education': education}
#     return render(request, 'profiles/create-form.html', context)
#
#
# @login_required(login_url='login')
# def edit_education(request, pk):
#     profile = request.user.profile
#     queryset = profile.education.get(id=pk)
#     form_type = 'Education'
#     form = EducationForm(instance=queryset)
#     if request.method == 'POST':
#         form = EducationForm(request.POST, request.FILES, instance=queryset)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Updated Successfully !!!')
#             return redirect('account')
#     context = {'form': form, 'form_type': form_type}
#     return render(request, 'profiles/create-form.html', context)
#
#
# @login_required(login_url='login')
# def delete_education(request, pk):
#     profile = request.user.profile
#     queryset = profile.education.get(id=pk)
#     if request.method == 'POST':
#         queryset.delete()
#         messages.success(request, 'Deleted Successfully !!!')
#         return redirect('account')
#     return render(request, 'delete-project.html', context={'queryset': queryset})
#
#
# # End of Education Functionality
#
#
# # CRUD Functionality of Experience in function based Views
#
# @login_required(login_url='login')
# def add_experience(request):
#     profile = request.user.profile
#     form_type = 'Experience'
#     form = ExperienceForm()
#     if request.method == 'POST':
#         form = ExperienceForm(request.POST, request.FILES)
#         if form.is_valid():
#             experience = form.save(commit=False)
#             experience.profile = profile
#             experience.save()
#             messages.success(request, 'Created Successfully !!!')
#             return redirect('account')
#     context = {'form': form, 'form_type': form_type, 'profile': profile}
#     return render(request, 'profiles/create-form.html', context)
#
#
# @login_required(login_url='login')
# def edit_experience(request, pk):
#     form_type = 'Experience'
#     queryset = get_object_or_404(Experience, id=pk)
#     form = ExperienceForm(instance=queryset)
#     if request.method == 'POST':
#         form = ExperienceForm(request.POST, request.FILES, instance=queryset)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Updated Successfully !!!')
#             return redirect('account')
#     context = {'form': form, 'form_type': form_type}
#     return render(request, 'profiles/create-form.html', context)
#
#
# @login_required(login_url='login')
# def delete_experience(request, pk):
#     queryset = get_object_or_404(Experience, id=pk)
#     if request.method == 'POST':
#         queryset.delete()
#         messages.success(request, 'Deleted Successfully !!!')
#         return redirect('account')
#     return render(request, 'delete-project.html', context={'queryset': queryset})
#
#
# # End of Experience Functionality
#
# # skill section with function based view
#
# @login_required(login_url='login')
# def add_skill(request):
#     form_type = 'Skill'
#     form = SkillForm()
#     if request.method == 'POST':
#         form = SkillForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Created Successfully !!!')
#             return redirect('account')
#     context = {'form': form, 'form_type': form_type}
#     return render(request, 'profiles/create-form.html', context)
#
#
# @login_required(login_url='login')
# def edit_skill(request, pk):
#     form_type = 'Skill'
#     queryset = get_object_or_404(Skills, id=pk)
#     form = SkillForm(instance=queryset)
#     if request.method == 'POST':
#         form = SkillForm(request.POST, request.FILES, instance=queryset)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Updated Successfully !!!')
#             return redirect('account')
#     context = {'form': form, 'form_type': form_type}
#     return render(request, 'profiles/create-form.html', context)
#
#
# @login_required(login_url='login')
# def delete_skill(request, pk):
#     queryset = get_object_or_404(Skills, id=pk)
#     if request.method == 'POST':
#         queryset.delete()
#         messages.success(request, 'Deleted Successfully !!!')
#         return redirect('account')
#     return render(request, 'delete-project.html', context={'queryset': queryset})
#
# #  end of skills functionality
#
# # CRUD operation of courses
#
#
# @login_required(login_url='login')
# def add_course(request):
#     form_type = 'Course'
#     form = CourseForm()
#     if request.method == 'POST':
#         form = CourseForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Created Successfully !!!')
#             return redirect('account')
#     context = {'form': form, 'form_type': form_type}
#     return render(request, 'profiles/create-form.html', context)
#
#
# @login_required(login_url='login')
# def edit_course(request, pk):
#     form_type = 'Course'
#     queryset = get_object_or_404(Courses, id=pk)
#     form = CourseForm(instance=queryset)
#     if request.method == 'POST':
#         form = CourseForm(request.POST, request.FILES, instance=queryset)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Updated Successfully !!!')
#             return redirect('account')
#     context = {'form': form, 'form_type': form_type}
#     return render(request, 'profiles/create-form.html', context)
#
#
# @login_required(login_url='login')
# def delete_course(request, pk):
#     queryset = get_object_or_404(Courses, id=pk)
#     if request.method == 'POST':
#         queryset.delete()
#         messages.success(request, 'Deleted Successfully')
#         return redirect('account')
#     return render(request, 'delete-project.html', context={'queryset': queryset})
#
#
# def login_page(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         try:
#             user = User.objects.get(username=username)
#
#         except:
#             messages.error(request, 'Username doesnt exist !!!')
#
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'Logged in successfully !!!')
#             return redirect('home')
#
#         else:
#             messages.error(request, 'Username or Password does not exist !!! ')
#
#     context = {}
#     return render(request, 'login.html', context)
#
#
# def logout_user(request):
#     logout(request)
#     messages.success(request, 'User Logged out Successfully !!!')
#     return redirect('home')
#
#
# def register_user(request):
#     form = UserCreationForm()
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
#             login(request, user)
#             messages.success(request, 'User registered successfully !!!')
#         return redirect('login')
#     context = {'form': form}
#     return render(request, 'register.html', context)
#
#
# @login_required(login_url='login')
# def account(request):
#     profile = request.user.profile
#     print(profile)
#     context = {'profile': profile}
#     return render(request, 'profiles/account.html', context)
