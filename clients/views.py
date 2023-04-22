from django.shortcuts import render
from experts.forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect


# Create your views here.


def register_client(request):
    form_type = "register client"
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


