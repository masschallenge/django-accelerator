# Generated by Django 2.2.24 on 2021-07-01 20:17

from django.db import migrations


def update_criterion_specs(apps, schema_editor):
    CriterionOptionSpec = apps.get_model("CriterionOptionSpec",
                                         "accelerator")
    CriterionOptionSpec.objects.filter(option="m").update(option="male")
    CriterionOptionSpec.objects.filter(option="fem").update(option="female")    


def reverse_update(apps, schema_editor):
    CriterionOptionSpec = apps.get_model("CriterionOptionSpec",
                                         "accelerator")
    CriterionOptionSpec.objects.filter(option="male").update(option="m")
    CriterionOptionSpec.objects.filter(option="female").update(option="f")    

    
    
class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0062_update_polymorphic_ctype'),
    ]

    operations = [
        migrations.RunPython(update_criterion_specs,
                             reverse=reverse_update)
    ]
