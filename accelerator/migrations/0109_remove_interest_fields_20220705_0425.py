from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0108_add_associated_industry_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coreprofile',
            name='judge_interest',
        ),
        migrations.RemoveField(
            model_name='coreprofile',
            name='mentor_interest',
        ),
        migrations.RemoveField(
            model_name='coreprofile',
            name='speaker_interest',
        ),
    ]
