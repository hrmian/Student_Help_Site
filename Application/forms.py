from django import forms
from django.forms import PasswordInput
from Application.models import Thread, Post, User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    ROLES = (
        ('Student', 'Student'),
        ('Professor', 'Professor'),
        ('Alum', 'Alum'),
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'role')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
        self.fields['role'].choices = self.ROLES

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.role = self.cleaned_data['role']

        if commit:
            user.save()

        return user

class EditAccount(forms.ModelForm):
    ROLES = (
        ('Student', 'Student'),
        ('Professor', 'Professor'),
        ('Alum', 'Alum'),
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'role')

    def __init__(self, *args, **kwargs):
        super(EditAccount, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['role'].choices = self.ROLES

    def save(self, commit=True):
        user = super(EditAccount, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.role = self.cleaned_data['role']

        if commit:
            user.save()

        return user


class ForgotPassForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Email"}), max_length=20, required=True)
    new_password = forms.CharField(widget=PasswordInput(attrs={"placeholder": "New Password"}), min_length=8,
                                   max_length=100, required=True)
    confirm_password = forms.CharField(widget=PasswordInput(attrs={"placeholder": "Confirm Password"}), min_length=8,
                                       max_length=100, required=True)


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('subject',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)
        labels = {
            'content': '',
        }