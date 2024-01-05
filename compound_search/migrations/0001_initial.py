from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Compound",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("smiles", models.TextField(unique=True)),
            ],
        ),
    ]
