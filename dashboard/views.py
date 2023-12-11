from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, DeleteAccountForm, CustomPasswordChangeForm, SensorListForm, UpdateUserForm, UpdateTodoForm, RegisterSensorForm
from .models import User, Sensor, SoldSensorQr, UnSoldSensorQr, Payloads, TodoApp
from datetime import datetime
from django.utils import timezone
import uuid
from django.db import IntegrityError
from django.contrib.auth.views import PasswordChangeView


# cbv
from django.views.generic import CreateView, FormView, TemplateView, DeleteView, UpdateView, View, DetailView, ListView
from django.contrib.auth import get_user_model
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


class RegisterNewSensorView(LoginRequiredMixin, DetailView, FormView):
    template_name = "dashboard/register_new_sensor.html"
    form_class = RegisterSensorForm
    second_form_class = SensorListForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(RegisterNewSensorView, self).get_context_data(**kwargs)
        if 'rform' not in context:
            context['rform'] = self.get_form(self.form_class)
        if 'uform' not in context:
            context['uform'] = self.get_form(self.second_form_class)
            context['sensor_list'] = self.object.sensor_set.all().order_by("-id")
        return context

    def get_success_url(self):
        return reverse('register_new_sensor', kwargs={'pk': self.request.user.id})

    def form_invalid(self, **kwargs):
        return self.render_to_response(self.get_context_data(**kwargs))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        rform = self.get_form(self.form_class)
        uform = self.get_form(self.second_form_class)
        if 'rform' in request.POST and rform.is_valid():
            return self.form_valid(rform, 'rform')
        elif 'uform' in request.POST and uform.is_valid():
            return self.form_valid(uform, 'uform')
        else:
            return self.form_invalid(rform=rform, uform=uform)

    def form_valid(self, form, form_name):
        user = self.request.user
        # Manipulate the form data before saving
        # Check which form is valid and perform specific logic
        if form_name == 'rform':
            # Logic for rform
            # Get the form data
            new_sensor_name = form.cleaned_data['new_sensor_name']
            sensor_location = form.cleaned_data['sensor_location']
            sensor_qr = form.cleaned_data['sensor_qr']

            if SoldSensorQr.objects.filter(sold_sensor_qr_code=sensor_qr).exists():
                messages.error(
                    self.request, 'Sorry this sensor is own by another customer')

            else:
                if UnSoldSensorQr.objects.filter(unsold_sensor_qr_code=sensor_qr).exists() and len(sensor_qr) == 22:
                    sensor = Sensor.objects.create(
                        name=new_sensor_name,
                        location=sensor_location,
                        user=user
                    )
                    payload = Payloads.objects.create(
                        sensor=sensor,
                    )
                    register_qr_new_code = SoldSensorQr.objects.create(
                        sensor=sensor,
                        sold_sensor_qr_code=sensor_qr
                    )
                    sensor.save()
                    payload.save()
                    register_qr_new_code.save()

                    UnSoldSensorQr.objects.filter(
                        unsold_sensor_qr_code=sensor_qr).first().delete()

                    messages.success(
                        self.request, "Sensor Registered successfully")
                else:
                    messages.error(
                        self.request, 'Sorry Invalid sensor, Please check carefully and try again.')
            # Create a new Sensor object

            # Redirect to the success URL
            return redirect(reverse('register_new_sensor', kwargs={'pk': user.id}))

        elif form_name == 'uform':
            # Logic for uform
            # Update sensor list
            sensor_id = self.request.POST.get("sensor_id")
            sensor = get_object_or_404(Sensor, id=sensor_id, user=user)
            form = SensorListForm(self.request.POST, instance=sensor)
            if form.is_valid():
                form.save()
                return redirect(reverse('register_new_sensor', kwargs={'pk': user.id}))
        return super(RegisterNewSensorView, self).form_valid(form)


# def sensorAddView(request):

#     user = get_object_or_404(User, username=request.user.username)
#     sensor_list = user.sensor_set.all().order_by("-id")

#     # this block generates qr code and check for duplicate in the database when the qrcode is exhausted
#     def sensor_code_generator(unregistered_sensors):
#         for i in range(unregistered_sensors):
#             uuid_code = uuid.uuid4()
#             main_uuid = str(uuid_code).upper().replace('-', '')[:20]
#             formatted = "DE-" + \
#                 '-'.join([main_uuid[i:i + 5]
#                          for i in range(0, len(main_uuid), 5)])
#             try:
#                 # Try creating the new sensor entry
#                 SensorQr.objects.create(sensor_qr=formatted)
#             except IntegrityError:
#                 # If there's a duplicate (IntegrityError), delete one of them and then create the new entry
#                 duplicate_sensor = SensorQr.objects.filter(
#                     sensor_qr=formatted).first()
#                 if duplicate_sensor:
#                     duplicate_sensor.delete()
#                 SensorQr.objects.create(sensor_qr=formatted)

#     if not SensorQr.objects.all():
#         for qr in SensorQr.objects.all().values():
#             if qr['sensor_id'] == None:
#                 pass
#         sensor_code_generator(100)

#     try:
#         form = SensorListForm(request.POST)
#         if form.is_valid():
#             id = request.POST.get('id')
#             sensor_id = request.POST.get("sensor_id")
#             sensor = get_object_or_404(Sensor, id=sensor_id, user=user)
#             form = SensorListForm(request.POST, instance=sensor)
#             if form.is_valid():
#                 form.save()
#     except:
#         if request.method == 'POST':
#             if request.POST.get("register_new_sensor"):
#                 adding_sensor = request.POST.get("register_new_sensor")
#                 matching_token = None

#                 for token in SensorQr.objects.all().values():
#                     if token['sensor_qr'] == adding_sensor and token['sensor_id'] == None:
#                         matching_token = token
#                         matching_token_id = token['id']
#                         break

#                 if matching_token:
#                     adding_to_db = str(matching_token)
#                     if adding_to_db:
#                         auto_sensor = Sensor(
#                             name=f"New Sensor {matching_token_id}", user=user, location="No Location Added")
#                         auto_sensor.save()
#                         sensor_qr = SensorQr.objects.get(id=matching_token_id)
#                         sensor_qr.sensor = auto_sensor
#                         sensor_qr.save()
#                         messages.success(
#                             request, "Sensor added successfully, Please rename as soon as possible")
#                         return redirect(reverse('settings'))
#                 else:
#                     messages.error(
#                         request, "Invalid QR Code or Code Already Used, please type carefully Thank you.")
#                     return redirect(reverse('settings'))
#         else:
#             pass

#     else:
#         form = SensorListForm()

#     context = {
#         "sensor_list": sensor_list,
#         "user": user,
#         "form": form,
#     }
#     return render(request, "dashboard/register_new_sensor.html", context)


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
