from django.db import models

# Create your models here.
class Apidata(models.Model):
     no = models.AutoField(db_column='NO',primary_key= True)
     pcode = models.CharField(db_column='PCODE', max_length=4)
     contents = models.CharField(db_column='contents', max_length=1000, blank = True, null = True)
     datetime = models.CharField(db_column='datetime', max_length=100, blank = True, null = True)
     title = models.CharField(db_column='title', max_length=100, blank = True, null = True)
     url = models.CharField(db_column='url', max_length=100, blank = True, null = True)
