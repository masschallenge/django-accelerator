# Generated by Django 2.2.16 on 2021-05-31 15:00

from django.db import migrations


PROGRAM_ROLE_IDS = [1434, 2012, 2011, 2184, 2008, 2004, 2005, 2009, 1960, 2061,
                    1986, 2073, 2028, 2226, 1939, 1941, 2139, 2238, 2062, 1961,
                    2060, 1985, 2072, 2027, 2225, 1938, 1942, 2138, 2237, 2063,
                    2010, 1998, 1999, 1962, 1973, 1974, 1997, 2000, 2079, 2076,
                    2074, 2235, 2078, 2077, 2075, 2234, 2162, 2161, 884, 43]


def update_program_roles(apps, schema_editor):
    ProgramRole = apps.get_model('accelerator', 'ProgramRole')
    ProgramRole.objects.exclude(
        id__in=PROGRAM_ROLE_IDS).update(landing_page="")


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0044_move_all_fields_from_expert_to_coreprofile'),
    ]

    operations = [
        migrations.RunPython(update_program_roles,
                             migrations.RunPython.noop)
    ]
