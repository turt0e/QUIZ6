from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username, contact, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        if not contact:
            raise ValueError("Users must have a contact number")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            contact=contact,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, contact, password=None):
        user = self.create_user(
            email=email,
            password=password,
            username=username,
            contact=contact,
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=200, unique=True)
    username = models.CharField(max_length=255, unique=True)
    contact = models.CharField(max_length=20, blank=True, null=True, unique=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'  # User can login using username
    REQUIRED_FIELDS = ['email', 'contact']  # Specify additional required fields for createsuperuser

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
