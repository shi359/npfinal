from django import forms
from django.db import models
from django.utils.safestring import mark_safe
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
        
class Reg(models.Model):
    def valid_mail(value):
        #Reg.objects
        u = Reg.objects.filter(mail = value).exists()
        if u:
            raise ValidationError(
                 _("this email has already been registered") 
                )
        return value
    def valid_name(value):
        if len(value) < 3:
            raise ValidationError(
                 _("name must longer than 3 words")   
                )
        return value    
    def valid_pwd(value):
        if(len(value) < 6):
            raise ValidationError(
                  _("password must longer than 6 characters")  
                    )
        return value    
    mail = models.EmailField(validators=[valid_mail],max_length=100)
    name = models.CharField(validators=[valid_name],max_length=50)
    password = models.CharField(validators=[valid_pwd],max_length=50)
    
    def __str__(self):
        return self.name

class RegForm(ModelForm):
    class Meta:
        model = Reg
        fields = ['mail','name','password']
        labels = {
          'mail': mark_safe('Email'), 
          'name': mark_safe('Name'), 
          'password': mark_safe('Password') 
        }
        widgets = {
                'mail': forms.TextInput(attrs={'class':'fill_form'}),    
            'password': forms.PasswordInput(attrs={'class':'fill_form'}),
        }

class LoginForm(forms.Form):
    def valid_account(value):
        if not Reg.objects.filter(mail=value).exists():
            raise ValidationError(
                 _("You didn't register")   
                    )
        return value  
    #def valid_pwd(value):
     #   pwd = Reg.objects.filter(mail = m, password=value).exists()
      #  if not pwd:
       #     raise ValidationError(
        #        _("wrong password %s") % m
         #       )
       # return value    
    account = forms.EmailField(validators=[valid_account],label=mark_safe('Email'), widget=forms.TextInput(attrs={'class':'fill_form'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'fill_form'}))
