from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from the_olympus.models import Profile, Plan, Invitation

class ProfileCreationForm(UserCreationForm):
	email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'register-form__input'}))
	plan = forms.ModelChoiceField(
		queryset=Plan.objects.all(),
		required=False,
		empty_label="--Select a plan--",
		widget=forms.Select(attrs={'class': 'register-form__input'})
	)

	bank_account = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'register-form__input'}))
	
	class Meta:
		model = Profile
		fields = ['username', 'email', 'plan', 'bank_account' , 'password1', 'password2']
		widgets = {
			'username': forms.TextInput(attrs={'class': 'register-form__input'}),
		}
	
	def __init__(self, *args, **kwargs):
		self.token = kwargs.pop('token', None)
		super().__init__(*args, **kwargs)
		self.fields['password1'].widget.attrs.update({'class': 'register-form__input'})
		self.fields['password2'].widget.attrs.update({'class': 'register-form__input'})
		
		# Si hay un token, verificar el role de la invitación
		if self.token:
			try:
				invitation = Invitation.objects.get(token=self.token)
				self.invitation_role = invitation.role
				
				# Pre-llenar el email y hacerlo readonly
				self.fields['email'].initial = invitation.email
				self.fields['email'].widget.attrs['readonly'] = True
				
				if invitation.role == 'admin':
					# Para admin, ocultar bank_account y plan
					del self.fields['bank_account']
					del self.fields['plan']
				else:
					# Para user, bank_account y plan son requeridos
					self.fields['bank_account'].required = True
					self.fields['plan'].required = True
			except Invitation.DoesNotExist:
				self.invitation_role = None
				# Si no existe la invitación, mostrar los campos requeridos
				self.fields['bank_account'].required = True
				self.fields['plan'].required = True
		else:
			self.invitation_role = None
			# Sin token, mostrar los campos requeridos
			self.fields['bank_account'].required = True
			self.fields['plan'].required = True

	def save(self, commit=True):
		user = super().save(commit=False)
		user.email = self.cleaned_data['email']
		
		# Establecer is_superuser según el role de la invitación
		if self.invitation_role == 'admin':
			user.is_superuser = True
			user.is_staff = True
		else:
			user.is_superuser = False
			user.is_staff = False
		
		if commit:
			user.save()
			# Marcar la invitación como inactiva si se usó un token
			if self.token:
				try:
					invitation = Invitation.objects.get(token=self.token)
					invitation.is_active = False
					invitation.save()
				except Invitation.DoesNotExist:
					pass
		return user

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'register-form__input'})
        self.fields['password'].widget.attrs.update({'class': 'register-form__input'})