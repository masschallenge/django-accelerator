from django.db import migrations


def add_home_community_to_users(apps, schema_editor):
    Community = apps.get_model('accelerator', 'Community')
    User = apps.get_model('simpleuser', 'User')

    community_ids = Community.objects.values_list('id', flat=True)

    filter = {('programrolegrant__program_role__program__program_family'
               '__home_community__in'):  community_ids}
    select_related = 'program_role__program__program_family__home_community'
    ordering = ('program_role__program__program_family__home_community__'
                'assignment_order')
    users = User.objects.filter(**filter).distinct()

    for user in users:
        role = user.programrolegrant_set.select_related(
            select_related).order_by(ordering)[0]
        community = role.program_role.program.program_family.home_community
        profile = user.get_profile()
        profile.home_community = community
        profile.save()


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0115_add_ecosystem_model'),
    ]

    operations = [
        migrations.RunPython(add_home_community_to_users,
                             migrations.RunPython.noop)]
