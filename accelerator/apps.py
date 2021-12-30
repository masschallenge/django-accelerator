from django.apps import AppConfig


class AcceleratorConfig(AppConfig):
    name = 'accelerator'

    def ready(self):
        from accelerator_abstract.apps import add_get_profile_to_user_class
        add_get_profile_to_user_class()
