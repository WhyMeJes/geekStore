from django.contrib.auth.forms import AuthenticationForm
from users.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control py-4','placeholder':'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control py-4','placeholder':'Введите пароль'}))
    class Meta:
        model = User
        fields = ('username', 'password')

    def __int__(self,*args,**kwargs):
        super(UserLoginForm, self).__init__(*args,**kwargs)
        for field_name in self.fields.items():
            field_name.widget.attrs['class'] = 'form-control py-4'