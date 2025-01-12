
from django.shortcuts import render,redirect
from .forms import get_user_model, UserRegistrationForm,UserLoginForm ,UserUpdateForm,CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

#from .decorators import user_not_authenticated

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

User = get_user_model()
# Create your views here.

def profile(request, username):
    user = get_user_model().objects.filter(username=username).first()
    
    if user:
        if request.method == 'POST':
            form = UserUpdateForm(request.POST, instance=user)
            
            if form.is_valid():
                form.save()  # Save the updated user profile
                
                # Show a success message
                messages.success(request, 'Your profile has been updated successfully!')
                
                # Redirect the user to the profile page or another page
                return redirect("home")  # Redirect to the same profile page
        
        # If it's a GET request, show the form pre-filled with the current user's data
        form = UserUpdateForm(instance=user)
        return render(request, 'profile.html', context={'form': form})
    
    # Redirect to the homepage if no user found
    return redirect("home")
    

def register(request):
    if request.method == "POST":
        form =  UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=True
            user.save()
            return redirect('home')
        else:
            for key, error_list in form.errors.items():
                for error in error_list:
                    if key == 'Captcha':
                        messages.error(request, "You must pass the <b>CAPTCHA</b> test.")
                    else:
                        messages.error(request, error)

    else:
        form = UserRegistrationForm()
    return render(request=request,template_name='register.html',context={"form": form}
)
def Login(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            if User.objects.filter(username=username).exists():
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                    return redirect("home")
                else:
                    messages.error(request, "Invalid password. Please try again.")
            else:
                messages.error(request, "Username not found. Please make sure you have registered.")
        else:
            for key, error_list in form.errors.items():
                for error in error_list:
                    if key == 'Captcha':
                        messages.error(request, "You must pass the <b>CAPTCHA</b> test.")
                    else:
                        messages.error(request, error)
                
                

    form = UserLoginForm()

    return render(
        request=request,
        template_name="login.html",
        context={"form": form}
        )
def Logout(request):
    logout(request)
    messages.info(request,"Logged out is successfully")
    return redirect("home")




@login_required
def PasswordConfirm(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password was successfully updated!")
            return redirect('home')
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'password_reset_confirm.html', {'form': form})
