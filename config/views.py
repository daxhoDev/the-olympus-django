from config.forms import LoginForm, ProfileCreationForm
from the_olympus.models import Profile
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from the_olympus.models import Invitation
from django.shortcuts import get_object_or_404

class SignupView(CreateView):
	model = Profile
	form_class = ProfileCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.html'

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		token = self.kwargs.get('token')
		if token:
			kwargs['token'] = token
		return kwargs

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		token = self.kwargs.get('token')
		if token:
			try:
				invitation = Invitation.objects.get(token=token, is_active=True)
				context['invitation'] = invitation
			except Invitation.DoesNotExist:
				context['invitation'] = None
				get_object_or_404(Invitation, token=token)
		return context

	
class CustomLoginView(LoginView):
	template_name = 'registration/login.html'
	authentication_form = LoginForm

	def get_success_url(self):
		if self.request.user.is_superuser:
			return reverse_lazy('admin_dashboard')
		else:
			return reverse_lazy('dashboard')