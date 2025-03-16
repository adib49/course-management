from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = CustomUser
        fields = ['username','password','role','unique_code']
    
    def save(self, commit = True):
        user = super().save(commit=False)
        raw_password = self.cleaned_data['password']
        user.set_password(raw_password)
        if commit:
            user.save()
        return user
