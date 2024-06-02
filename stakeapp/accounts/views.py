from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login,logout
from django.contrib import messages
from .forms import CustomUserCreationForm  # Replace with your actual form
from django.contrib.auth.views import LoginView

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.session['success_message'] = 'Account created successfully! You can now log in.'
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = {"ptitle": "Sign Up/Register"}
        return context


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        success_message = self.request.session.pop('success_message', None)
        if success_message:
            context["success_message"] = success_message
            # Ensure the message persists for the next request
            self.request.session['success_message'] = success_message
        else:
            context["success_message"] = None
        context["data"] = {"ptitle": "Sign In/Login"}
        return context

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return render(request, self.template_name, self.get_context_data())



def custom_logout(request):
    logout(request)
    # Redirect to your home page or any other desired URL after logout
    return redirect('/')