# Generated by Django 2.2.10 on 2022-02-14 11:30

from django.db import migrations, models

legal_check_description = (
    'I agree to the <a href="https://masschallenge.org/competition-rules" '
    'target="_blank">Competition Rules</a>, <a href="https://masschallenge.'
    'org/anti-harassment-policies" target="_blank">Anti-Harassment Policies'
    '</a>, <a href="https://masschallenge.org/website-terms-of-use"target='
    '"_blank">Site Terms of Use</a> and the <a href="https://masschallenge.org'
    '/expert-agreement" target="_blank">Expert Agreement</a>.')
legal_check_help_text = (
    'This legal check is only available for users with unified profiles. '
    '(Neither Experts nor Entrepreneurs)')
legal_check_name = 'competition_anti_harassment_expert_and_site_rule'


def add_unified_profile_legal_checks(apps, schema_editor):
    LegalCheck = apps.get_model('accelerator', 'LegalCheck')
    LegalCheck.objects.filter(
        name='privacy_notice').update(is_enabled_for_unified_profile=True)
    LegalCheck.objects.get_or_create(
        name='competition_anti_harassment_expert_and_site_rule',
        description=legal_check_description,
        is_enabled_for_experts=False,
        is_enabled_for_entrepreneurs=False,
        is_enabled_for_unified_profile=True, )


def revert_unified_profile_legal_checks(apps, schema_editor):
    LegalCheck = apps.get_model('accelerator', 'LegalCheck')
    LegalCheck.objects.filter(name=legal_check_name).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('accelerator', '0082_update_core_profile_20220203_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='legalcheck',
            name='is_enabled_for_unified_profile',
            field=models.BooleanField(
                default=False,
                help_text=legal_check_help_text)),
        migrations.RunPython(add_unified_profile_legal_checks,
                             revert_unified_profile_legal_checks)
    ]
