from django.db import models

class Category(models.Model):
    '''
    Classification, product type and identity such as clothes, electronic devices, and...
    '''
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=124)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name