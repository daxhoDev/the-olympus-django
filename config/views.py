from config.forms import LoginForm, ProfileCreationForm
from the_olympus.models import Profile
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

class SignupView(CreateView):
	model = Profile
	form_class = ProfileCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.html'
	

class CustomLoginView(LoginView):
	template_name = 'registration/login.html'
	authentication_form = LoginForm

	def get_success_url(self):
		if self.request.user.is_superuser:
			return reverse_lazy('admin_dashboard')
		else:
			return reverse_lazy('dashboard')