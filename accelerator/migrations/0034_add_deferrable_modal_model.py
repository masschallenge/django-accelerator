# Generated by Django 2.2.10 on 2021-03-02 17:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0033_migrate_gender_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeferrableModal',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('created_at', models.DateTimeField(
                    auto_now_add=True,
                    null=True)),
                ('updated_at', models.DateTimeField(
                    auto_now=True,
                    null=True)),
                ('name', models.CharField(
                    default='',
                    help_text='Deferrable modal name',
                    max_length=255)),
                ('type', models.CharField(
                    default='',
                    help_text='Deferrable modal type',
                    max_length=35)),
                ('header', models.CharField(
                    default='',
                    help_text='Deferrable modal header text',
                    max_length=255)),
                ('submit_button', models.CharField(
                    default='',
                    help_text='Submit button text',
                    max_length=255)),
                ('defer_button', models.CharField(
                    default='',
                    help_text='Deferment button text',
                    max_length=255)),
                ('content', models.TextField(
                    default='',
                    help_text='Modal popup content can accept HTML')),
                ('duration', models.DurationField(
                    blank=True,
                    help_text=('Default deferment duration. Format: '
                               'days hours:minutes:seconds e.g 1 00:00:00'),
                    null=True)),
                ('user_type', models.CharField(
                    blank=True,
                    choices=[('EXPERT', 'Expert'),
                             ('ENTREPRENEUR', 'Entrepreneur'),
                             ('MEMBER', 'Member')],
                    max_length=35,
                    null=True)),
                ('active_program', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=False)),
                ('redirect_url', models.CharField(
                    blank=True,
                    max_length=255,
                    null=True)),
                ('program', models.ManyToManyField(
                    blank=True,
                    to=settings.ACCELERATOR_PROGRAM_MODEL)),
                ('program_family', models.ManyToManyField(
                    blank=True,
                    to=settings.ACCELERATOR_PROGRAMFAMILY_MODEL)),
                ('user_role', models.ManyToManyField(
                    blank=True,
                    to=settings.ACCELERATOR_USERROLE_MODEL)),
            ],
            options={
                'verbose_name': 'Deferrable Modal',
                'abstract': False,
                'managed': True,
                'swappable': None,
            },
        ),
    ]
