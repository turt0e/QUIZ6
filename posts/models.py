from django.db import models
from django.conf import settings

class Posts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)
