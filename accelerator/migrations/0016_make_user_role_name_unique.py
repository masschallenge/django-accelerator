# Generated by Django 2.2.10 on 2020-03-04 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0015_past_due_migrations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrole',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
