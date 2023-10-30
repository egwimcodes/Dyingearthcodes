from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, SensorListForm, UpdateUserForm, UpdateTodoForm
from .models import User, Sensor, TodoApp, SensorQr
from datetime import datetime
from django.utils import timezone
import uuid
from django.db import IntegrityError


# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("main")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful")
                return redirect("main")
            else:
                messages.error(request, "Invalid email or password")
    return render(request, "dashboard/authentication-signin-with-header-footer.html")


def logoutPage(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect("login-page")


def registerPage(request):
    if request.user.is_authenticated:
        return redirect("main")
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Account created successfully")
                return redirect("login-page")

    context = {"form": form}
    return render(request, "dashboard/authentication-signup-with-header-footer.html", context)


@login_required(login_url="login-page")
def userProfile(request, pk):
    user = get_object_or_404(User, username=request.user.username)
    sensor_list = user.sensor_set.all().order_by("-id")

    # checking if the request is post
    if request.method == 'POST':
        # for updating user profile
        updateform = UpdateUserForm(request.POST, request.FILES, instance=user)
        if updateform.is_valid():
            updateform.save()
            return redirect(reverse('user-profile', kwargs={'pk': user.username}))

        # for updating sensor list
        form = SensorListForm(request.POST)
        if form.is_valid():
            id = request.POST.get('id')
            print(id)
            sensor_id = request.POST.get("sensor_id")
            sensor = get_object_or_404(Sensor, id=sensor_id, user=user)
            form = SensorListForm(request.POST, instance=sensor)
            if form.is_valid():
                form.save()
                return redirect(reverse('user-profile', kwargs={'pk': user.username}))
    else:
        form = SensorListForm()

    # context for rendering the page
    context = {
        "sensor_list": sensor_list,
        "user": user,
        "form": form,
    }
    return render(request, "dashboard/user-profile.html", context)


@login_required(login_url="login-page")
def settingsPage(request):
    user = get_object_or_404(User, username=request.user.username)
    sensor_list = user.sensor_set.all().order_by("-id")

    # this block generates qr code and check for duplicate in the database when the qrcode is exhausted
    def sensor_code_generator(unregistered_sensors):
        for i in range(unregistered_sensors):
            uuid_code = uuid.uuid4()
            main_uuid = str(uuid_code).upper().replace('-', '')[:20]
            formatted = "DE-" + '-'.join([main_uuid[i:i + 5] for i in range(0, len(main_uuid), 5)])
            try:
                # Try creating the new sensor entry
                SensorQr.objects.create(sensor_qr=formatted)
            except IntegrityError:
                # If there's a duplicate (IntegrityError), delete one of them and then create the new entry
                duplicate_sensor = SensorQr.objects.filter(sensor_qr=formatted).first()
                if duplicate_sensor:
                    duplicate_sensor.delete()
                SensorQr.objects.create(sensor_qr=formatted)

    if not SensorQr.objects.all():
        for qr in SensorQr.objects.all().values():
            if qr['sensor_id'] == None:
                pass
        sensor_code_generator(100)

    try:
        form = SensorListForm(request.POST)
        if form.is_valid():
            id = request.POST.get('id')
            sensor_id = request.POST.get("sensor_id")
            sensor = get_object_or_404(Sensor, id=sensor_id, user=user)
            form = SensorListForm(request.POST, instance=sensor)
            if form.is_valid():
                form.save()
    except:
        if request.method == 'POST':
            if request.POST.get("add-sensor"):
                adding_sensor = request.POST.get("add-sensor")
                matching_token = None

                for token in SensorQr.objects.all().values():
                    if token['sensor_qr'] == adding_sensor and token['sensor_id'] == None:
                        matching_token = token
                        matching_token_id = token['id']
                        break

                if matching_token:
                    adding_to_db = str(matching_token)
                    if adding_to_db:
                        auto_sensor = Sensor(name=f"New Sensor {matching_token_id}", user=user, location="No Location Added")
                        auto_sensor.save()
                        sensor_qr = SensorQr.objects.get(id=matching_token_id)
                        sensor_qr.sensor = auto_sensor
                        sensor_qr.save()
                        messages.success(request, "Sensor added successfully, Please rename as soon as possible")
                        return redirect(reverse('profile-settings'))
                else:
                    messages.error(request, "Invalid QR Code or Code Already Used, please type carefully Thank you.")
                    return redirect(reverse('profile-settings'))
        else:
            pass



    else:
        form = SensorListForm()

    context = {
        "sensor_list": sensor_list,
        "user": user,
        "form": form,
    }
    return render(request, "dashboard/settings.html", context)


@login_required(login_url="login-page")
def mainPage(request):
    return render(request, "dashboard/main.html")


@login_required(login_url="login-page")
def appCalendar(request):
    return render(request, "dashboard/app-fullcalendar.html")


@login_required(login_url="login-page")
def appTodo(request):
    user = get_object_or_404(User, username=request.user.username)
    todos = user.todo_set.order_by("-id")

    del_id = request.POST.get("delete-todo")

    todo_add_text = request.POST.get("todo-text-add")
    todo_add_time = request.POST.get("todo-time-add")
    choose_form = todo_add_text if todo_add_text else False
    if request.method == "POST" and choose_form:
        try:
            todo_time = todo_add_time if todo_add_time else timezone.now()
            todo = TodoApp.objects.create(text=todo_add_text, user=user, time=todo_time)
            todo.save()
            messages.success(request, "Todo added successfully")
            return redirect(reverse('app-todo'))
        except not todo_add_text:
            messages.error(request, "Please enter a valid Todo")

    elif request.method == "POST" and not todo_add_text and not del_id:
        try:
            form = UpdateTodoForm(request.POST)
            if form.is_valid():
                todo_id = request.POST.get("todo-id-update")
                todo = get_object_or_404(TodoApp, id=todo_id, user=user)
                done = request.POST.get("done") == "on"
                form = UpdateTodoForm(request.POST, instance=todo)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Todo updated successfully")
        except:
            messages.error(request, "Please enter valid data for updating the todo")


    elif request.method == "POST" and del_id:
        try:
            todo = get_object_or_404(TodoApp, id=del_id, user=user)
            todo.delete()
            messages.success(request, "Todo deleted successfully")
            return redirect(reverse('app-todo'))
        except:
            messages.error(request, "Please enter valid data for deleting the todo")

    context = {
        "todos": todos,
        "todo_update_form": UpdateTodoForm()  # Instantiate the update form
    }
    return render(request, "dashboard/app-to-do.html", context)
    # for updating todos


@login_required(login_url="login-page")
def dashboardPage(request):
    return render(request, "dashboard/user-profile.html")
