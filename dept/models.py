from django.db import models

# Create your models here.

class department(models.Model):
    dept_no=models.IntegerField()
    d_name=models.CharField(max_length=50)
    loc=models.CharField(max_length=50)
    

    def __str__(self):
        return self.d_name


class employee(models.Model):
    emp_no=models.IntegerField(primary_key=True)
    e_name=models.CharField(max_length=50)
    job=models.CharField(max_length=50)
    mgr=models.IntegerField()
    hirdate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField()
    dept_no=models.ForeignKey(department,on_delete=models.CASCADE)

    def __str__(self):
        return self.e_name
    