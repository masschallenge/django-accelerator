# Generated by Django 2.2.24 on 2022-05-12 18:05

from django.db import migrations
from django.db.models import (
    Case,
    IntegerField,
    When,
)


def add_community_participation(through_model, profiles, participation):
    through_model.objects.bulk_create([
        through_model(**{
            "coreprofile": profile,
            "communityparticipation": participation
        })
        for profile in profiles
    ], ignore_conflicts=True)


def migrate_user_interest(apps, schema_editor):
    CommunityParticipation = apps.get_model(
        "accelerator", "CommunityParticipation")
    CoreProfile = apps.get_model("accelerator", "CoreProfile")
    participations = ['Judge', 'Mentor', 'Speaker']
    judge, mentor, speaker = CommunityParticipation.objects.filter(
        name__in=participations
    ).order_by(
        Case(*[When(name=name, then=index)
               for index, name in enumerate(participations)],
             output_field=IntegerField()))
    ThroughModel = CoreProfile.community_participation.through

    judge_profiles = CoreProfile.objects.filter(judge_interest=True)
    add_community_participation(ThroughModel, judge_profiles, judge)

    speaker_profiles = CoreProfile.objects.filter(speaker_interest=True)
    add_community_participation(ThroughModel, speaker_profiles, speaker)

    mentor_profiles = CoreProfile.objects.filter(mentor_interest=True)
    add_community_participation(ThroughModel, mentor_profiles, mentor)


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator', '0102_update_program_model'),
    ]

    operations = [
        migrations.RunPython(migrate_user_interest,
                             migrations.RunPython.noop)
    ]