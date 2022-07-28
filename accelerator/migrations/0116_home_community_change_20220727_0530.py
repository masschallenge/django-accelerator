import json
import urllib.request
from django.core.files.uploadedfile import SimpleUploadedFile
from urllib.parse import urlparse
from django.db import migrations


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
                    ".amazonaws.com/icons/mc_swiss.png")
            },{
             "name": "MC Israel",
             "email": "support.2622.5304df655bf8538a@helpscout.net",
             "is_default": False,
             "assignment_order": 2,
             "image": ("https://home-community-image.s3"
                       ".amazonaws.com/mc_images/mc_israel.jpg"),
             "icon": ("https://home-community-image.s3"
                      ".amazonaws.com/icons/mc_israel.png")
            },{
             "name": "MC Mexico",
             "email": "support.2622.5012bf8e0f9cb2f7@helpscout.net",
             "is_default": False,
             "assignment_order": 3,
             "image": ("https://home-community-image.s3"
                       ".amazonaws.com/mc_images/mc_mexico.jpg"),
             "icon": ("https://home-community-image.s3"
                      ".amazonaws.com/icons/mc_mexico.png")
            },{
             'name': 'MC Bridge',
             "email": 'support.2622.1347a3fe9de0848d@helpscout.net',
             "is_default": False,
             "assignment_order": 4,
             "image": ("https://home-community-image.s3"
                       ".amazonaws.com/mc_images/mc_bridge.jpg"),
             "icon": ("https://home-community-image.s3"
                      ".amazonaws.com/icons/mc_bridge.png")
            },{
             "name": "MC United States",
             "email": "community@masschallenge.helpscoutapp.com",
             "is_default": False,
             "assignment_order": 5,
             "image": ("https://home-community-image.s3"
                       ".amazonaws.com/mc_images/mc_united_state.jpg"),
             "icon": ("https://home-community-image.s3"
                      ".amazonaws.com/icons/mc_usa.png")}]

    for item in data:
        image_name = urlparse(item['image']).path.split('/')[-1]
        image_tmpfile, _ = urllib.request.urlretrieve(item['image'])

        icon_name = urlparse(item['icon']).path.split('/')[-1]
        icon_tmpfile, _ = urllib.request.urlretrieve(item['icon'])

        community = Community()
        community.name = item['name']
        community.is_default = item['is_default']
        community.is_visible = True
        community.assignment_order = item['assignment_order']
        community.image = SimpleUploadedFile(image_name,
                                             open(image_tmpfile,
                                                  "rb").read())
        community.icon = SimpleUploadedFile(icon_name,
                                            open(icon_tmpfile,
                                                 "rb").read())
        community.save()
    response = urllib.request.urlopen(('https://home-community-image.'
                                       's3.amazonaws.com/mapping.json'))
    mappings = json.loads(response.read())
    for mapping in mappings:
        family_name = mapping["Program Family"]
        program_family = ProgramFamily.objects.filter(name=family_name)
        program_family = program_family.first()
        if program_family:
            community_name = mapping["Home Community"]
            community = Community.objects.filter(name=community_name).first()
            program_family = program_family
            program_family.home_community = community
            program_family.save()


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0115_add_ecosystem_model'),
    ]

    operations = [
        migrations.RunPython(set_home_community,
                             migrations.RunPython.noop)]
