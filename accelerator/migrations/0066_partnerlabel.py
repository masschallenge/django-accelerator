# Generated by Django 2.2.10 on 2021-08-25 01:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0065_organization_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('label', models.CharField(max_length=255)),
                ('partners', models.ManyToManyField(blank=True, to=settings.ACCELERATOR_PARTNER_MODEL)),
            ],
            options={
                'abstract': False,
                'managed': True,
                'swappable': 'ACCELERATOR_PARTNERLABEL_MODEL',
            },
        ),
    ]
