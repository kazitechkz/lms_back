from app.seeders.course_type_seeder import CourseTypeSeeder
from app.seeders.language_seeder import LanguageSeeder
from app.seeders.organization_type_seeder import OrganizationTypeSeeder
from app.seeders.permission_seeder import PermissionSeeder
from app.seeders.question_type_seeder import QuestionTypeSeeder
from app.seeders.role_permission_seeder import RolePermissionSeeder
from app.seeders.role_seeder import RoleSeeder
from app.seeders.test_type_seeder import TestTypeSeeder
from app.seeders.user_seeder import UserSeeder
from app.seeders.user_type_seeder import UserTypeSeeder

seeders = [
    RoleSeeder(),
    PermissionSeeder(),
    RolePermissionSeeder(),
    LanguageSeeder(),
    UserTypeSeeder(),
    OrganizationTypeSeeder(),
    CourseTypeSeeder(),
    UserSeeder(),
    TestTypeSeeder(),
    QuestionTypeSeeder(),
]
