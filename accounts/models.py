from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, phone, password):
        email = self.normalize_email(email)
        User = self.model(email=email, phone=phone)
        User.set_password(password)
        User.save(using=self._db)
        return User

class user(AbstractUser): 
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    phone = models.CharField(max_length=15)
    objects = UserManager()


class ticket(models.Model):
    subject = models.CharField(max_length=30, blank=True, null=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, db_index=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE) 