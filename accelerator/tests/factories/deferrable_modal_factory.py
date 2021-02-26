import swapper

from datetime import (
    timedelta,
)
from factory import (
    Sequence,
    post_generation,
)
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice
from accelerator_abstract.models.base_base_profile import USER_TYPES

DeferrableModal = swapper.load_model('accelerator', 'DeferrableModal')


class DeferrableModalFactory(DjangoModelFactory):
    class Meta:
        model = DeferrableModal

    name = Sequence(lambda n: "DeferrableModal name {0}".format(n))
    type = Sequence(lambda n: "DeferrableModal type {0}".format(n))
    header = Sequence(lambda n: "DeferrableModal header {0}".format(n))
    submit_button = Sequence(lambda n: "Submit button text {0}".format(n))
    defer_button = Sequence(lambda n: "Deferment button text {0}".format(n))
    content = Sequence(lambda n: "Deferment button content {0}".format(n))
    duration = timedelta(days=1)
    user_type = FuzzyChoice([type[0] for type in USER_TYPES])
    active_program = False
    published = False

    @post_generation
    def user_role(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for user_role in extracted:
                self.user_role.add(user_role)

    @post_generation
    def program(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for program in extracted:
                self.program.add(program)

    @post_generation
    def program_family(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for program_family in extracted:
                self.program_family.add(program_family)
