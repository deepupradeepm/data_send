from django.db import models

# Create your models here.
class Student12(models.Model):
    idno=models.IntegerField(db_column='Idno',primary_key=True)
    name=models.CharField(max_length=50)
    sal=models.IntegerField(db_column='Sal')

    class Meta:
        managed=False
        db_table='student12'
