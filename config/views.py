from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class SignupView(CreateView):
	form_class = UserCreationForm 
	success_url = reverse_lazy('landing')
	template_name= 'auth/signup.html'