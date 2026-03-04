from django.db import models
from django.contrib.auth.models import AbstractUser

# _________________________ First Register ________________________

class Register(AbstractUser):
    class Meta:
        verbose_name = "Register"          
        verbose_name_plural = "Register"
        
# _________________________ Then Create Note ________________________    
class Note(models.Model):
    user=models.ForeignKey(Register, on_delete=models.CASCADE)
    title=models.CharField()
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

# Create your models here.
