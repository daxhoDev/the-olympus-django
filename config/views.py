from the_olympus.models import Profile, Plan
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django import forms

class ProfileCreationForm(UserCreationForm):
	email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'register-form__input'}))
	plan = forms.ModelChoiceField(
		queryset=Plan.objects.all(),
		required=False,
		empty_label="--Select a plan--",
		widget=forms.Select(attrs={'class': 'register-form__input'})
	)
	
	class Meta:
		model = Profile
		fields = ['username', 'email', 'plan', 'password1', 'password2']
		widgets = {
			'username': forms.TextInput(attrs={'class': 'register-form__input'}),
		}
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['password1'].widget.attrs.update({'class': 'register-form__input'})
		self.fields['password2'].widget.attrs.update({'class': 'register-form__input'})

class SignupView(CreateView):
	model = Profile
	form_class = ProfileCreationForm
	success_url = reverse_lazy('landing')
	template_name = 'auth/signup.html'