# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-04 16:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0049_update_fluent_page_links_to_redirect_view'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nodesidenavassociation',
            options={
                'managed': True,
                'verbose_name': 'Node Side Navigation Association',
                'verbose_name_plural': 'Node Side Navigation Associations'
            },
        ),
        migrations.AlterField(
            model_name='nodesidenavassociation',
            name='side_nav',
            field=models.ForeignKey(
                help_text=(
                    'This is the sub navigation '
                    'tree that this page is tied to'
                ),
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.ACCELERATOR_NAVTREE_MODEL),
        ),
        migrations.AlterField(
            model_name='nodesidenavassociation',
            name='sub_nav_item',
            field=models.ForeignKey(
                help_text=(
                    'This is the sub navigation '
                    'item that this page it tied to'
                ),
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.ACCELERATOR_NAVTREEITEM_MODEL),
        ),
    ]
