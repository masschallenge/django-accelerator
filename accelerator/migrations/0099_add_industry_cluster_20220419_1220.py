# Generated by Django 2.2.27 on 2022-04-19 16:20

import sorl.thumbnail.fields
from django.conf import settings
from django.db import (
    migrations,
    models,
)

class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0098_update_startup_update_20220408_0441'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndustryCluster',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('created_at', models.DateTimeField(
                    auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', sorl.thumbnail.fields.ImageField(
                    blank=True,
                    null=True,
                    upload_to='industry_cluster_images')),
            ],
            options={
                'verbose_name_plural': 'Industry Clusters',
                'db_table': 'accelerator_industrycluster',
                'abstract': False,
                'managed': True,
                'swappable': 'ACCELERATOR_INDUSTRYCLUSTER_MODEL',
            },
        ),
        migrations.AddField(
            model_name='coreprofile',
            name='industry_cluster_interest',
            field=models.ManyToManyField(
                blank=True,
                related_name='profiles',
                to=settings.ACCELERATOR_INDUSTRYCLUSTER_MODEL),
        ),
        migrations.AddField(
            model_name='program',
            name='supported_industry_clusters',
            field=models.ManyToManyField(
                blank=True,
                related_name='programs',
                to=settings.ACCELERATOR_INDUSTRYCLUSTER_MODEL),
        ),
    ]
