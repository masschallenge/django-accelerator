from accelerator_abstract.models import (
    FORM_ELEM_FEEDBACK_TO_MC,
    FORM_ELEM_FEEDBACK_TO_STARTUP,
    FORM_ELEM_OVERALL_RECOMMENDATION,
)

from accelerator.models import (
    ASSIGNED_PANEL_ASSIGNMENT_STATUS,
    COMPLETE_PANEL_ASSIGNMENT_STATUS,
    FEEDBACK_DISPLAY_DISABLED as DISABLED,
    FEEDBACK_DISPLAY_ENABLED as ENABLED,
    IN_PERSON_JUDGING_ROUND_TYPE,
    ONLINE_JUDGING_ROUND_TYPE,

    PREVIEW_PANEL_STATUS,
    SUBMITTED_APP_STATUS,
    UserRole,
)
from accelerator.tests.factories import (
    ApplicationAnswerFactory,
    ApplicationFactory,
    ApplicationPanelAssignmentFactory,
    ExpertFactory,
    JudgeApplicationFeedbackFactory,
    JudgeFeedbackComponentFactory,
    JudgePanelAssignmentFactory,
    JudgeRoundCommitmentFactory,
    JudgingFormElementFactory,
    JudgingRoundFactory,
    PanelFactory,
    ProgramCycleFactory,
    ProgramRoleFactory,
    ProgramRoleGrantFactory,
    ScenarioFactory,
    StartupCycleInterestFactory,
    StartupProgramInterestFactory,
)

ELEMENT_NAMES = [
    FORM_ELEM_OVERALL_RECOMMENDATION,
    FORM_ELEM_FEEDBACK_TO_STARTUP,
    FORM_ELEM_FEEDBACK_TO_MC,
]
_round_type = {True: ONLINE_JUDGING_ROUND_TYPE,
               False: IN_PERSON_JUDGING_ROUND_TYPE}


class JudgeFeedbackContext:
    def __init__(self,
                 application=None,
                 num_components=1,
                 complete=True,
                 panel_status=PREVIEW_PANEL_STATUS,
                 display_feedback=False,
                 merge_feedback_with=None,
                 cycle_based_round=False,
                 online_round=True,
                 is_active=True,
                 judge_capacity=10):
        self.judging_capacity = 0
        if application:
            self.application = application
            self.cycle = application.cycle
        else:
            self.cycle = ProgramCycleFactory()
            self.application = ApplicationFactory(
                application_status=SUBMITTED_APP_STATUS,
                application_type=self.cycle.default_application_type,
                cycle=self.cycle)
        self.application_type = self.application.application_type
        self.applications = [self.application]
        self.startup = self.application.startup
        self.industry = self.startup.primary_industry
        feedback_display = ENABLED if display_feedback else DISABLED
        jr_kwargs = {
            'program__cycle': self.cycle,
            'round_type': _round_type[online_round],
            'feedback_display': feedback_display,
            'cycle_based_round': cycle_based_round,
            'application_type': self.application_type,
            'is_active': is_active,
        }
        if merge_feedback_with:
            jr_kwargs['feedback_merge_with'] = merge_feedback_with
        self.judging_round = JudgingRoundFactory(**jr_kwargs)
        self.program = self.judging_round.program
        self.panel = PanelFactory(status=panel_status,
                                  panel_time__judging_round=self.judging_round)
        self.scenario = ScenarioFactory(judging_round=self.judging_round)
        self.judge_role = ProgramRoleFactory(program=self.program,
                                             user_role__name=UserRole.JUDGE)
        self.judges = []
        self.judge = self.add_judge(complete=complete,
                                    capacity=judge_capacity)
        self.feedback = JudgeApplicationFeedbackFactory(
            judge=self.judge,
            application=self.application,
            panel=self.panel,
            form_type=self.judging_round.judging_form)
        self.judging_form = self.feedback.form_type
        self.application_assignment = ApplicationPanelAssignmentFactory(
            application=self.application,
            panel=self.panel,
            scenario=self.scenario)
        cycle_interest = StartupCycleInterestFactory(cycle=self.program.cycle,
                                                     startup=self.startup)
        StartupProgramInterestFactory(program=self.program,
                                      startup=self.startup,
                                      startup_cycle_interest=cycle_interest,
                                      applying=True)
        self.components = []
        self.elements = []
        self.application_questions = []
        self.application_answers = []
        for element_name in ELEMENT_NAMES:
            self.add_component(element_name=element_name)

        if complete:
            self.feedback.save()
            for _ in range(num_components):
                self.add_component()
        else:
            for _ in range(num_components):
                self.add_element()

    def add_application_answer(self, question=None, answer_text=None):
        question = question or self.application_questions[0]
        kwargs = {"application_question": question,
                  "application": self.application}
        if answer_text:
            kwargs["answer_text"] = answer_text
        app_answer = ApplicationAnswerFactory(**kwargs)
        self.application_answers.append(app_answer)
        return app_answer

    def add_component(self, element_name=None,
                      feedback_element=None,
                      add_answer=True,
                      answer_text=None):

        factory_params = {
            "judge_feedback": self.feedback, }

        if feedback_element is None:
            app_type_key = "__".join(["feedback_element",
                                      "application_question",
                                      "application_type"])
            factory_params.update(
                {
                    "feedback_element__form_type": self.judging_form,
                    "feedback_element__element_type": "feedback",
                    "feedback_element__mandatory": True,
                    "feedback_element__sharing": "share-with-startup",
                    app_type_key: self.application_type}
            )
            if element_name:
                factory_params['feedback_element__element_name'] = element_name
        else:
            factory_params.update({"feedback_element": feedback_element})

        if answer_text:
            factory_params["answer_text"] = answer_text

        component = JudgeFeedbackComponentFactory(
            **factory_params)
        self.components.append(component)
        question = component.feedback_element.application_question
        self.application_questions.append(question)
        if add_answer:
            app_answer = ApplicationAnswerFactory(
                application_question=question,
                application=self.application)
            self.application_answers.append(app_answer)
        if feedback_element is None:
            self.elements.append(component.feedback_element)
        self.feedback.save()
        return component

    def add_element(self,
                    feedback_type="",
                    element_type="feedback",
                    choice_layout="",
                    mandatory=True,
                    text_minimum=0,
                    text_minimum_units="",
                    answer_text=None):
        element = JudgingFormElementFactory(
            form_type=self.judging_form,
            mandatory=mandatory,{
            element_type=element_type,
            feedback_type=feedback_type,
            choice_layout=choice_layout,
            sharing="share-with-startup",
            application_question__application_type=self.application_type,
            text_minimum=text_minimum,
            text_minimum_units=text_minimum_units
        )
        application_question = element.application_question
        self.application_questions.append(application_question)
        answer_kwargs = {"application_question": application_question,
                         "application": self.application}
        if answer_text:
            answer_kwargs["answer_text"] = answer_text
        application_answer = ApplicationAnswerFactory(**answer_kwargs)
        self.application_answers.append(application_answer)
        self.elements.append(element)
        self.feedback.save()
        return element

    def add_extra_scenario(self):
        return ScenarioFactory(judging_round=self.judging_round)

    def add_panel(self):
        return PanelFactory(
            panel_time__judging_round=self.judging_round,
            panel_type__judging_round=self.judging_round,
            location__judging_round=self.judging_round)

    def add_assignment(self,
                       judge=None,
                       panel=None,
                       scenario=None):
        scenario = scenario or self.scenario
        judge = judge or self.judge
        panel = panel or self.panel
        return JudgePanelAssignmentFactory(
            judge=judge,
            panel=panel,
            scenario=scenario)

    def add_feedback(self,
                     application=None,
                     judge=None,
                     panel=None):
        judge = judge or self.judge
        application = application or self.application
        panel = panel or self.panel
        if not panel.applicationpanelassignment_set.filter(
                application=application).exists():
            ApplicationPanelAssignmentFactory(
                application=application,
                panel=panel,
                scenario=self.scenario)
        return JudgeApplicationFeedbackFactory(
            judge=judge,
            application=application,
            panel=panel,
            form_type=self.judging_round.judging_form)

    def add_application(self,
                        application=None,
                        field=None,
                        option=None,
                        program=None):
        program = program or self.program
        if application is None:
            fields = {
                "application_status": SUBMITTED_APP_STATUS,
                "application_type": self.application_type,
            }
            if field:
                fields[field] = option
            application = ApplicationFactory(**fields)
        self.applications.append(application)
        startup = application.startup
        cycle_interest = StartupCycleInterestFactory(cycle=program.cycle,
                                                     startup=startup)
        StartupProgramInterestFactory(program=program,
                                      startup=startup,
                                      startup_cycle_interest=cycle_interest,
                                      applying=True)

    def add_applications(self, count, field=None, options=[], programs=[]):
        result = []
        option_count = len(options)
        option = None
        program_count = len(programs)
        program = None
        for i in range(count):
            if option_count > 0:
                option = options[i % option_count]
            if program_count > 0:
                program = programs[i % program_count]
            result.append(self.add_application(field=field,
                                               option=option,
                                               program=program))
        return result

    def add_judge(self,
                  assigned=True,
                  complete=True,
                  judge=None,
                  panel=None,
                  capacity=10):
        if judge is None:
            judge = ExpertFactory(
                profile__primary_industry=self.industry,
                profile__home_program_family=self.program.program_family)
        ProgramRoleGrantFactory(person=judge, program_role=self.judge_role)
        self.judging_round.confirmed_judge_label.users.add(judge)
        JudgeRoundCommitmentFactory(judging_round=self.judging_round,
                                    judge=judge,
                                    capacity=10,
                                    commitment_state=True)
        self.judging_capacity += capacity
        if assigned:
            if complete:
                status = COMPLETE_PANEL_ASSIGNMENT_STATUS
            else:
                status = ASSIGNED_PANEL_ASSIGNMENT_STATUS
            JudgePanelAssignmentFactory(
                judge=judge,
                assignment_status=status,
                panel=panel or self.panel,
                scenario=self.scenario)
        self.judges.append(judge)
        return judge

    @classmethod
    def create_batch(cls, qty, *args, **kwargs):
        if 'merge_feedback' in kwargs:
            merge_feedback = kwargs.pop('merge_feedback')
        else:
            merge_feedback = False
        contexts = [cls(*args, **kwargs)]
        if merge_feedback:
            kwargs['merge_feedback_with'] = contexts[0].judging_round
        for _ in range(1, qty):
            contexts.append(cls(*args, **kwargs))
        return contexts
