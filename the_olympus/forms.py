from django import forms
from the_olympus.models import Invitation

class InvitationForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'register-form__input'})
    )
    role = forms.ChoiceField(
        choices=[('user', 'User'), ('admin', 'Admin')],
        widget=forms.Select(attrs={'class': 'register-form__input'})
    )
    
    class Meta:
        model = Invitation
        fields = ['email', 'role']
