from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserCar, History

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class UserCarForm(forms.ModelForm):
    class Meta:
        model = UserCar
        fields = ['mark', 'model', 'year', 'photo']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        user_car = super().save(commit=False)
        if self.request and self.request.user:
            user_car.user = self.request.user
        if commit:
            user_car.save()
        return user_car

class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = ['note', 'image']
        widgets = {
            'note': forms.Textarea(attrs={'rows': 3}),
            'image': forms.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(HistoryForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        history = super(HistoryForm, self).save(commit=False)
        if self.request:
            history.user = self.request.user
        if commit:
            history.save()
        return history