from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, DeleteAccountForm, CustomPasswordChangeForm, SensorListForm, UpdateUserForm, UpdateTodoForm
from .models import User, Sensor, TodoApp, SensorQr
from datetime import datetime
from django.utils import timezone
import uuid
from django.db import IntegrityError
from django.contrib.auth.views import PasswordChangeView


# cbv
from django.views.generic import CreateView, FormView, TemplateView, DeleteView, UpdateView, View, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class UserCreationView(CreateView):
    template_name = "dashboard/registration/register.html"
    form_class = CreateUserForm
    success_url = reverse_lazy('login')


class SettingsView(LoginRequiredMixin, UpdateView):
    model = User  # Replace with your user model
    form_class = UpdateUserForm  # Replace with your user update form
    template_name = "dashboard/user_update_form.html"

    def get_object(self, queryset=None):
        # Retrieve the user based on the 'user_id' parameter from the URL
        return User.objects.get(id=self.kwargs['user_id'])

    def get_success_url(self):
        return reverse('settings', kwargs={'user_id': self.request.user.id})


class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm


class AccountDeleteView(DeleteView, LoginRequiredMixin):
    model = User
    template_name = "dashboard/registration/account_delete_done.html"
    success_url = reverse_lazy('logout')


# @method_decorator(login_required(login_url="login"), name="dispatch")
class UserSensorsView(LoginRequiredMixin, DetailView, FormView):
    template_name = 'dashboard/sensors_main.html'
    model = User
    context_object_name = 'user'
    form_class = SensorListForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sensor_list'] = self.object.sensor_set.all().order_by("-id")
        context['form'] = self.get_form()
        return context

    def form_valid(self, form):
        # Handle form submission logic here
        user = self.request.user

        # Update sensor list
        sensor_id = self.request.POST.get("sensor_id")
        sensor = get_object_or_404(Sensor, id=sensor_id, user=user)
        form = SensorListForm(self.request.POST, instance=sensor)
        if form.is_valid():
            form.save()
            return redirect(reverse('sensors', kwargs={'pk': user.username}))

        return super().form_valid(form)

    def form_invalid(self, form):
        # Handle invalid form submission logic here
        return self.render_to_response(self.get_context_data(form=form))


@login_required(login_url="login-page")
def settingsView(request):
    user = get_object_or_404(User, username=request.user.username)
    sensor_list = user.sensor_set.all().order_by("-id")

    # this block generates qr code and check for duplicate in the database when the qrcode is exhausted
    def sensor_code_generator(unregistered_sensors):
        for i in range(unregistered_sensors):
            uuid_code = uuid.uuid4()
            main_uuid = str(uuid_code).upper().replace('-', '')[:20]
            formatted = "DE-" + \
                '-'.join([main_uuid[i:i + 5]
                         for i in range(0, len(main_uuid), 5)])
            try:
                # Try creating the new sensor entry
                SensorQr.objects.create(sensor_qr=formatted)
            except IntegrityError:
                # If there's a duplicate (IntegrityError), delete one of them and then create the new entry
                duplicate_sensor = SensorQr.objects.filter(
                    sensor_qr=formatted).first()
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
                        auto_sensor = Sensor(
                            name=f"New Sensor {matching_token_id}", user=user, location="No Location Added")
                        auto_sensor.save()
                        sensor_qr = SensorQr.objects.get(id=matching_token_id)
                        sensor_qr.sensor = auto_sensor
                        sensor_qr.save()
                        messages.success(
                            request, "Sensor added successfully, Please rename as soon as possible")
                        return redirect(reverse('settings'))
                else:
                    messages.error(
                        request, "Invalid QR Code or Code Already Used, please type carefully Thank you.")
                    return redirect(reverse('settings'))
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


def sensorAddView(request):

    user = get_object_or_404(User, username=request.user.username)
    sensor_list = user.sensor_set.all().order_by("-id")

    # this block generates qr code and check for duplicate in the database when the qrcode is exhausted
    def sensor_code_generator(unregistered_sensors):
        for i in range(unregistered_sensors):
            uuid_code = uuid.uuid4()
            main_uuid = str(uuid_code).upper().replace('-', '')[:20]
            formatted = "DE-" + \
                '-'.join([main_uuid[i:i + 5]
                         for i in range(0, len(main_uuid), 5)])
            try:
                # Try creating the new sensor entry
                SensorQr.objects.create(sensor_qr=formatted)
            except IntegrityError:
                # If there's a duplicate (IntegrityError), delete one of them and then create the new entry
                duplicate_sensor = SensorQr.objects.filter(
                    sensor_qr=formatted).first()
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
                        auto_sensor = Sensor(
                            name=f"New Sensor {matching_token_id}", user=user, location="No Location Added")
                        auto_sensor.save()
                        sensor_qr = SensorQr.objects.get(id=matching_token_id)
                        sensor_qr.sensor = auto_sensor
                        sensor_qr.save()
                        messages.success(
                            request, "Sensor added successfully, Please rename as soon as possible")
                        return redirect(reverse('settings'))
                else:
                    messages.error(
                        request, "Invalid QR Code or Code Already Used, please type carefully Thank you.")
                    return redirect(reverse('settings'))
        else:
            pass

    else:
        form = SensorListForm()

    context = {
        "sensor_list": sensor_list,
        "user": user,
        "form": form,
    }
    return render(request, "dashboard/add-sensor.html", context)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/main.html"
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user  # Use self.request.user to get the current user
        context['sensor_list'] = user.sensor_set.all().order_by("-id")
        return context

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
            todo = TodoApp.objects.create(
                text=todo_add_text, user=user, time=todo_time)
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
            messages.error(
                request, "Please enter valid data for updating the todo")

    elif request.method == "POST" and del_id:
        try:
            todo = get_object_or_404(TodoApp, id=del_id, user=user)
            todo.delete()
            messages.success(request, "Todo deleted successfully")
            return redirect(reverse('app-todo'))
        except:
            messages.error(
                request, "Please enter valid data for deleting the todo")

    context = {
        "todos": todos,
        "todo_update_form": UpdateTodoForm()  # Instantiate the update form
    }
    return render(request, "dashboard/app-to-do.html", context)
    # for updating todos


@login_required(login_url="login-page")
def dashboardPage(request):
    return render(request, "dashboard/user-profile.html")
