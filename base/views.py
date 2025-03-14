from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm, PostForm, CategoryForm
from .models import CustomUser, Post, Category, Tag

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

@login_required(login_url='login')
def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'posts': posts,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'home.html', context)


def createPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) # Save the post without committing
            post.author = request.user # Set the author of the post
            post.save() # Save the post instance

            tags_list = form.cleaned_data.get('tags', [])
            for tag_name in tags_list:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                post.tags.add(tag)

            post.save()

            return redirect('home') # redirect to the home page on successful submission
        else:
            return redirect(request, 'create_post.html', {'form': form})
    else:
        form = PostForm()
        return render(request, 'create_post.html', {'form': form})

def addCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})