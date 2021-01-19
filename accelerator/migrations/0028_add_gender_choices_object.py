from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0027_add_birth_year_to_core_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenderChoices',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True,
                                                    null=True)),
                ('updated_at', models.DateTimeField(auto_now=True,
                                                    null=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Gender Choices',
                'db_table': 'accelerator_genderchoices',
                'abstract': False,
                'managed': True,
            },
        ),
    ]
