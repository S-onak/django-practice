from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser, BaseUserManager, AbstractUser
)

# Create your models here.

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique = True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)  # 로그인 할 수 있는가? (휴면계정 여부)
    staff = models.BooleanField(default=False)  # superuser가 아닌 staff
    admin = models.BooleanField(default=False)  # superuser
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
def __str__(self):
    return self.email

def is_staff(self):
    return self.staff

def is_superuser(self):
    return self.admin
