from django.shortcuts import render
from .forms import StudentForm
from .models import Studentmodel
from django.http import JsonResponse
# Create your views here.

def home(request):
    # if request.method == 'POST':
    form = StudentForm(request.POST)
    stud = Studentmodel.objects.all()
    return render (request,'enroll/home.html',{'form':form,'stud':stud})



def save_data(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            sid = request.POST.get('stuid')
            name = request.POST['name']
            email = request.POST['email']
            desc = request.POST['desc']
            if(sid == ''):
                usr = Studentmodel(name=name , email = email , desc= desc)
            else:
                usr = Studentmodel(id =sid,name=name , email = email , desc= desc)
            usr.save()
            stud = Studentmodel.objects.values()
            # print(stud)
            student_data = list(stud)
            print(student_data)
            return JsonResponse({'status':'save','student_data':student_data})
        else:
            return JsonResponse({'status':0})



def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        print(id)
        pi = Studentmodel.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})



def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        print(id)
        student = Studentmodel.objects.get(pk=id)
        student_data = {'id':student.id,'name':student.name,'email':student.email,'desc':student.desc}
        return JsonResponse(student_data)
    