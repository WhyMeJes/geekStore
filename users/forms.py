from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Введите пароль'}))
    required_css_class = 'form-control py-4'
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for a in self.fields:
            self.fields[a].widget.attrs.update({'class': 'form-control py-4'})

    error_messages = {
        "invalid_login": (
            "Неправильное имя пользователя или пароль "),"inactive": ("Аккаунт деактивирован"),
    }


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Введите почту'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Подтвердите пароль'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for a in self.fields:
            self.fields[a].widget.attrs.update({'class': 'form-control py-4'})

class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly':True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'readonly':True}))
    image = forms.ImageField(widget=forms.FileInput(),required=False)
    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name','image')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for a in self.fields:
            self.fields[a].widget.attrs.update({'class': 'form-control py-4'})
        self.fields['image'].widget.attrs.update({'class':'custom-file-input'})
