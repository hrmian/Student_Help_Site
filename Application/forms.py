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