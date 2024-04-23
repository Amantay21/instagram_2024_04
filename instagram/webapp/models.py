from django.db import models

class Publication(models.Model):
    image = models.CharField(max_length=500, verbose_name='Фото' )
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    
