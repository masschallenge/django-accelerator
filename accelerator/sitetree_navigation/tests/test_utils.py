from django.test import TestCase

from accelerator.tests.factories import (
    UserRoleFactory,
    ProgramFactory,
    ProgramFamilyFactory
)
from accelerator.sitetree_navigation.utils import (
    create_items,
    add_user_roles_to_nav_items,
    add_allowed_programs_to_nav_items,
    add_allowed_program_families_to_nav_items,
    delete_nav_tree
)
from accelerator_abstract.models import BaseUserRole
from mc.models import (
    NavTree,
    NavTreeItem
)

FINALIST = BaseUserRole.FINALIST
ALUMNI = BaseUserRole.ALUM
MENTOR = BaseUserRole.MENTOR

TEST_TREE = {
    "title": 'Test SubNav',
    "alias": 'test_subnav'
}

TEST_ITEMS = [
    {
        "title": 'Kenya',
        "url": '/nairobi',
        "alias": 'ke_alias',
        "user_roles": [MENTOR]
    }, {
        "title": 'Uganda',
        "url": '/kampala',
        "user_roles": [FINALIST, ALUMNI, MENTOR],
        "alias": 'ug_alias',
    }
]


class TestSitetreeUtils(TestCase):

    def setUp(self):
        self.tree = NavTree.objects.create(**TEST_TREE)
        self.programs = ProgramFactory.create_batch(5)
        self.program_families = ProgramFamilyFactory.create_batch(5)

        for item in TEST_ITEMS:
            item['programs'] = [self.programs[0].id]
            item['program_families'] = [self.program_families[0].id]

        for role in [FINALIST, ALUMNI, MENTOR]:
            UserRoleFactory(name=role)

    def tearDown(self):
        self.tree.delete()

    def test_create_items_creates_non_existent_objects(self):
        create_items(self.tree, TEST_ITEMS)

        for item in TEST_ITEMS:
            self.assertTrue(NavTreeItem.objects.filter(
                alias=item['alias']).exists())

    def test_create_items_updates_existenting_objects(self):
        create_items(self.tree, TEST_ITEMS)
        for item in TEST_ITEMS:
            item['title'] = item['title'] + "blah"
        create_items(self.tree, TEST_ITEMS)
        for item in TEST_ITEMS:
            self.assertTrue("blah" in NavTreeItem.objects.filter(
                alias=item['alias']).first().title)

    def test_add_user_roles_to_nav_items(self):
        create_items(self.tree, TEST_ITEMS)
        add_user_roles_to_nav_items(TEST_ITEMS)

        for item in TEST_ITEMS:
            user_roles = NavTreeItem.objects.filter(
                alias=item['alias']).first().user_role.all()
            self.assertTrue(len(user_roles) == len(item['user_roles']))
            for user_role in user_roles:
                self.assertTrue(user_role.name in item['user_roles'])

    def test_add_user_roles_to_nav_items_updates_existing_objects(self):
        create_items(self.tree, TEST_ITEMS)
        add_user_roles_to_nav_items(TEST_ITEMS)

        for item in TEST_ITEMS:
            item['user_roles'] = [FINALIST, ALUMNI]
        add_user_roles_to_nav_items(TEST_ITEMS)

        for item in TEST_ITEMS:
            user_roles = NavTreeItem.objects.filter(
                alias=item['alias']).first().user_role.all()
            self.assertTrue(len(user_roles) == len(item['user_roles']))
            for user_role in user_roles:
                self.assertTrue(user_role.name in item['user_roles'])

    def test_add_allowed_programs_to_nav_items(self):
        create_items(self.tree, TEST_ITEMS)
        add_allowed_programs_to_nav_items(TEST_ITEMS)
        self._add_allowed_programs_to_nav_items_assertions

    def test_add_allowed_program_to_nav_items_updates_existing_objects(self):
        create_items(self.tree, TEST_ITEMS)
        add_allowed_programs_to_nav_items(TEST_ITEMS)

        for item in TEST_ITEMS:
            item['programs'] = [program.id for program in self.programs[1:]]
        add_allowed_programs_to_nav_items(TEST_ITEMS)
        self._add_allowed_programs_to_nav_items_assertions

    def test_add_programs_does_nothing(self):
        create_items(self.tree, TEST_ITEMS)
        add_allowed_programs_to_nav_items(TEST_ITEMS)
        programs_before = []
        for item in TEST_ITEMS:
            programs = NavTreeItem.objects.filter(
                alias=item['alias']).first().program.all()
            programs_before.append(
                {
                    'alias': item['alias'],
                    'programs': programs
                })
        for item in TEST_ITEMS:
            item.pop('programs', None)
        add_allowed_programs_to_nav_items(TEST_ITEMS)

        for program in programs_before:
            programs = NavTreeItem.objects.filter(
                alias=program['alias']).first().program.all()
            self.assertEqual(list(program['programs']), list(programs))

    def test_add_allowed_program_families_to_nav_items(self):
        create_items(self.tree, TEST_ITEMS)
        add_allowed_program_families_to_nav_items(TEST_ITEMS)
        self._add_allowed_program_families_to_nav_items_assertions()

    def test_add_allowed_program_families_to_nav_items_update_existing(self):
        create_items(self.tree, TEST_ITEMS)
        add_allowed_program_families_to_nav_items(TEST_ITEMS)

        for item in TEST_ITEMS:
            item['program_families'] = [
                family.id for family in self.program_families[1:]]
        add_allowed_program_families_to_nav_items(TEST_ITEMS)
        self._add_allowed_program_families_to_nav_items_assertions()

    def test_add_empty_families_does_nothing(self):
        create_items(self.tree, TEST_ITEMS)
        add_allowed_program_families_to_nav_items(TEST_ITEMS)
        families_before = []
        for item in TEST_ITEMS:
            program_families = NavTreeItem.objects.filter(
                alias=item['alias']).first().program_family.all()
            families_before.append(
                {
                    'alias': item['alias'],
                    'families': program_families
                })
        for item in TEST_ITEMS:
            item.pop('program_families', None)
        add_allowed_program_families_to_nav_items(TEST_ITEMS)

        for family in families_before:
            program_families = NavTreeItem.objects.filter(
                alias=family['alias']).first().program_family.all()
            self.assertEqual(list(family['families']), list(program_families))

    def test_delete_nav_tree_also_deletes_related_objects(self):
        create_items(self.tree, TEST_ITEMS)
        delete_nav_tree(TEST_TREE)
        self.assertEqual(
            0,
            NavTree.objects.filter(alias=TEST_TREE['alias']).count())
        self.assertEqual(
            0,
            NavTreeItem.objects.filter(tree=self.tree).count())

    def _add_allowed_programs_to_nav_items_assertions(self):
        for item in TEST_ITEMS:
            programs = NavTreeItem.objects.filter(
                alias=item['alias']).first().program.all()
            self.assertTrue(len(programs) == len(item['programs']))
            for program in programs:
                self.assertTrue(program.id in item['programs'])

    def _add_allowed_program_families_to_nav_items_assertions(self):
        for item in TEST_ITEMS:
            program_families = NavTreeItem.objects.filter(
                alias=item['alias']).first().program_family.all()
            self.assertTrue(
                len(program_families) == len(item['program_families']))
            for program_family in program_families:
                self.assertTrue(program_family.id in item['program_families'])
