import json
import urllib.request
from django.core.files.uploadedfile import SimpleUploadedFile
from urllib.parse import urlparse
from django.db import migrations

DATA_MAPPING_URL = ('https://home-community-image.'
                    's3.amazonaws.com/mapping.json')


def set_home_community(apps, schema_editor):
    ProgramFamily = apps.get_model('accelerator', 'ProgramFamily')
    Community = apps.get_model('accelerator', 'Community')

    data = [{"name": "MC Switzerland",
             "email": "support.2622.15317b82e21677f6@helpscout.net",
             "is_default": True,
             "assignment_order": 1,
             "image": ("https://home-community-image.s3"
                       ".amazonaws.com/mc_images/mc_swiss.jpg"),
             "icon": ("https://home-community-image.s3"
                      ".amazonaws.com/icons/mc_swiss.png")},
            {"name": "MC Israel",
             "email": "support.2622.5304df655bf8538a@helpscout.net",
             "is_default": False,
             "assignment_order": 2,
             "image": ("https://home-community-image.s3"
                       ".amazonaws.com/mc_images/mc_israel.jpg"),
             "icon": ("https://home-community-image.s3"
                      ".amazonaws.com/icons/mc_israel.png")},
            {"name": "MC Mexico",
             "email": "support.2622.5012bf8e0f9cb2f7@helpscout.net",
             "is_default": False,
             "assignment_order": 3,
             "image": ("https://home-community-image.s3"
                       ".amazonaws.com/mc_images/mc_mexico.jpg"),
             "icon": ("https://home-community-image.s3"
                      ".amazonaws.com/icons/mc_mexico.png")},
            {'name': 'MC Bridge',
             "email": 'support.2622.1347a3fe9de0848d@helpscout.net',
             "is_default": False,
             "assignment_order": 4,
             "image": ("https://home-community-image.s3"
                       ".amazonaws.com/mc_images/mc_bridge.jpg"),
             "icon": ("https://home-community-image.s3"
                      ".amazonaws.com/icons/mc_bridge.png")},
            {"name": "MC United States",
             "email": "community@masschallenge.helpscoutapp.com",
             "is_default": False,
             "assignment_order": 5,
             "image": ("https://home-community-image.s3"
                       ".amazonaws.com/mc_images/mc_united_state.jpg"),
             "icon": ("https://home-community-image.s3"
                      ".amazonaws.com/icons/mc_usa.png")}]

    community_mapper = {}

    for item in data:
        image_name = urlparse(item['image']).path.split('/')[-1]
        image_tmpfile, _ = urllib.request.urlretrieve(item['image'])
        icon_name = urlparse(item['icon']).path.split('/')[-1]
        icon_tmpfile, _ = urllib.request.urlretrieve(item['icon'])
        community_data = {'name': item['name'],
                          'email': item['email'],
                          'is_default': item['is_default'],
                          'is_visible': True,
                          'assignment_order': item['assignment_order'],
                          'image': SimpleUploadedFile(image_name,
                                                      open(image_tmpfile,
                                                           "rb").read()),
                          'icon': SimpleUploadedFile(icon_name,
                                                     open(icon_tmpfile,
                                                          "rb").read())}
        community = Community.objects.create(**community_data)
        community_mapper[item['name']] = community

    response = urllib.request.urlopen(DATA_MAPPING_URL)
    mappings = json.loads(response.read())
    program_family_data = []
    for mapping in mappings:
        family_name = mapping["Program Family"]
        program_family = ProgramFamily.objects.filter(name=family_name)
        program_family = program_family.first()
        if program_family:
            community_name = mapping["Home Community"]
            community = community_mapper[community_name]
            program_family.home_community = community
            program_family_data.append(program_family)
    ProgramFamily.objects.bulk_update(program_family_data, ['home_community'])


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0116_add_program_menu_sidenav'),
    ]

    operations = [
        migrations.RunPython(set_home_community,
                             migrations.RunPython.noop)]
