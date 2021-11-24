import swapper
from pytz import utc

from datetime import datetime
from django.db.models import Q
from django.urls import reverse

from accelerator.models import (
    CoreProfile,
    UserRole)
from accelerator.utils import UserAlert
from accelerator_abstract.models import (
    ACTIVE_PANEL_STATUS,
    CAPTURE_AVAILABILITY_DISABLED)

CONFIRMED_FOR_MESSAGE = "<h4>%s, you are confirmed for %s:</h4>"
EXPECTING_TO_SEE_YOU_MESSAGE = ("<p>&nbsp;</p><h4>We are expecting "
                                "to see you at %s.</h4>")
SINGLE_PANEL_MESSAGE = "this upcoming judging panel"
MULTIPLE_PANELS_MESSAGE = "these upcoming judging panels"
PLEASE_INFORM_US_MESSAGE = ("<p>&nbsp;</p><p><b>PLEASE INFORM US IMMEDIATELY "
                            'AT <a href="mailto:%s">%s</a>'
                            "IF YOU ARE NO LONGER ABLE TO MAKE %s. "
                            "THANKS!</b></p>")
ACTIVE_IN_PERSON_JUDGING_MESSAGE = (
    'You are assigned to an active judging panel, please'
    '&nbsp;<b><a class="btn btn-primary btn-large" href="%s">'
    'go to your judging portal to review applications</a></b>'
    '<p>&nbsp;</p>'
)

ONGOING_ONLINE_JUDGING_NOTIFICATION = (
    'You are assigned to an active online judging round, please'
    '<p>&nbsp;</p><b><a class="btn btn-primary btn-large" href="%s">'
    'go to your judging portal to review applications</a></b>'
    '<p>&nbsp;</p>'
)

UPDATE_JUDGE_COMMITMENTS_NOTIFICATION = (
    'There are upcoming judging opportunities for you to revew. '
    '<b><a class="btn btn-primary btn-large" href="%s"> '
    'Update your judging commitments</a></b>'
    '<p>&nbsp;</p>'
)
SHORT_BIO_MAX_LENGTH = 140


class ExpertProfile(CoreProfile):
    user_type = 'expert'
    default_page = "expert_homepage"

    class Meta:
        db_table = 'accelerator_expertprofile'
        permissions = (
            ('change_password', 'Can change users passwords directly'),
        )
        swappable = swapper.swappable_setting(
            CoreProfile.Meta.app_label, "ExpertProfile")

    def judge_round_commitments(self):
        return self.user.judgeroundcommitment_set.all()

    def user_id(self):
        return self.user.id

    def has_invited_judging_rounds(self):
        # True iff judge has desired state for upcoming
        # judging rounds, for which they have no commitment object
        # note that commitement object can indicate "decline to commit"
        JudgingRound = swapper.load_model('accelerator', 'JudgingRound')
        return JudgingRound.objects.filter(
            start_date_time__gt=utc.localize(datetime.now()),
            desired_judge_label__in=self.user.userlabel_set.all()).exclude(
            judgeroundcommitment__judge=self.user).exists()

    def get_active_assignments(self):
        jpas = self.get_all_panel_assignments(round_active=True)
        active_jpas = jpas.filter(panel__status=ACTIVE_PANEL_STATUS)
        return active_jpas

    @classmethod
    def mentors(cls, program):
        role_name = UserRole.MENTOR
        return ExpertProfile.objects.filter(
            user__programrolegrant__program_role__program=program,
            user__programrolegrant__program_role__user_role__name=role_name)

    def get_active_alerts(self, page=None):
        """Return any active alerts for the user, that are relevant for
        the current 'page' of the application
        """
        alerts = []
        panels_url = reverse('panel_listing', urlconf="mc_judge.urls")

        if self.has_invited_judging_rounds():
            alerts.append(self._invited_judge_alert())

        active_rounds = self.active_judging_rounds()
        if self.is_judge(state="confirmed") and active_rounds.exists():
            alert = UserAlert()
            alert.alert_type = 'judge-portal-access'
            alert.alert_style = 'success'
            alert.message = ACTIVE_IN_PERSON_JUDGING_MESSAGE % panels_url

            alerts.append(alert)

        if self.is_judge() and self.get_active_assignments().exists():
            alert = UserAlert()
            alert.alert_type = 'judge-panel-active'
            alert.alert_style = 'warning'

            alert.message = (ONGOING_ONLINE_JUDGING_NOTIFICATION %
                             panels_url)
        return alerts

    def _invited_judge_alert(self):
        manage_url = reverse('manage_commitments')
        alert = UserAlert()
        alert.alert_type = 'judge-invite'
        alert.alert_style = 'success'
        alert.message = UPDATE_JUDGE_COMMITMENTS_NOTIFICATION % manage_url
        return alert


def _recruiting_judges():
    capacity = Q(capture_capacity=True)
    availability = ~Q(capture_availability=CAPTURE_AVAILABILITY_DISABLED)
    return swapper.load_model('accelerator', 'JudgingRound').objects.filter(
        capacity | availability).exists()
