from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import login, authenticate, logout # type: ignore
from .forms import SignupForm, LoginForm
from .models import CustomUser

# Create your views here.
def signup_view(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'signup.html', {'form':form})

def login_view(request):
    form = LoginForm(request.POST or None) # Initialize with POST data if available

    if request.method == 'POST':
        print(request.POST) # ! For debugging purposes
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                # user = CustomUser.objects.get(email=email) # Find user by email
                user = authenticate(request, username=email, password=password) # Authenticate with username

                if user:
                    login(request, user)
                    return redirect('home')
                else:
                    print('Authentication failed!') # ! For debugging purposes
                    form.add_error(None, 'Invalid Credentials! Try again.')
            except CustomUser.DoesNotExist:
                print("User with this email does not exist!") # ! For debugging purposes
                form.add_error(None, 'User with this email does not exist! Try signing up.')
        else:
            print("Form errors: ")
            for error in form.errors:
                print(error)
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'home.html')