from django.db import models


class Compound(models.Model):
    id = models.BigAutoField(primary_key=True)
    smiles = models.TextField(null=False, unique=True)

    def __str__(self) -> str:
        return self.smiles
