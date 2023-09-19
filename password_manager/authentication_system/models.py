from django.db import models

# Create your models here.
class MyUsers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')
    phone = models.CharField('Contact Phone', max_length=15)
    zip_code  = models.CharField('Zip Code', max_length=30)
    address = models.CharField(max_length=300)
    web  = models.URLField('Website Address', blank=True)
    
    class Meta:
        db_table = 'myusers'

    def __str__(self):
        return self.first_name + ' ' + self.last_name
