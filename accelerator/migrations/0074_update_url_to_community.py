# Generated by Django 2.2.10 on 2021-11-05 12:29

from django.db import migrations
from django.db.models.query_utils import Q


def update_url_to_community(apps, schema_editor):
    people_url = ["/people", "/people"]
    mentor_url = "/directory"
    mentor_refinement_url = "/directory/?refinementList%5Bhome_program_family%5D%5B0%5D=Israel"
    community_url = "/community"
    community_refinement_url = "/community/?refinementList%5Bprogram_family_names%5D%5B0%5D=Israel"

    SiteRedirectPage = apps.get_model('accelerator', 'SiteRedirectPage')
    SiteRedirectPage.objects.filter(
      Q(new_url__in=people_url) | Q(new_url=mentor_url)
      ).update(new_url=community_url)

    if mentor_refinement_url:
      SiteRedirectPage.objects.filter(mentor_refinement_url
      ).update(community_refinement_url)


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0073_auto_20210909_1706'),
    ]

    operations = [
        migrations.RunPython(update_url_to_community,
                             migrations.RunPython.noop)
    ]
