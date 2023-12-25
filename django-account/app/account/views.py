from django.contrib.auth import login, authenticate, logout, get_user_model, update_session_auth_hash
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, LoginForm, AccountUpdateForm, PasswordForm
from django.contrib.auth.decorators import login_required
from .models import Account
from django.contrib import messages

def signup(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request = request, template_name = "signup.html", context={"form":form})

@login_required
def logout_user(request):
	logout(request)
	return redirect("/")

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('/')
        else:
            messages.error(request,f"Invalid username or password.")
    else:
        form = LoginForm()
    return render(request=request, template_name="login.html", context={'form': form})

@login_required
def account(request, username):
    account = get_object_or_404(Account, username=username)
    return render(request, 'account.html', {'account': account})

@login_required
def account_edit(request):
    if request.method == 'POST':
        user = request.user
        form = AccountUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()
            return redirect('account', user_form.username)
        for error in list(form.errors.values()):
            messages.error(request, error)
    user = get_user_model().objects.filter(username=request.user).first()
    if user:
        form = AccountUpdateForm(instance=user)
        return render(request, 'account_edit.html', context={'form': form})
    return redirect("homepage")

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('change_password')
    else:
        form = PasswordForm(request.user)
    return render(request, 'change_password.html', {'form': form})