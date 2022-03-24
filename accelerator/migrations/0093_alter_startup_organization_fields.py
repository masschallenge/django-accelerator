# Generated by Django 2.2.24 on 2022-03-24 05:01

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accelerator', '0092_update_business_proposition_20220318_1245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allocator',
            options={
                'managed': False,
                'verbose_name_plural': 'Allocators'},
        ),
        migrations.AlterModelOptions(
            name='application',
            options={
                'managed': False,
                'ordering': ['startup'],
                'verbose_name_plural':
                'Applications'},
        ),
        migrations.AlterModelOptions(
            name='applicationanswer',
            options={
                'managed': False,
                'verbose_name_plural':
                'Application Answers'},
        ),
        migrations.AlterModelOptions(
            name='applicationpanelassignment',
            options={
                'managed': False,
                'ordering': ('panel_slot_number',),
                'verbose_name_plural':
                    'assignments of startup applications to panel'},
        ),
        migrations.AlterModelOptions(
            name='applicationquestion',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='applicationtype',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='baseprofile',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='bucketstate',
            options={'managed': False, 'ordering': ['sort_order']},
        ),
        migrations.AlterModelOptions(
            name='businessproposition',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='categoryheaderpage',
            options={
                'managed': False,
                'verbose_name': 'Category Header',
                'verbose_name_plural': 'Category Headers'},
        ),
        migrations.AlterModelOptions(
            name='clearance',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='communityparticipation',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='coreprofile',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='criterion',
            options={
                'managed': False,
                'verbose_name': 'Application Allocator Criterion',
                'verbose_name_plural': 'Application Allocator Criteria'},
        ),
        migrations.AlterModelOptions(
            name='criterionoptionspec',
            options={
                'managed': False,
                'verbose_name': 'Application Allocator Criterion Option'},
        ),
        migrations.AlterModelOptions(
            name='currency',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='deferrablemodal',
            options={'managed': False, 'verbose_name': 'Deferrable Modal'},
        ),
        migrations.AlterModelOptions(
            name='ethnoracialidentity',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='expertcategory',
            options={
                'managed': False,
                'ordering': ['name'],
                'verbose_name': 'Expert Category',
                'verbose_name_plural': 'Expert Categories'},
        ),
        migrations.AlterModelOptions(
            name='expertinterest',
            options={
                'managed': False,
                'verbose_name_plural': 'Expert Interests'},
        ),
        migrations.AlterModelOptions(
            name='expertinteresttype',
            options={
                'managed': False,
                'verbose_name_plural': 'Expert Interest Types'},
        ),
        migrations.AlterModelOptions(
            name='filepage',
            options={
                'managed': False,
                'verbose_name': 'File',
                'verbose_name_plural': 'Files'},
        ),
        migrations.AlterModelOptions(
            name='functionalexpertise',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='genderchoices',
            options={
                'managed': False,
                'ordering': ['name'],
                'verbose_name': 'Gender Choice',
                'verbose_name_plural': 'Gender Choices'},
        ),
        migrations.AlterModelOptions(
            name='geographicexperience',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='interestcategory',
            options={
                'managed': False,
                'verbose_name_plural': 'Interest Categories'},
        ),
        migrations.AlterModelOptions(
            name='jobposting',
            options={
                'managed': False,
                'verbose_name_plural': 'Job postings for startups'},
        ),
        migrations.AlterModelOptions(
            name='judgeapplicationfeedback',
            options={
                'managed': False,
                'verbose_name_plural': 'Judge Application Feedback'},
        ),
        migrations.AlterModelOptions(
            name='judgeavailability',
            options={
                'managed': False,
                'ordering': ['panel_time__start_date_time',
                             'panel_type__panel_type',
                             'panel_location__location'],
                'verbose_name_plural':
                    'Judge availability for specific Panel types,'
                    'times, locations'},
        ),
        migrations.AlterModelOptions(
            name='judgefeedbackcomponent',
            options={
                'managed': False,
                'verbose_name_plural': 'Feedback Components'},
        ),
        migrations.AlterModelOptions(
            name='judgepanelassignment',
            options={
                'managed': False,
                'verbose_name_plural':
                'assignments of judge to panel'},
        ),
        migrations.AlterModelOptions(
            name='judgeroundcommitment',
            options={
                'managed': False,
                'verbose_name_plural':
                    'Judge commitment to participate in a Judging Round'},
        ),
        migrations.AlterModelOptions(
            name='judgingform',
            options={
                'managed': False,
                'verbose_name_plural': 'Judging Forms'},
        ),
        migrations.AlterModelOptions(
            name='judgingformelement',
            options={
                'managed': False,
                'ordering': ['form_type', 'element_number'],
                'verbose_name_plural': 'Judging Form Elements'},
        ),
        migrations.AlterModelOptions(
            name='judginground',
            options={
                'managed': False,
                'ordering': ['program__program_status',
                             '-program__end_date',
                             '-end_date_time', 'name'],
                'verbose_name_plural': 'Judging Rounds'},
        ),
        migrations.AlterModelOptions(
            name='legalcheck',
            options={'managed': False, 'verbose_name': 'Legal Check'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={
                'managed': False,
                'verbose_name_plural': 'locations'},
        ),
        migrations.AlterModelOptions(
            name='mentoringspecialties',
            options={
                'managed': False,
                'ordering': ['name'],
                'verbose_name': 'Mentoring Specialty',
                'verbose_name_plural': 'Mentoring Specialties'},
        ),
        migrations.AlterModelOptions(
            name='mentorprogramofficehour',
            options={
                'managed': False,
                'ordering': ['start_date_time'],
                'verbose_name': 'Office Hour'},
        ),
        migrations.AlterModelOptions(
            name='modelchange',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='namedgroup',
            options={'managed': False, 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='navtree',
            options={
                'managed': False,
                'verbose_name_plural': 'NavTrees'},
        ),
        migrations.AlterModelOptions(
            name='navtreeitem',
            options={
                'managed': False,
                'verbose_name_plural': 'NavTreeItems'},
        ),
        migrations.AlterModelOptions(
            name='newsletter',
            options={
                'managed': False,
                'ordering': ('-created_at', 'name')},
        ),
        migrations.AlterModelOptions(
            name='newsletterreceipt',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='nodepublishedfor',
            options={
                'managed': False,
                'verbose_name': 'Node is Published For',
                'verbose_name_plural': 'Node is Published For'},
        ),
        migrations.AlterModelOptions(
            name='nodesubnavassociation',
            options={
                'managed': False,
                'verbose_name': 'Node Sub Navigation Association',
                'verbose_name_plural':
                    'Node Sub Navigation Associations'},
        ),
        migrations.AlterModelOptions(
            name='observer',
            options={
                'managed': False,
                'ordering': ['last_name', 'first_name'],
                'verbose_name': 'Observer',
                'verbose_name_plural': 'Observers'},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={
                'managed': False,
                'ordering': ['name'],
                'verbose_name_plural': 'Organizations'},
        ),
        migrations.AlterModelOptions(
            name='organizationnote',
            options={
                'managed': False,
                'verbose_name': 'Organization note'},
        ),
        migrations.AlterModelOptions(
            name='panel',
            options={
                'managed': False,
                'verbose_name_plural': 'Panels'},
        ),
        migrations.AlterModelOptions(
            name='panellocation',
            options={
                'managed': False,
                'ordering': ['judging_round', 'description'],
                'verbose_name_plural': 'Panel Locations'},
        ),
        migrations.AlterModelOptions(
            name='paneltime',
            options={
                'managed': False,
                'ordering': ['judging_round', 'start_date_time'],
                'verbose_name_plural': 'Panel Times'},
        ),
        migrations.AlterModelOptions(
            name='paneltype',
            options={
                'managed': False,
                'ordering': ['judging_round', 'description'],
                'verbose_name_plural': 'Panel Types'},
        ),
        migrations.AlterModelOptions(
            name='partner',
            options={
                'managed': False,
                'ordering': ['organization__name'],
                'verbose_name_plural': 'Partners'},
        ),
        migrations.AlterModelOptions(
            name='partnerapplicationinterest',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='partnerjudgeapplicationassignment',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='partnerjudginginstructions',
            options={
                'managed': False,
                'verbose_name_plural':
                    'Partner judging Round instructions'},
        ),
        migrations.AlterModelOptions(
            name='partnerjudgingroundchallenge',
            options={
                'managed': False,
                'verbose_name_plural':
                    'Partner Judging Round Challenges'},
        ),
        migrations.AlterModelOptions(
            name='partnerlabel',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='partnerteammember',
            options={
                'managed': False,
                'ordering': ['team_member__last_name',
                             'team_member__first_name'],
                'verbose_name_plural': 'Partner Team Members'},
        ),
        migrations.AlterModelOptions(
            name='paypalpayment',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='paypalrefund',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='program',
            options={
                'managed': False,
                'verbose_name_plural': 'Programs'},
        ),
        migrations.AlterModelOptions(
            name='programcycle',
            options={
                'managed': False,
                'verbose_name_plural': 'program cycles'},
        ),
        migrations.AlterModelOptions(
            name='programfamily',
            options={
                'managed': False,
                'verbose_name_plural': 'program families'},
        ),
        migrations.AlterModelOptions(
            name='programfamilylocation',
            options={
                'managed': False,
                'verbose_name': 'Program Family Location',
                'verbose_name_plural': 'Program Family Locations'},
        ),
        migrations.AlterModelOptions(
            name='programoverride',
            options={
                'managed': False,
                'verbose_name_plural': 'Program Overrides'},
        ),
        migrations.AlterModelOptions(
            name='programpartner',
            options={
                'managed': False,
                'ordering': ['program__name',
                             'partner_type__sort_order',
                             'partner'],
                'verbose_name_plural': 'Program Partner'},
        ),
        migrations.AlterModelOptions(
            name='programpartnertype',
            options={
                'managed': False,
                'ordering': ['program', 'sort_order'],
                'verbose_name_plural': 'Program Partner Types'},
        ),
        migrations.AlterModelOptions(
            name='programrole',
            options={
                'managed': False,
                'ordering': ['name'],
                'verbose_name': 'Program Role',
                'verbose_name_plural': 'Program Roles'},
        ),
        migrations.AlterModelOptions(
            name='programrolegrant',
            options={
                'managed': False,
                'verbose_name': 'Program Role Grant',
                'verbose_name_plural': 'Program Role Grants'},
        ),
        migrations.AlterModelOptions(
            name='programstartupattribute',
            options={
                'managed': False,
                'ordering': ['program', 'attribute_label']},
        ),
        migrations.AlterModelOptions(
            name='programstartupstatus',
            options={
                'managed': False,
                'ordering': ['program',
                             'sort_order',
                             'startup_status'],
                'verbose_name_plural': 'Program Startup Statuses'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='reference',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='refundcode',
            options={
                'managed': False,
                'verbose_name_plural': 'Refund Codes'},
        ),
        migrations.AlterModelOptions(
            name='refundcoderedemption',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='scenario',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='scenarioapplication',
            options={
                'managed': False,
                'verbose_name_plural': 'Scenario Applications'},
        ),
        migrations.AlterModelOptions(
            name='scenariojudge',
            options={
                'managed': False,
                'verbose_name_plural': 'Scenario Judges'},
        ),
        migrations.AlterModelOptions(
            name='scenariopreference',
            options={
                'managed': False,
                'ordering': ['priority']},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={
                'managed': False,
                'ordering': ('newsletter', 'sequence')},
        ),
        migrations.AlterModelOptions(
            name='site',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='siteprogramauthorization',
            options={
                'managed': False,
                'verbose_name_plural': 'Site Program Authorizations'},
        ),
        migrations.AlterModelOptions(
            name='siteredirectpage',
            options={
                'managed': False,
                'verbose_name': 'Site Redirect',
                'verbose_name_plural': 'Site Redirects'},
        ),
        migrations.AlterModelOptions(
            name='startup',
            options={
                'managed': False,
                'verbose_name_plural': 'Startups'},
        ),
        migrations.AlterModelOptions(
            name='startupattribute',
            options={
                'managed': False,
                'verbose_name_plural': 'Startup Attributes'},
        ),
        migrations.AlterModelOptions(
            name='startupcycleinterest',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='startuplabel',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='startupmentorrelationship',
            options={
                'managed': False,
                'verbose_name_plural': 'Startup Mentor Relationships'},
        ),
        migrations.AlterModelOptions(
            name='startupmentortrackingrecord',
            options={
                'managed': False,
                'verbose_name': 'Mentor Tracking Record',
                'verbose_name_plural': 'Mentor Tracking Records'},
        ),
        migrations.AlterModelOptions(
            name='startupoverridegrant',
            options={
                'managed': False,
                'verbose_name_plural': 'Startup Override Grants'},
        ),
        migrations.AlterModelOptions(
            name='startupprograminterest',
            options={'managed': False, 'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='startuprole',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='startupstatus',
            options={
                'managed': False,
                'verbose_name_plural': 'Startup Statuses'},
        ),
        migrations.AlterModelOptions(
            name='startupteammember',
            options={
                'managed': False,
                'verbose_name_plural': 'Startup Team Members'},
        ),
        migrations.AlterModelOptions(
            name='userdeferrablemodal',
            options={
                'managed': False,
                'verbose_name': 'User Deferrable Modal'},
        ),
        migrations.AlterModelOptions(
            name='userlabel',
            options={'managed': False, 'ordering': ['label']},
        ),
        migrations.AlterModelOptions(
            name='userlegalcheck',
            options={
                'managed': False,
                'verbose_name': 'User Legal Check'},
        ),
        migrations.AlterModelOptions(
            name='usernote',
            options={
                'managed': False,
                'verbose_name': 'User note'},
        ),
        migrations.AlterModelOptions(
            name='userrole',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='userrolemenu',
            options={
                'managed': False,
                'verbose_name': 'User Role Menu',
                'verbose_name_plural': 'User Role Menus'},
        ),
        migrations.AlterField(
            model_name='industry',
            name='parent',
            field=mptt.fields.TreeForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='children',
                to=settings.MPTT_SWAPPABLE_INDUSTRY_MODEL),
        ),
    ]
