from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm, PostForm, CategoryForm, EditProfileForm
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

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile_view(request, username):
    user = get_object_or_404(CustomUser,  username=username)

    # Get blogs by this user
    blogs = Post.objects.filter(author=user)

    context = {
        'user': user,
        'blogs': blogs,
    }
    return render(request, 'profile_details.html', context)

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

@login_required(login_url='login')
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

            return redirect('post-details', post_id=post.id) # redirect to the home page on successful submission
        else:
            return render(request, 'create_post.html', {'form': form})
    else:
        form = PostForm()
        return render(request, 'create_post.html', {'form': form})

@login_required(login_url='login')
def editProfile(request):
    # user = request.user
    
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
        else:
            return render(request, 'edit_profile.html', {'form': form})
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

@login_required(login_url='login')
def addCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

def viewPost(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    blogs = Post.objects.filter(author=post.author)
    context = {
        'post': post,
        'blogs': blogs,
    }
    return render(request, 'post_details.html', context)