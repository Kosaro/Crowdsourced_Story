from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewChoiceForm(forms.Form):
    choice_text = forms.CharField(label='choice_text', max_length=100)
    plot_point_text = forms.CharField(label='plotpoint-text', max_length=1000)
    plot_point_id = forms.IntegerField(label='plot_point_id')
    author = forms.CharField(label='author', max_length=20)

class OpenPlotPointForm(forms.Form):
    destination_id = forms.IntegerField(label='destination_id')

class ToggleBookmarkForm(forms.Form):
    plot_point_id = forms.IntegerField(label='plot_point_id')
    user = forms.CharField(label='user', max_length=20)

class ToggleUpvoteForm(forms.Form):
    plot_point_id = forms.IntegerField(label='plot_point_id')
    user = forms.CharField(label='user', max_length=20)

class ToggleDownvoteForm(forms.Form):
    plot_point_id = forms.IntegerField(label='plot_point_id')
    user = forms.CharField(label='user', max_length=20)

class LogInForm(forms.Form):
    user = forms.CharField(label='user_name', max_length=20)
    password = forms.CharField(label='password', max_length=20)

#class SignupForm(forms.Form):
    #user = forms.CharField(label='username', max_length=20)
    #email = forms.CharField(label='email', max_length=20)
    #password = forms.CharField(label='password1', max_length=20)
    #confirm_password = forms.CharField(label='password2', max_length=20)

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

