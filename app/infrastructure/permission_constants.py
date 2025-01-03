class PermissionConstants:
    # permission permissions
    READ_PERMISSION_VALUE = "read_permission_value"
    CREATE_PERMISSION_VALUE = "create_permission_value"
    UPDATE_PERMISSION_VALUE = "update_permission_value"
    DELETE_PERMISSION_VALUE = "delete_permission_value"

    # role permissions
    READ_ROLE_VALUE = "read_role_value"
    CREATE_ROLE_VALUE = "create_role_value"
    UPDATE_ROLE_VALUE = "update_role_value"
    DELETE_ROLE_VALUE = "delete_role_value"

    # course type permissions
    READ_COURSE_TYPE_VALUE = "read_course_type_value"
    CREATE_COURSE_TYPE_VALUE = "create_course_type_value"
    UPDATE_COURSE_TYPE_VALUE = "update_course_type_value"
    DELETE_COURSE_TYPE_VALUE = "delete_course_type_value"

    # course category permissions
    READ_COURSE_CATEGORY_VALUE = "read_course_category_value"
    CREATE_COURSE_CATEGORY_VALUE = "create_course_category_value"
    UPDATE_COURSE_CATEGORY_VALUE = "update_course_category_value"
    DELETE_COURSE_CATEGORY_VALUE = "delete_course_category_value"

    # course permissions
    READ_COURSE_VALUE = "read_course_value"
    CREATE_COURSE_VALUE = "create_course_value"
    UPDATE_COURSE_VALUE = "update_course_value"
    DELETE_COURSE_VALUE = "delete_course_value"

    # tag permissions
    READ_TAG_VALUE = "read_tag_value"
    CREATE_TAG_VALUE = "create_tag_value"
    UPDATE_TAG_VALUE = "update_tag_value"
    DELETE_TAG_VALUE = "delete_tag_value"

    # user permissions
    READ_USER_VALUE = "read_user_value"
    CREATE_USER_VALUE = "create_user_value"
    UPDATE_USER_VALUE = "update_user_value"
    DELETE_USER_VALUE = "delete_user_value"

    # user permissions
    READ_VIDEO_COURSE_VALUE = "read_video_course_value"
    CREATE_VIDEO_COURSE_VALUE = "create_video_course_value"
    UPDATE_VIDEO_COURSE_VALUE = "update_video_course_value"
    DELETE_VIDEO_COURSE_VALUE = "delete_video_course_value"

    # material permissions
    READ_MATERIAL_VALUE = "read_material_value"
    CREATE_MATERIAL_VALUE = "create_material_value"
    UPDATE_MATERIAL_VALUE = "update_material_value"
    DELETE_MATERIAL_VALUE = "delete_material_value"

    # course material permissions
    READ_COURSE_MATERIAL_VALUE = "read_course_material_value"
    CREATE_COURSE_MATERIAL_VALUE = "create_course_material_value"
    UPDATE_COURSE_MATERIAL_VALUE = "update_course_material_value"
    DELETE_COURSE_MATERIAL_VALUE = "delete_course_material_value"

    # video material permissions
    READ_VIDEO_MATERIAL_VALUE = "read_video_material_value"
    CREATE_VIDEO_MATERIAL_VALUE = "create_video_material_value"
    UPDATE_VIDEO_MATERIAL_VALUE = "update_video_material_value"
    DELETE_VIDEO_MATERIAL_VALUE = "delete_video_material_value"

    # organization permissions
    READ_ORGANIZATION_VALUE = "read_organization_value"
    CREATE_ORGANIZATION_VALUE = "create_organization_value"
    UPDATE_ORGANIZATION_VALUE = "update_organization_value"
    DELETE_ORGANIZATION_VALUE = "delete_organization_value"

    # PERMISSIONS, которые нельзя удалить или изменить
    IMMUTABLE_PERMISSIONS = frozenset(
        [
            READ_PERMISSION_VALUE,
            CREATE_PERMISSION_VALUE,
            UPDATE_PERMISSION_VALUE,
            DELETE_PERMISSION_VALUE,
            READ_ROLE_VALUE,
            CREATE_ROLE_VALUE,
            UPDATE_ROLE_VALUE,
            DELETE_ROLE_VALUE,
            READ_COURSE_TYPE_VALUE,
            CREATE_COURSE_TYPE_VALUE,
            UPDATE_COURSE_TYPE_VALUE,
            DELETE_COURSE_TYPE_VALUE,
            READ_COURSE_CATEGORY_VALUE,
            CREATE_COURSE_CATEGORY_VALUE,
            UPDATE_COURSE_CATEGORY_VALUE,
            DELETE_COURSE_CATEGORY_VALUE,
            READ_COURSE_VALUE,
            CREATE_COURSE_VALUE,
            UPDATE_COURSE_VALUE,
            DELETE_COURSE_VALUE,
            READ_TAG_VALUE,
            CREATE_TAG_VALUE,
            UPDATE_TAG_VALUE,
            DELETE_TAG_VALUE,
            READ_USER_VALUE,
            CREATE_USER_VALUE,
            UPDATE_USER_VALUE,
            DELETE_USER_VALUE,
            READ_VIDEO_COURSE_VALUE,
            CREATE_VIDEO_COURSE_VALUE,
            UPDATE_VIDEO_COURSE_VALUE,
            DELETE_VIDEO_COURSE_VALUE,
            READ_MATERIAL_VALUE,
            CREATE_MATERIAL_VALUE,
            UPDATE_MATERIAL_VALUE,
            DELETE_MATERIAL_VALUE,
            READ_COURSE_MATERIAL_VALUE,
            CREATE_COURSE_MATERIAL_VALUE,
            UPDATE_COURSE_MATERIAL_VALUE,
            DELETE_COURSE_MATERIAL_VALUE,
            READ_VIDEO_MATERIAL_VALUE,
            CREATE_VIDEO_MATERIAL_VALUE,
            UPDATE_VIDEO_MATERIAL_VALUE,
            DELETE_VIDEO_MATERIAL_VALUE,
            READ_ORGANIZATION_VALUE,
            CREATE_ORGANIZATION_VALUE,
            UPDATE_ORGANIZATION_VALUE,
            DELETE_ORGANIZATION_VALUE,
        ]
    )
