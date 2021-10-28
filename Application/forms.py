from django import forms
from django.contrib.auth import authenticate
from django.forms import PasswordInput
from Application.models import Reply, Topic


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100, required=True)
    password = forms.CharField(widget=PasswordInput(), required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError('Invalid login.')
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class SignupForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "First Name"}), max_length=100, required=True)
    last_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder": "Last Name"}), max_length=100, required=True)
    email = forms.CharField(widget= forms.TextInput(attrs={"placeholder": "Email"}), max_length=20, required=True)
    role = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Role"}), max_length=100, required=True)
    username = forms.CharField(widget= forms.TextInput(attrs={"placeholder": "Username"}), max_length=100, required=True)
    password = forms.CharField(widget=PasswordInput(attrs={"placeholder": "Password"}), min_length=8, max_length=100, required=True)
    confirm_password = forms.CharField(widget=PasswordInput(attrs={"placeholder": "Confirm Password"}),min_length=8,
                                        max_length=100, required=True)


class ForgotPassForm(forms.Form):
    email = forms.CharField(widget= forms.TextInput(attrs={"placeholder": "Email"}), max_length=20, required=True)
    new_password = forms.CharField(widget=PasswordInput(attrs={"placeholder": "New Password"}), min_length=8, max_length=100, required=True)
    confirm_password = forms.CharField(widget=PasswordInput(attrs={"placeholder": "Confirm Password"}), min_length=8,
                                       max_length=100, required=True)


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('subject', 'course', 'content')
        labels = {
            'content': '',
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('content',)
        labels = {
            'content': '',
        }