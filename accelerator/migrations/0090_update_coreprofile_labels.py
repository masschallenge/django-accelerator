# Generated by Django 2.2.27 on 2022-03-09 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def add_expert_categories(apps, schema_editor):
    ExpertCategory = apps.get_model('accelerator', 'ExpertCategory')
    ExpertCategory.objects.bulk_create(
        [ExpertCategory(name=name)
         for name in ['Entrepreneur', 'Subject Matter Expert']])


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator',
         '0089_remove_community_participation_read_more_prompts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coreprofile',
            name='expert_category',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='coreprofile_experts',
                to=settings.ACCELERATOR_EXPERTCATEGORY_MODEL,
                verbose_name='My background is primarily as a(n)'),
        ),
        migrations.AlterField(
            model_name='coreprofile',
            name='primary_industry',
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={'level__exact': 0},
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='coreprofile_experts',
                to=settings.MPTT_SWAPPABLE_INDUSTRY_MODEL,
                verbose_name='Primary Industry/Experience'),
        ),
        migrations.RunPython(add_expert_categories,
                             migrations.RunPython.noop)
    ]