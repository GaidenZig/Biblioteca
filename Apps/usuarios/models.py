from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

USERNAME_REGEX='^[a-zA-Z0-9,+-]*$'
# Create your models here. 
class MyUserManager(BaseUserManager):
    def create_user(self,username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        user=self.model(username= username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username, email, password=None):
        user= self.create_user(username,email, password=password)        
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser,PermissionsMixin):
    username= models.CharField(max_length=10, validators=[
        RegexValidator(
            regex=USERNAME_REGEX,
            message='Username must be alphanumeric or contain numbers',
            code='invalid_username')
        ],unique=True)    
    email= models.EmailField(max_length=80,unique=True,verbose_name='email address')
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    img_perfil= models.ImageField(default='images/no-image.png', upload_to='images/')
    is_active=models.BooleanField(default=True)
    descripcion=models.TextField(max_length=1000, null=True,blank=True)
    objects= MyUserManager()
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email']

    #def image_url(self):
    #    if self.img_perfil and hasattr(self.img_perfil, 'url'):
    #        return self.img_perfil.url
    #    else:
    #        return '/media/images/no-image.png'
