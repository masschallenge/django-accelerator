from accelerator.models import CoreProfile


class EntrepreneurProfile(CoreProfile):
    user_type = 'entrepreneur'
    default_page = "applicant_homepage"

    class Meta:
        db_table = 'accelerator_entrepreneurprofile'
