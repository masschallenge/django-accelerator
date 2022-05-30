# Generated by Django 2.2.28 on 2022-05-30 12:49

from django.db import (
    migrations,
    models,
)
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator', '0104_update_startupupdate_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='business_proposition',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='accelerator.BusinessProposition'),
        ),
        migrations.AddField(
            model_name='judgingformelement',
            name='business_proposition_section',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='judginground',
            name='use_business_proposition',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='judgingformelement',
            name='element_type',
            field=models.CharField(
                choices=[
                    ('answer', 'Application Answer'),
                    ('boilerplate', 'Boilerplate'),
                    ('feedback', 'Feedback'),
                    ('business_proposition', 'Business Proposition')],
                max_length=64),
        ),
    ]
