from customuser.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CustomUserCreationForm, ExpertForm, EducationForm, ExperienceForm, SkillForm, CreateMessage
from .utils import search_experts, pagination_experts
from posts.models import BlogPost


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
    experts, search_query = search_experts(request)
    experts, custom_range = pagination_experts(request, experts, 4)
    context = {'experts': experts, 'search_query': search_query, 'custom_range':custom_range}
    return render(request, 'experts/expert_list.html', context)


@login_required(login_url='user-login')
def expert_details(request, pk):
    expert = Experts.objects.get(id=pk)
    educations = expert.educations.all()
    experiences = expert.experiences.all()
    context = {'expert': expert, 'educations': educations, 'experiences': experiences}
    return render(request, 'profile.html', context)


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


@login_required(login_url='login')
def add_education(request):
    expert = request.user.experts
    education = expert.educations.all()
    form_type = 'Education'
    form = EducationForm()
    if request.method == 'POST':
        form = EducationForm(request.POST, request.FILES)
        if form.is_valid():
            education = form.save(commit=False)
            education.experts = expert
            education.save()
            messages.success(request, 'Created Successfully !!!')
            return redirect('account')
    context = {'form': form, 'form_type': form_type, 'education': education}
    return render(request, 'experts/adding_detail_forms.html', context)


@login_required(login_url='login')
def edit_education(request, pk):
    expert = request.user.experts
    queryset = expert.educations.get(id=pk)
    form_type = 'Education'
    form = EducationForm(instance=queryset)
    if request.method == 'POST':
        form = EducationForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully !!!')
            return redirect('account')
    context = {'form': form, 'form_type': form_type}
    return render(request, 'experts/adding_detail_forms.html', context)


@login_required(login_url='login')
def delete_education(request, pk):
    form_type = 'Education'
    expert = request.user.experts
    queryset = expert.educations.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Deleted Successfully !!!')
        return redirect('account')
    return render(request, 'confirm_delete.html', context={'queryset': queryset, 'form_type': form_type})


# End of Education Functionality


# # CRUD Functionality of Experience in function based Views

@login_required(login_url='login')
def add_experience(request):
    expert = request.user.experts
    form_type = 'Experience'
    form = ExperienceForm()
    if request.method == 'POST':
        form = ExperienceForm(request.POST, request.FILES)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.experts = expert
            experience.save()
            messages.success(request, 'Created Successfully !!!')
            return redirect('account')
    context = {'form': form, 'form_type': form_type, 'expert': expert}
    return render(request, 'experts/adding_detail_forms.html', context)


@login_required(login_url='login')
def edit_experience(request, pk):
    form_type = 'Experience'
    queryset = get_object_or_404(Experiences, id=pk)
    form = ExperienceForm(instance=queryset)
    if request.method == 'POST':
        form = ExperienceForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully !!!')
            return redirect('account')
    context = {'form': form, 'form_type': form_type}
    return render(request, 'experts/adding_detail_forms.html', context)


@login_required(login_url='login')
def delete_experience(request, pk):
    queryset = get_object_or_404(Experiences, id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Deleted Successfully !!!')
        return redirect('account')
    return render(request, 'confirm_delete.html', context={'queryset': queryset})


# # End of Experience Functionality

# # skill section with function based view

@login_required(login_url='login')
def add_skill(request):
    form_type = 'Skill'
    expert = request.user.experts
    skills = expert.skills.all()
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.experts = expert
            skill.save()
            messages.success(request, 'Created Successfully !!!')
            return redirect('account')
    context = {'form': form, 'form_type': form_type}
    return render(request, 'experts/adding_detail_forms.html', context)


@login_required(login_url='login')
def edit_skill(request, pk):
    form_type = 'Skill'
    queryset = get_object_or_404(Skills, id=pk)
    form = SkillForm(instance=queryset)
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully !!!')
            return redirect('account')
    context = {'form': form, 'form_type': form_type}
    return render(request, 'experts/adding_detail_forms.html', context)


@login_required(login_url='login')
def delete_skill(request, pk):
    queryset = get_object_or_404(Skills, id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Deleted Successfully !!!')
        return redirect('account')
    return render(request, 'confirm_delete.html', context={'queryset': queryset})

# #  end of skills functionality

@login_required(login_url='login')
def account(request):
    expert = request.user.experts
    educations = expert.educations.all()
    experiences = expert.experiences.all()
    skills = expert.skills.all()
    blog_posts = BlogPost.objects.filter(author=request.user)
    context = {'expert': expert, 'educations': educations, 'experiences': experiences,
               'skills': skills, 'blog_posts':blog_posts}
    return render(request, 'account.html', context)

# messages


@login_required(login_url='login')
def inbox(request):
    expert = request.user.experts
    message_inbox = expert.messages.all()
    unReadCount = message_inbox.filter(is_read=False).count()
    context = {'message_inbox':message_inbox, 'unreadCount':unReadCount}
    return render(request, 'experts/inbox.html', context)


@login_required(login_url='login')
def view_message(request, pk):
    expert = request.user.experts
    view_msg = expert.messages.get(id=pk)
    if not view_msg.is_read:
        view_msg.is_read = True
        view_msg.save()
    context = {'message': view_msg}
    return render(request, 'experts/message.html', context)


def create_message(request, pk):
    recipient = Experts.objects.get(id=pk)
    form = CreateMessage()
    try:
        sender = request.user.experts
    except:
        sender = None

    if request.method == 'POST':
        form = CreateMessage(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.full_name
                message.email = sender.email
            message.save()
            messages.success(request, 'Message sent successfully !!')
            return redirect('expert-details', pk=recipient.id)

    context = {'recipient': recipient, 'form':form}
    return render(request, 'experts/create_message.html', context)