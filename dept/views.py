from django.shortcuts import render
from django.http import HttpResponse
from dept.models import *
# Create your views here.

def dept_table(request):
    Loc=department.objects.all()
    d={'ddata':Loc}
    return render(request,'dept_table.html',d)


def emp_table(request):
    Loc=employee.objects.all()
    Loc=employee.objects.filter(hirdate__year='1881')
    Loc=employee.objects.filter(hirdate__year='1880')
    Loc=employee.objects.filter(hirdate__month='02')
    Loc=employee.objects.filter(hirdate__month='09')
    Loc=employee.objects.filter(hirdate__day='02')
    Loc=employee.objects.filter(hirdate__day='22')
    Loc=employee.objects.filter(job__startswith='s')
    Loc=employee.objects.filter(job__endswith='r')
    Loc=employee.objects.filter(job__contains='m')
    Loc=employee.objects.filter(job__regex='r')
    Loc=employee.objects.filter(job__in=('Salesman','Manager'))
    Loc=employee.objects.filter(mgr__in=('7698','7839'))
    Loc=employee.objects.all()


    d={'edata':Loc}
    return render(request,'emp_table.html',d)
