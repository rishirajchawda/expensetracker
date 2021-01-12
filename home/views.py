from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def Login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')

        else:
            messages.info(request,'Username OR password is incorrect')
            

    context={}
    return render (request,'login.html',context)


def Register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)

            return redirect('login')

    context = {'form':form}
    return render(request,'register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def home(request):
    profile = Profile.objects.filter(user = request.user).first()
    print(profile)
    expenses = Expense.objects.filter(user = request.user)
    if request.method=='POST':
        text=request.POST.get('text')
        amount=request.POST.get('amount')
        expense_type=request.POST.get('expense_type')

        expense=Expense(name=text ,amount=amount ,expense_type=expense_type ,user=request.user)
        expense.save()

        if expense_type == 'Credit':
            profile.user_balance += float(amount)
        else:
            profile.expenses += float(amount)
            profile.user_balance -= float(amount)

        profile.save()
        return redirect('home')



    context = {'profile':profile , 'expenses':expenses}
    return render (request,'index.html',context)
    
