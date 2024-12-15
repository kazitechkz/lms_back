from app.seeders.language_seeder import LanguageSeeder
from app.seeders.organization_type_seeder import OrganizationTypeSeeder
from app.seeders.role_seeder import RoleSeeder
from app.seeders.user_type_seeder import UserTypeSeeder

seeders = [
    RoleSeeder(),
    LanguageSeeder(),
    UserTypeSeeder(),
    OrganizationTypeSeeder(),
]
