from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, LoginForm, UserCarForm, HistoryForm
from .models import MarkModel, Mark, UserCar, History
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# home
def home_page(request):
    return render(request, "./home.html")

# cars
@login_required
def user_cars_page(request):
    user_cars = UserCar.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'user_cars': user_cars
    }
    return render(request, "./user_cars.html", context)

# add car
@login_required
def add_user_car(request):
    if request.method == 'POST':
        form = UserCarForm(request.POST, request.FILES, request=request)
        if form.is_valid():
            form.save()
            return redirect('user_cars_page')
    else:
        form = UserCarForm(request=request)
    return render(request, './add_user_car.html', {'form': form})
# edit car
@login_required
def edit_user_car(request, pk):
    user_car = get_object_or_404(UserCar, pk=pk, user=request.user)
    if request.method == 'POST':
        form = UserCarForm(request.POST, request.FILES, instance=user_car)
        if form.is_valid():
            form.save()
            return redirect('user_cars_page')
    else:
        form = UserCarForm(instance=user_car)
    return render(request, './edit_user_car.html', {'form': form})
# delete car
@login_required
def delete_user_car(request, pk):
    user_car = get_object_or_404(UserCar, pk=pk, user=request.user)
    user_car.delete()
    return redirect('user_cars_page')



def car_histories_page(request, pk):
    car = get_object_or_404(UserCar, pk=pk)
    histories = History.objects.filter(car=car).order_by('-created_at')
    return render(request, "./histories.html", {'car': car, 'histories': histories})

def add_history_page(request, pk):
    car = get_object_or_404(UserCar, pk=pk)
    if request.method == 'POST':
        form = HistoryForm(request.POST, request.FILES, request=request)
        if form.is_valid():
            history = form.save(commit=False)
            history.car = car
            history.user = request.user
            history.save()
            return redirect('car_histories_page', pk=car.pk)
    else:
        form = HistoryForm(request=request)
    return render(request, "./add_history.html", {'form': form, 'car': car})

def edit_history_page(request, pk):
    history = get_object_or_404(History, pk=pk)
    if request.method == 'POST':
        form = HistoryForm(request.POST, request.FILES, instance=history, request=request)
        if form.is_valid():
            form.save()
            return redirect('car_histories_page', pk=history.car.pk)
    else:
        form = HistoryForm(instance=history, request=request)
    return render(request, "./edit_history.html", {'form': form, 'history': history})

def delete_history_page(request, pk):
    history = get_object_or_404(History, pk=pk)
    car_id = history.car.id
    history.delete()
    return redirect('car_histories_page', pk=history.car.pk)

# sign up
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login_view')
    else:
        form = SignUpForm()
    return render(request, './register.html', {
        'form': form
    })

# login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_page')
    else:
        form = LoginForm()
    return render(request, './login.html', {
        'form': form
    })

# exit
def logout_view(request):
    logout(request)
    return redirect('home_page')