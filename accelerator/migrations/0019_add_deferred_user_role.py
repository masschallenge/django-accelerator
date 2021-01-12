# Generated by Django 2.2.10 on 2020-04-09 21:24

from django.db import migrations


def add_deferred_user_role(apps, schema_editor):
    DEFERRED_MENTOR = 'Deferred Mentor'
    UserRole = apps.get_model('accelerator', 'UserRole')
    Program = apps.get_model('accelerator', 'Program')
    ProgramRole = apps.get_model('accelerator', 'ProgramRole')
    if UserRole.objects.filter(name=DEFERRED_MENTOR).exists():
        user_role = UserRole.objects.filter(name=DEFERRED_MENTOR)[0]
    else:
        user_role = UserRole.objects.create(name=DEFERRED_MENTOR,
                                            sort_order=17)
    for program in Program.objects.all():
        if not ProgramRole.objects.filter(user_role=user_role,
                                          program=program).exists():
            name = "{} {} ({}-{})".format(
                (program.end_date.year if program.end_date else ""),
                DEFERRED_MENTOR,
                program.program_family.url_slug.upper(),
                program.pk)

            ProgramRole.objects.get_or_create(
                program=program,
                user_role=user_role,
                name=name)


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0018_make_location_nonrequired'),
    ]

    operations = [
        migrations.RunPython(add_deferred_user_role,
                             migrations.RunPython.noop)
    ]