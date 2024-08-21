from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, AbstractBaseUser
# 1. Create an email field
# 2. Override the username field
# 3. A user manager
# 4. register the user model with django admin

# 3.
class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('Users must have an email')
        
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    def create_superuser(self, email, password):
        user = self.create_user(email,password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
class User(AbstractUser):
    # 1.
    email = models.EmailField(unique=True, max_length=255,verbose_name='Email')
    # 2.
    username = models.CharField(unique=False,max_length=10)

    USERNAME_FIELD = "email" 
    REQUIRED_FIELDS = ['username']
    # 3.

