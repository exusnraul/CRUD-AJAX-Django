from django.contrib import admin
from .models import Studentmodel
# Register your models here.

@admin.register(Studentmodel)
class StudentmodelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','desc']
    

