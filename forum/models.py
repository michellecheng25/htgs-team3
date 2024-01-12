import uuid
from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    content = models.TextField(null=False)

    def __str__(self) -> str:
        return self.content