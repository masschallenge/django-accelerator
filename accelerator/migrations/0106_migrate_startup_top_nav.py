# Generated by Django 2.2.10 on 2021-11-24 16:41
import swapper
from django.db import migrations


def add_startup_profile_top_nav(apps, schema_editor):
    NavTreeItem = apps.get_model('accelerator', 'NavTreeItem')
    NavTree = swapper.load_model('accelerator', 'NavTree')
    nav_items = [
        {"title": 'My Startups',
         'alias': 'my_startup',
         'url': '/mystartups'},
        {"title": 'Dashboard',
         'alias': 'dashboard',
         'urlaspattern': True,
         'url': 'startup_dashboard startup.id'},
        {"title": 'Company Profile',
         'alias': 'company_profile',
         'urlaspattern': True,
         'url': 'startup_profile startup.id'},
        {"title": 'Business Proposition',
         'alias': 'business_proposition',
         'urlaspattern': True,
         'url': 'business_proposition_view startup.id'},
        {"title": 'Progress',
         'alias': 'progress',
         'urlaspattern': True,
         'url': 'startup_update_view startup.id'},
        {"title": 'Team',
         'alias': 'startup_team',
         'urlaspattern': True,
         'url': 'startup_team_view startup.id'},
    ]
    nav_tree = NavTree.objects.filter(
        alias='startup_profile_manager_subnav').first()
    if not nav_tree:
        nav_tree = NavTree.objects.create(
            title='Startup Profile Manager',
            alias='startup_profile_manager_subnav')

    for item in nav_items:
        defaults = {
            'title': item['title']
        }
        if item['urlaspattern']:
            defaults['urlaspattern'] = item['urlaspattern']
        NavTreeItem.objects.get_or_create(
            alias=item['alias'],
            url=item['url'],
            tree__pk=nav_tree.id,
            defaults=defaults)

class Migration(migrations.Migration):
    dependencies = [
        ('accelerator',
         '0105_inclusion_of_business_proposition_model_changes'),
    ]
    operations = [
        migrations.RunPython(add_startup_profile_top_nav,
                             migrations.RunPython.noop)
    ]
