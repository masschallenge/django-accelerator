# Generated by Django 2.2.10 on 2021-12-07 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0077_update_sitetree_judging_commitment_view_url'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='partnerapplicationinterest',
            unique_together={('partner', 'judging_round', 'application')},
        ),
    ]
