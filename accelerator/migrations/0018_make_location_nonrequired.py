# Generated by Django 2.2.10 on 2020-04-16 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0017_add_required_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
