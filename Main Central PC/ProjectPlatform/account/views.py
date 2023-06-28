from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import Account
from twinregister.models import VerticleMilling
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            is_manufacturer = form.cleaned_data['is_manufacturer']
            is_serviceprovider = form.cleaned_data['is_serviceprovider']
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.is_manufacturer = is_manufacturer
            user.is_serviceprovider = is_serviceprovider
            user.save()
            messages.success(request, "Registration successful")
            return redirect('register')

           
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'account/register.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)


        if user is not None:
            auth.login(request, user)
            if user.is_manufacturer is True:
                return redirect('maininterface')
            elif user.is_serviceprovider is True:
                return redirect('serviceproviderinterface')
            else:
                return redirect('home')

        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')

    return render(request, 'account/login.html')

@login_required(login_url = 'login')
def logout(request):
    ## to set is_connected false for all models at the time of logout
    ## for vertilcle milling model
    registered_models = VerticleMilling.objects.filter(user=request.user)
    registered_models_connected = registered_models.filter(is_connected=True).all().update(is_connected=False)


    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')