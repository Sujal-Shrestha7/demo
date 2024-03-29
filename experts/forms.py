from .models import Experts, Educations, Experiences, Skills, Message
from django.forms import ModelForm, widgets
from django import forms
from django.contrib.auth.forms import UserCreationForm
from customuser.models import User


class ExpertForm(ModelForm):
    class Meta:
        model = Experts
        fields = ['full_name', 'email', 'profile_photo', 'short_intro', 'position', 'location', 'categories',
                  'github_link', 'linkedin_link', 'website_link', 'twitter_link']

        widgets = {
            'categories': forms.RadioSelect(),
        }


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password', 'class': 'form-control'}),
        strip=False,
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'class': 'form-control'}),
        strip=False,
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        # labels = {
        #     'email': 'Email',
        #     'username': 'Username',
        #     'password1': 'Password',
        #     'password2': 'Confirm Password'
        #
        # }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'name': 'email', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password1',
                                                    'placeholder': 'Password'}, render_value=True),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password2',
                                                    'placeholder': 'Confirm Password'}, render_value=True),
        }

    # def __init__(self, *args, **kwargs):
    #     super(CustomUserCreationForm, self).__init__(*args, **kwargs)
    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'input'})


class EducationForm(ModelForm):
    class Meta:
        model = Educations
        fields = ['degree', 'title', 'university_name', 'institute_name', 'location']
        widgets = {
            'degree': forms.Select(choices=Educations.DEGREE_OPTIONS),
        }

        def __init__(self, *args, **kwargs):
            super(EducationForm, self).__init__(*args, **kwargs)
            for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input'})


class ExperienceForm(ModelForm):
    class Meta:
        model = Experiences
        fields = ['title', 'organization', 'position', 'duration', 'is_working']
        widgets = {
            'position': forms.Select(choices=Experiences.POSITION_CHOICES),
        }

        def __init__(self, *args, **kwargs):
            super(ExperienceForm, self).__init__(*args, **kwargs)
            for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input'})


class SkillForm(ModelForm):
    class Meta:
        model = Skills
        fields = ['title', 'description']

        def __init__(self, *args, **kwargs):
            super(SkillForm, self).__init__(*args, **kwargs)
            for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input'})


class CreateMessage(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']

    def __init__(self, *args, **kwargs):
        super(CreateMessage, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})