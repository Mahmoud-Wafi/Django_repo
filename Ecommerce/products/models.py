from django.db import models

# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=50)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    description= models.TextField()
    image=models.ImageField(upload_to='photos/%y/%m/%d')
    active= models.BooleanField(default=True)
    
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name='Product'
        ordering=['-name']