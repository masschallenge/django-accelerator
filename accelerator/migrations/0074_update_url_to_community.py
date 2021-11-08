# Generated by Django 2.2.10 on 2021-11-05 12:29

from django.db import migrations
from django.db.models.query_utils import Q


def update_url_to_community(apps, schema_editor):
  people_url = "/people"
  mentor_url = "/directory"
  community_url = "/community"
  SiteRedirectPage = apps.get_model('accelerator', 'SiteRedirectPage')
  for siteredirectpage in SiteRedirectPage.objects.all():
    has_old_url = siteredirectpage.objects.filter(Q(new_url=people_url)| Q(new_url=mentor_url))
    if has_old_url.exists():
      has_old_url.update(new_url=community_url)
        
class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0073_auto_20210909_1706'),
    ]

    operations = [
        migrations.RunPython(update_url_to_community,
                             migrations.RunPython.noop)
    ]
