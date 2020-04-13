import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Student12
from .forms import Student_Form
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.core.serializers import serialize
from django.views.generic import View
# Create your views here.
def show_detalis(request):
    # if request.method=="post":
    #     data=request.POST['sear']
    #     print(data)
    #     qs=Student12.objects.filter(name__icontains=data)
    #     return render(request,'show.html',{'data':qs})
    qs=Student12.objects.all()
    page_no=request.GET.get('pageno')
    p=Paginator(qs,2)
    if page_no:
        res=p.page(page_no)
    else:
        page_no=1
        res=p.page(page_no)
    return render(request,'show.html',{'res':res})


def save_details(request):
    if request.method=="POST":
        student=Student_Form(request.POST)
        if student.is_valid():
            student.save()
            messages.success(request,'details are saved')
            return redirect('save')
        else:
            messages.success(request, 'somthing wrong')
            return redirect('save')
    else:
        student=Student_Form()
        return render(request,'save.html',{'student':student})


def update_details(request):
    idno=request.GET.get('idno')
    qs=get_object_or_404(Student12,idno=idno)
    if request.method=="POST":
        student_from=Student_Form(request.POST,instance=qs)
        if student_from.is_valid():
            student_from.save()
            messages.success(request,'details are updated')
            return redirect('show_details')
        else:
            return render(request,'edit.html',{'student_form':student_from})
    else:
        student_from=Student_Form(instance=qs)
        return render(request,'edit.html',{'student_form':student_from})


def delete_details(request):
    idno=request.GET.get('idno')
    qs=Student12.objects.get(idno=idno)
    if qs:
        qs.delete()
        messages.success(request,'record is deleted successfully')
        return redirect('show_details')
    else:
        messages.error(request,'something went wrong')
        return redirect('show_details')
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# from rest_framework.viewsets import ModelViewSet
# from .serial import Emp_serialize
# class Viewset_Emp(ModelViewSet):
#     queryset = Student12.objects.all()
#     serializer_class = Emp_serialize
# class Viewset_Details(ModelViewSet):
#     queryset = Student12.objects.all()
#     serializer_class = Emp_serialize
#     lookup_field = ('idno',)
class Student_serial(View):
    def get(self,request,*args,**kwargs):
        qs=Student12.objects.all()
        res=serialize('json',qs)
        p_data=json.loads(res)
        print(p_data)
        a=[]
        b={}
        for x in p_data:
            if x['pk'] not in a:
                b['idno']= x['pk']
                a.append(dict(**b,**x['fields']))
        print(a)
        j_data=json.dumps(a)
        return HttpResponse(j_data)
class Student_details(View):
    def get(self,request,idno,*args,**kwargs):
        try:
            qs=Student12.objects.get(idno=idno)
            res=serialize('json',[qs,])
            p_data=json.loads(res)
            a=[]
            b={}
            for x in p_data:
                if x['pk'] not in a:
                    b['idno']=x['pk']
                    a.append(dict(**b,**x['fields']))
            j_data=json.dumps(a)
            return HttpResponse(j_data)
        except Student12.DoesNotExist:
            return HttpResponse('not avaibale')


def search(request):
    if 'search' in request.POST:
        tearm = request.POST['tearm']
        data=Student12.objects.filter(name__icontains=tearm)
        result = []
        for r in data:
            result.append(r.name)
        resp = json.dumps(result)
        return HttpResponse(resp, content_type='application/json')

