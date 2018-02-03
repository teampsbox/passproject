from django.db import models
from django.urls import reverse
from datetime import datetime

class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    address = models.TextField()
    gallon_code = models.CharField(max_length=5, blank=True, null=True)    
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["last_name"]

    
    def get_absolute_url(self):
        return reverse('customer_list')

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
        
