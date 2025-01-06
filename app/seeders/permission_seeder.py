from sqlalchemy.ext.asyncio import AsyncSession

from app.entities import PermissionModel
from app.infrastructure.db_constants import AppTableNames
from app.infrastructure.permission_constants import PermissionConstants
from app.seeders.base_seeder import BaseSeeder


class PermissionSeeder(BaseSeeder):

    async def seed(self, session: AsyncSession):
        permissions = self.get_data()
        await self.load_seeders(
            PermissionModel, session, AppTableNames.PermissionTableName, permissions
        )

    def get_dev_data(self):
        return [
            PermissionModel(
                title_kk="Рұқсатты жасау",
                title_ru="Создание прав",
                title_en="Create permission",
                description="Create permission",
                value=PermissionConstants.CREATE_PERMISSION_VALUE
            ),
            PermissionModel(
                title_kk="Рұқсатты жаңарту",
                title_ru="Обновление прав",
                title_en="Update permission",
                description="Update permission",
                value=PermissionConstants.UPDATE_PERMISSION_VALUE
            ),
            PermissionModel(
                title_kk="Рұқсатты жою",
                title_ru="Удаление прав",
                title_en="Delete permission",
                description="Delete permission",
                value=PermissionConstants.DELETE_PERMISSION_VALUE
            ),
            PermissionModel(
                title_kk="Рұқсатты оқу",
                title_ru="Чтение прав",
                title_en="Read permission",
                description="Read permission",
                value=PermissionConstants.READ_PERMISSION_VALUE
            ),
            PermissionModel(
                title_kk="Рөль жасау",
                title_ru="Создание роли",
                title_en="Create role",
                description="Create role",
                value=PermissionConstants.CREATE_ROLE_VALUE
            ),
            PermissionModel(
                title_kk="Рөль жаңарту",
                title_ru="Обновление роли",
                title_en="Update role",
                description="Update role",
                value=PermissionConstants.UPDATE_ROLE_VALUE
            ),
            PermissionModel(
                title_kk="Рөль жою",
                title_ru="Удаление роли",
                title_en="Delete role",
                description="Delete role",
                value=PermissionConstants.DELETE_ROLE_VALUE
            ),
            PermissionModel(
                title_kk="Рөль оқу",
                title_ru="Чтение роли",
                title_en="Read role",
                description="Read role",
                value=PermissionConstants.READ_ROLE_VALUE
            ),
            PermissionModel(
                title_kk="Курстың категориясын оқу",
                title_ru="Чтение категории курса",
                title_en="Read course category",
                description="Read course category",
                value=PermissionConstants.READ_COURSE_CATEGORY_VALUE
            ),
            PermissionModel(
                title_kk="Курстың категориясын жасау",
                title_ru="Создание категории курса",
                title_en="Create course category",
                description="Create course category",
                value=PermissionConstants.CREATE_COURSE_CATEGORY_VALUE
            ),
            PermissionModel(
                title_kk="Курстың категориясын жаңарту",
                title_ru="Обновление категории курса",
                title_en="Update course category",
                description="Update course category",
                value=PermissionConstants.UPDATE_COURSE_CATEGORY_VALUE
            ),
            PermissionModel(
                title_kk="Курстың категориясын жою",
                title_ru="Удаление категории курса",
                title_en="Delete course category",
                description="Delete course category",
                value=PermissionConstants.DELETE_COURSE_CATEGORY_VALUE
            ),
            PermissionModel(
                title_kk="Курстың типін оқу",
                title_ru="Чтение тип курса",
                title_en="Read course type",
                description="Read course type",
                value=PermissionConstants.READ_COURSE_TYPE_VALUE
            ),
            PermissionModel(
                title_kk="Курстың типін жасау",
                title_ru="Создание тип курса",
                title_en="Create course type",
                description="Create course type",
                value=PermissionConstants.CREATE_COURSE_TYPE_VALUE
            ),
            PermissionModel(
                title_kk="Курстың типін жаңарту",
                title_ru="Обновление тип курса",
                title_en="Update course type",
                description="Update course type",
                value=PermissionConstants.UPDATE_COURSE_TYPE_VALUE
            ),
            PermissionModel(
                title_kk="Курстың типін жою",
                title_ru="Удаление тип курса",
                title_en="Delete course type",
                description="Delete course type",
                value=PermissionConstants.DELETE_COURSE_TYPE_VALUE
            ),
            PermissionModel(
                title_kk="Курстың тегін оқу",
                title_ru="Чтение тега курса",
                title_en="Read course tag",
                description="Read course tag",
                value=PermissionConstants.READ_TAG_VALUE
            ),
            PermissionModel(
                title_kk="Курстың тегін жасау",
                title_ru="Создание тега курса",
                title_en="Create course tag",
                description="Create course tag",
                value=PermissionConstants.CREATE_TAG_VALUE
            ),
            PermissionModel(
                title_kk="Курстың тегін жаңарту",
                title_ru="Обновление тега курса",
                title_en="Update course tag",
                description="Update course tag",
                value=PermissionConstants.UPDATE_TAG_VALUE
            ),
            PermissionModel(
                title_kk="Курстың тегін жою",
                title_ru="Удаление тега курса",
                title_en="Delete course tag",
                description="Delete course tag",
                value=PermissionConstants.DELETE_TAG_VALUE
            ),
            PermissionModel(
                title_kk="Курсты оқу",
                title_ru="Чтение курса",
                title_en="Read course",
                description="Read course",
                value=PermissionConstants.READ_COURSE_VALUE
            ),
            PermissionModel(
                title_kk="Курсты жасау",
                title_ru="Создание курса",
                title_en="Create course",
                description="Create course",
                value=PermissionConstants.CREATE_COURSE_VALUE
            ),
            PermissionModel(
                title_kk="Курсты жаңарту",
                title_ru="Обновление курса",
                title_en="Update course",
                description="Update course",
                value=PermissionConstants.UPDATE_COURSE_VALUE
            ),
            PermissionModel(
                title_kk="Курсты жою",
                title_ru="Удаление курса",
                title_en="Delete course",
                description="Delete course",
                value=PermissionConstants.DELETE_COURSE_VALUE
            ),
            PermissionModel(
                title_kk="Қолданушыны оқу",
                title_ru="Чтение пользователя",
                title_en="Read user",
                description="Read user",
                value=PermissionConstants.READ_USER_VALUE
            ),
            PermissionModel(
                title_kk="Қолданушыны жасау",
                title_ru="Создание пользователя",
                title_en="Create user",
                description="Create user",
                value=PermissionConstants.CREATE_USER_VALUE
            ),
            PermissionModel(
                title_kk="Қолданушыны жаңарту",
                title_ru="Обновление пользователя",
                title_en="Update user",
                description="Update user",
                value=PermissionConstants.UPDATE_USER_VALUE
            ),
            PermissionModel(
                title_kk="Қолданушыны жою",
                title_ru="Удаление пользователя",
                title_en="Delete user",
                description="Delete user",
                value=PermissionConstants.DELETE_USER_VALUE
            ),
            PermissionModel(
                title_kk="Видеокурсты оқу",
                title_ru="Чтение видеокурса",
                title_en="Read video course",
                description="Read video course",
                value=PermissionConstants.READ_VIDEO_COURSE_VALUE
            ),
            PermissionModel(
                title_kk="Видеокурсты жасау",
                title_ru="Создание видеокурса",
                title_en="Create video course",
                description="Create video course",
                value=PermissionConstants.CREATE_VIDEO_COURSE_VALUE
            ),
            PermissionModel(
                title_kk="Видеокурсты жаңарту",
                title_ru="Обновление видеокурса",
                title_en="Update video course",
                description="Update video course",
                value=PermissionConstants.UPDATE_VIDEO_COURSE_VALUE
            ),
            PermissionModel(
                title_kk="Видеокурсты жою",
                title_ru="Удаление видеокурса",
                title_en="Delete video course",
                description="Delete video course",
                value=PermissionConstants.DELETE_VIDEO_COURSE_VALUE
            ),
            PermissionModel(
                title_kk="Материалды оқу",
                title_ru="Чтение материала",
                title_en="Read material",
                description="Read material",
                value=PermissionConstants.READ_MATERIAL_VALUE
            ),
            PermissionModel(
                title_kk="Материалды жасау",
                title_ru="Создание материала",
                title_en="Create material",
                description="Create material",
                value=PermissionConstants.CREATE_MATERIAL_VALUE
            ),
            PermissionModel(
                title_kk="Материалды жаңарту",
                title_ru="Обновление материала",
                title_en="Update material",
                description="Update material",
                value=PermissionConstants.UPDATE_MATERIAL_VALUE
            ),
            PermissionModel(
                title_kk="Материалды жою",
                title_ru="Удаление материала",
                title_en="Delete material",
                description="Delete material",
                value=PermissionConstants.DELETE_MATERIAL_VALUE
            ),
            PermissionModel(
                title_kk="Курстың материалын оқу",
                title_ru="Чтение материала курса",
                title_en="Read course material",
                description="Read course material",
                value=PermissionConstants.READ_COURSE_MATERIAL_VALUE
            ),
            PermissionModel(
                title_kk="Курстың материалын жасау",
                title_ru="Создание материала курса",
                title_en="Create course material",
                description="Create course material",
                value=PermissionConstants.CREATE_COURSE_MATERIAL_VALUE
            ),
            PermissionModel(
                title_kk="Курстың материалын жаңарту",
                title_ru="Обновление материала курса",
                title_en="Update course material",
                description="Update course material",
                value=PermissionConstants.UPDATE_COURSE_MATERIAL_VALUE
            ),
            PermissionModel(
                title_kk="Курстың материалын жою",
                title_ru="Удаление материала курса",
                title_en="Delete course material",
                description="Delete course material",
                value=PermissionConstants.DELETE_COURSE_MATERIAL_VALUE
            ),
            PermissionModel(
                title_kk="Видеокурстың материалын оқу",
                title_ru="Чтение материала видеокурса",
                title_en="Read video course material",
                description="Read video course material",
                value=PermissionConstants.READ_VIDEO_MATERIAL_VALUE
            ),
            PermissionModel(
                title_kk="Видеокурстың материалын жасау",
                title_ru="Создание материала видеокурса",
                title_en="Create video course material",
                description="Create video course material",
                value=PermissionConstants.CREATE_VIDEO_MATERIAL_VALUE
            ),
            PermissionModel(
                title_kk="Видеокурстың материалын жаңарту",
                title_ru="Обновление материала видеокурса",
                title_en="Update video course material",
                description="Update video course material",
                value=PermissionConstants.UPDATE_VIDEO_MATERIAL_VALUE
            ),
            PermissionModel(
                title_kk="Видеокурстың материалын жою",
                title_ru="Удаление материала видеокурса",
                title_en="Delete video course material",
                description="Delete video course material",
                value=PermissionConstants.DELETE_VIDEO_MATERIAL_VALUE
            ),
            PermissionModel(
                title_kk="Организацияны оқу",
                title_ru="Чтение организации",
                title_en="Read organization",
                description="Read organization",
                value=PermissionConstants.READ_ORGANIZATION_VALUE
            ),
            PermissionModel(
                title_kk="Организацияны жасау",
                title_ru="Создание организации",
                title_en="Create organization",
                description="Create organization",
                value=PermissionConstants.CREATE_ORGANIZATION_VALUE
            ),
            PermissionModel(
                title_kk="Организацияны жаңарту",
                title_ru="Обновление организации",
                title_en="Update organization",
                description="Update organization",
                value=PermissionConstants.UPDATE_ORGANIZATION_VALUE
            ),
            PermissionModel(
                title_kk="Организацияны жою",
                title_ru="Удаление организации",
                title_en="Delete organization",
                description="Delete organization",
                value=PermissionConstants.DELETE_ORGANIZATION_VALUE
            ),
            PermissionModel(
                title_kk="Тестті оқу",
                title_ru="Чтение тестов",
                title_en="Read test",
                description="Read test",
                value=PermissionConstants.READ_TEST_VALUE
            ),
            PermissionModel(
                title_kk="Тестті жасау",
                title_ru="Создание тестов",
                title_en="Create test",
                description="Create test",
                value=PermissionConstants.CREATE_TEST_VALUE
            ),
            PermissionModel(
                title_kk="Тестті жаңарту",
                title_ru="Обновление тестов",
                title_en="Update test",
                description="Update test",
                value=PermissionConstants.UPDATE_TEST_VALUE
            ),
            PermissionModel(
                title_kk="Тестті жою",
                title_ru="Удаление тестов",
                title_en="Delete test",
                description="Delete test",
                value=PermissionConstants.DELETE_TEST_VALUE
            ),
            PermissionModel(
                title_kk="Сұрақты оқу",
                title_ru="Чтение вопросов",
                title_en="Read question",
                description="Read question",
                value=PermissionConstants.READ_QUESTION_VALUE
            ),
            PermissionModel(
                title_kk="Сұрақты жасау",
                title_ru="Создание вопросов",
                title_en="Create question",
                description="Create question",
                value=PermissionConstants.CREATE_QUESTION_VALUE
            ),
            PermissionModel(
                title_kk="Сұрақты жаңарту",
                title_ru="Обновление вопросов",
                title_en="Update question",
                description="Update question",
                value=PermissionConstants.UPDATE_QUESTION_VALUE
            ),
            PermissionModel(
                title_kk="Сұрақты жою",
                title_ru="Удаление вопросов",
                title_en="Delete question",
                description="Delete question",
                value=PermissionConstants.DELETE_QUESTION_VALUE
            ),
            PermissionModel(
                title_kk="Мінезді оқу",
                title_ru="Чтение характеристики",
                title_en="Read characteristic",
                description="Read characteristic",
                value=PermissionConstants.READ_CHARACTERISTIC_VALUE
            ),
            PermissionModel(
                title_kk="Мінезді жасау",
                title_ru="Создание характеристики",
                title_en="Create characteristic",
                description="Create characteristic",
                value=PermissionConstants.CREATE_CHARACTERISTIC_VALUE
            ),
            PermissionModel(
                title_kk="Мінезді жаңарту",
                title_ru="Обновление характеристики",
                title_en="Update characteristic",
                description="Update characteristic",
                value=PermissionConstants.UPDATE_CHARACTERISTIC_VALUE
            ),
            PermissionModel(
                title_kk="Мінезді жою",
                title_ru="Удаление характеристики",
                title_en="Delete characteristic",
                description="Delete characteristic",
                value=PermissionConstants.DELETE_CHARACTERISTIC_VALUE
            ),
            PermissionModel(
                title_kk="Жауапты оқу",
                title_ru="Чтение ответов",
                title_en="Read answer",
                description="Read answer",
                value=PermissionConstants.READ_ANSWER_VALUE
            ),
            PermissionModel(
                title_kk="Жауапты жасау",
                title_ru="Создание ответов",
                title_en="Create answer",
                description="Create answer",
                value=PermissionConstants.CREATE_ANSWER_VALUE
            ),
            PermissionModel(
                title_kk="Жауапты жаңарту",
                title_ru="Обновление ответов",
                title_en="Update answer",
                description="Update answer",
                value=PermissionConstants.UPDATE_ANSWER_VALUE
            ),
            PermissionModel(
                title_kk="Жауапты жою",
                title_ru="Удаление ответов",
                title_en="Delete answer",
                description="Delete answer",
                value=PermissionConstants.DELETE_ANSWER_VALUE
            ),
            PermissionModel(
                title_kk="Өтінішті оқу",
                title_ru="Чтение обращении",
                title_en="Read feedback",
                description="Read feedback",
                value=PermissionConstants.READ_FEEDBACK_VALUE
            ),
            PermissionModel(
                title_kk="Өтінішті жасау",
                title_ru="Создание обращении",
                title_en="Create feedback",
                description="Create feedback",
                value=PermissionConstants.CREATE_FEEDBACK_VALUE
            ),
            PermissionModel(
                title_kk="Өтінішті жаңарту",
                title_ru="Обновление обращении",
                title_en="Update feedback",
                description="Update feedback",
                value=PermissionConstants.UPDATE_FEEDBACK_VALUE
            ),
            PermissionModel(
                title_kk="Өтінішті жою",
                title_ru="Удаление обращении",
                title_en="Delete feedback",
                description="Delete feedback",
                value=PermissionConstants.DELETE_FEEDBACK_VALUE
            ),
            PermissionModel(
                title_kk="Блогтың категориясын оқу",
                title_ru="Чтение категории блога",
                title_en="Read blog category",
                description="Read blog category",
                value=PermissionConstants.READ_BLOG_CATEGORY_VALUE
            ),
            PermissionModel(
                title_kk="Блогтың категориясын жасау",
                title_ru="Создание категории блога",
                title_en="Create blog category",
                description="Create blog category",
                value=PermissionConstants.CREATE_BLOG_CATEGORY_VALUE
            ),
            PermissionModel(
                title_kk="Блогтың категориясын жаңарту",
                title_ru="Обновление категории блога",
                title_en="Update blog category",
                description="Update blog category",
                value=PermissionConstants.UPDATE_BLOG_CATEGORY_VALUE
            ),
            PermissionModel(
                title_kk="Блогтың категориясын жою",
                title_ru="Удаление категории блога",
                title_en="Delete blog category",
                description="Delete blog category",
                value=PermissionConstants.DELETE_BLOG_CATEGORY_VALUE
            ),
            PermissionModel(
                title_kk="Блогты оқу",
                title_ru="Чтение блога",
                title_en="Read blog",
                description="Read blog",
                value=PermissionConstants.READ_BLOG_VALUE
            ),
            PermissionModel(
                title_kk="Блогты жасау",
                title_ru="Создание блога",
                title_en="Create blog",
                description="Create blog",
                value=PermissionConstants.CREATE_BLOG_VALUE
            ),
            PermissionModel(
                title_kk="Блогты жаңарту",
                title_ru="Обновление блога",
                title_en="Update blog",
                description="Update blog",
                value=PermissionConstants.UPDATE_BLOG_VALUE
            ),
            PermissionModel(
                title_kk="Блогты жою",
                title_ru="Удаление блога",
                title_en="Delete blog",
                description="Delete blog",
                value=PermissionConstants.DELETE_BLOG_VALUE
            )
        ]

    def get_prod_data(self):
        return self.get_dev_data()
