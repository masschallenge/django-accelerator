from django.db import migrations
import swapper


# RunPython code from old migrations, per http://bit.ly/mc-migration-trimming

# 0008
LOCATION_TO_NAME_MAPPING = {
    "(Phone) Provide a preferred contact number below.": 'Remote',
    "ATLAS VENTURE:  25 First Street, St 303 Cambridge": 'Other',
    "Call +1-508-244-9854 at start time.": 'Remote',
    "Cloud conference room": 'MassChallenge Boston',
    "Cobalt": 'MassChallenge Boston',
    "FOLEY & LARDNER": 'Other',
    "Fog Conference Room @ MassChallenge": 'MassChallenge Boston',
    "Lounge": 'MassChallenge Boston',
    "MC Lounge": 'MassChallenge Boston',
    "Magenta Conference Room": 'MassChallenge Boston',
    "MassChallenge Boston": 'MassChallenge Boston',
    "MassChallenge Israel - Jerusalem": 'MassChallenge Israel',
    "MassChallenge Israel - Tel Aviv": 'MassChallenge Tel Aviv',
    "MassChallenge Lounge": 'MassChallenge Boston',
    "MassChallenge Mexico": 'MassChallenge Mexico',
    "MassChallenge Rhode Island": 'MassChallenge Rhode Island',
    "MassChallenge Switzerland": 'MassChallenge Switzerland',
    "MassChallenge Texas": 'MassChallenge Austin',
    "MassChallenge Texas - Austin": 'MassChallenge Austin',
    "MassChallenge Texas - Houston": 'MassChallenge Houston',
    "MassChallenge UK": 'MassChallenge UK',
    "OFFSITE: General Catalyst Offices": 'Other',
    "OFFSITE: Third Rock Ventures": 'Other',
    "Offline w KB, entered by Matt": 'Other',
    "Other - see description": 'Other',
    "PULSE@MassChallenge": 'MassChallenge Boston',
    "Pulse@MassChallenge": 'MassChallenge Boston',
    "Remote - see description": 'Remote',
    "mc lounge": 'MassChallenge Boston',
    "phone call": 'MassChallenge Boston'
}

def migrate_office_hours_locations(apps, schema_editor):
    Location = apps.get_model('accelerator', 'Location')
    MentorProgramOfficeHour = apps.get_model('accelerator',
                                             'MentorProgramOfficeHour')
    location_values = set(MentorProgramOfficeHour.objects.values_list(
        "old_location", flat=True))
    for old_location in location_values:
        new_location_name = LOCATION_TO_NAME_MAPPING[old_location]
        location, _ = Location.objects.get_or_create(name=new_location_name)
        MentorProgramOfficeHour.objects.filter(
            old_location=old_location).update(location=location)

# 0012
def delete_unused_user_roles(apps, schema_editor):
    unused_roles = ("Senior Judge", "Active Judge")
    UserRole = apps.get_model('accelerator', 'UserRole')
    UserRole.objects.filter(name__in=unused_roles).delete()

# 0019
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

# 0029
GENDER_CHOICES = ("Male", "Female", "Cisgender", "Transgender",
    "Non-Binary", "I Prefer To Self-describe", "I Prefer Not To Say")

def add_gender_choices(apps, schema_editor):
    GenderChoices = apps.get_model('accelerator', 'GenderChoices')
    db_gender_choices = GenderChoices.objects.all().values_list(
        'name', flat=True)
    missing_gender_choices = set(GENDER_CHOICES).difference(db_gender_choices)
    if missing_gender_choices:
        GenderChoices.objects.bulk_create(
            [GenderChoices(name=choice) for choice in missing_gender_choices])

# 0032
ETHNO_RACIAL_IDENTITY_LIST = [
    'Black', 'East and/or Southeast Asian',
    'Hispanic, Latinx, and/or Spanish', 'Indigenous',
    'Native Hawaiian, Pacific Islander, or Polynesian',
    'Middle Eastern and/or North African', 'North and/or Central Asian',
    'South Asian', 'White or Caucasian', 'I prefer not to say'
]
def add_ethno_racial_identity_data(*args, **kwargs):
    EthnoRacialIdentity = swapper.load_model(
        'accelerator', 'EthnoRacialIdentity')
    for ethno_racial_identity in ETHNO_RACIAL_IDENTITY_LIST:
        EthnoRacialIdentity.objects.create(identity=ethno_racial_identity)

# 0033
GENDER_MAP = {
    "m": "Male",
    "f": "Female",
    "o": "I Prefer To Self-describe",
    "p": "I Prefer Not To Say"
}

def get_gender_choice_obj_dict(apps):
    GenderChoices = apps.get_model("accelerator", "GenderChoices")
    return {
        gender_choice.name: gender_choice
        for gender_choice in GenderChoices.objects.all()
    }

def add_gender_identity_data(model, gender_choices):
    ThroughModel = model.gender_identity.through
    for gender, gender_identity in GENDER_MAP.items():
        gender_choice = gender_choices[gender_identity]
        profiles = model.objects.filter(gender=gender)
        ThroughModel.objects.bulk_create([
            ThroughModel(**{
                f"{model.__name__.lower()}": profile,
                "genderchoices": gender_choices[gender_identity]
            })
            for profile in profiles if not profile.gender_identity.filter(
                pk=gender_choice.pk).exists()
        ], ignore_conflicts=True)

def migrate_gender_data_to_gender_identity(apps, schema_editor):
    gender_choices = get_gender_choice_obj_dict(apps)
    MemberProfile = apps.get_model("accelerator", "MemberProfile")
    ExpertProfile = apps.get_model("accelerator", "ExpertProfile")
    EntrepreneurProfile = apps.get_model("accelerator", "EntrepreneurProfile")
    for model in [EntrepreneurProfile, ExpertProfile, MemberProfile]:
        add_gender_identity_data(model, gender_choices)


class Migration(migrations.Migration):

    dependencies = [('accelerator', '0001_initial')]

    operations = [
        migrations.RunPython(
            code=add_gender_choices, reverse_code=migrations.RunPython.noop
        ),
        migrations.RunPython(
            code=migrate_office_hours_locations, reverse_code=migrations.RunPython.noop,
        ),
        migrations.RunPython(
            code=delete_unused_user_roles, reverse_code=migrations.RunPython.noop
        ),
        migrations.RunPython(
            code=add_deferred_user_role, reverse_code=migrations.RunPython.noop
        ),
        migrations.RunPython(
            code=add_ethno_racial_identity_data, reverse_code=migrations.RunPython.noop
        ),
        migrations.RunPython(
            code=migrate_gender_data_to_gender_identity, reverse_code=migrations.RunPython.noop
        ),
    ]