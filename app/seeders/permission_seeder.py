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
            )
        ]

    def get_prod_data(self):
        return self.get_dev_data()
