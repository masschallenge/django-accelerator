# Generated by Django 2.2.10 on 2022-03-03 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0086_alter_founder_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='bipoc_founder',
            field=models.BooleanField(
                default=False,
                verbose_name='BIPOC Founder'),
        ),
        migrations.AddField(
            model_name='startup',
            name='female_or_transgender_founder',
            field=models.BooleanField(
                default=False,
                verbose_name='Female or Transgender Founder'),
        ),
        migrations.AddField(
            model_name='startup',
            name='first_time_founder',
            field=models.BooleanField(
                default=False,
                verbose_name='First-time Founder'),
        ),
        migrations.AddField(
            model_name='startup',
            name='is_startup',
            field=models.BooleanField(
                default=False),
        ),
        migrations.AddField(
            model_name='startup',
            name='location_street_address',
            field=models.CharField(
                blank=True,
                default='',
                help_text='Please specify the street address for your main office (headquarters).', 
                max_length=100),
        ),
        migrations.AlterField(
            model_name='coreprofile',
            name='preferred_name',
            field=models.CharField(
                blank=True,
                max_length=32,
                null=True,
                verbose_name='Nickname / Preferred Name'),
        ),
    ]
