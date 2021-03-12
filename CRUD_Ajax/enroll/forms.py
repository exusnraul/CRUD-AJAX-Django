from django import forms
from .models import Studentmodel


class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Studentmodel
        fields = '__all__'
        labels= {'name':'Input Name','email':'Enter-Email','desc':'Description'}
        widgets = {'name':forms.TextInput(attrs={'class':'form-control','id':'id-name','placeholder':'Enter Name'}),
                    'email':forms.EmailInput(attrs={'class':'form-control','id':'id-email','placeholder':'name@mail.com'}),
                    'desc':forms.Textarea(attrs={'class':'form-control','id':'id-desc','placeholder':'Describe'})
        }



    
