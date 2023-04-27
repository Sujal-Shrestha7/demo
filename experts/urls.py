
from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name='landing-page'),
    path('login/', views.user_login, name='user-login'),
    path('register', views.register_expert, name='register-expert'),
    path('logout/', views.logout_user, name='user-logout'),

    path('create-expert/', views.create_expert, name='create-expert'),

    path('expert-list/', views.experts, name='expert-list'),
    path('expert-details/<str:pk>/', views.expert_details, name='expert-details'),
    path('edit-expert-profile/', views.edit_expert_profile, name='edit-expert-profile'),
    path('account/', views.account, name='account'),




    # path('login/', views.login_page, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('register/', views.register_user, name='register'),
    #
    # path('profile-list/', views.profiles, name='profile-list'),
    # path('profile-details/<str:pk>/', views.profile_details, name='profile-details'),
    #
    # # Profiles CRUD urls
    # path('create-profile/', views.create_profile, name='create-profile'),
    # path('edit-profile/<str:pk>/', views.edit_profile, name='edit-profile'),
    # path('delete-profile/<str:pk>/', views.delete_profile, name='delete-profile'),

    # Education CRUD urls
    path('add-education/', views.add_education, name='add-education'),
    path('edit-education/<str:pk>/', views.edit_education, name='edit-education'),
    path('delete-education/<str:pk>/', views.delete_education, name='delete-education'),

    # # Experience CRUD urls
    path('add-experience/', views.add_experience, name='add-experience'),
    path('edit-experience/<str:pk>/', views.edit_experience, name='edit-experience'),
    path('delete-experience/<str:pk>/', views.delete_experience, name='delete-experience'),

    # # Skills CRUD urls
    path('add-skill/', views.add_skill, name='add-skill'),
    path('edit-skill/<str:pk>/', views.edit_skill, name='edit-skill'),
    path('delete-skill/<str:pk>/', views.delete_skill, name='delete-skill'),

    # # Courses CRUD urls
    # path('add-course/', views.add_course, name='add-course'),
    # path('edit-course/<str:pk>/', views.edit_course, name='edit-course'),
    # path('delete-course/<str:pk>/', views.delete_course, name='delete-course'),
    #
    # path('account/', views.account, name='account'),

    # messages
    path('inbox/', views.inbox, name='inbox'),
    path('message/<str:pk>/', views.view_message, name='message'),
    path('create-message/<str:pk>/', views.create_message, name='create-message'),

]

