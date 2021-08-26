# Generated by Django 2.2.24 on 2021-08-26 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0067_auto_20210824_1704'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partnerjudginginstructions',
            options={'managed': True, 'verbose_name_plural': 'instructions from a partner'},
        ),
        migrations.AlterField(
            model_name='partnerjudginginstructions',
            name='instructions',
            field=models.TextField(help_text='Partner Judging instructions for judging rounds', max_length=1000),
        ),
    ]
