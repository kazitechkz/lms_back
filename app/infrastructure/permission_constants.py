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

    # test permissions
    READ_TEST_VALUE = "read_test_value"
    CREATE_TEST_VALUE = "create_test_value"
    UPDATE_TEST_VALUE = "update_test_value"
    DELETE_TEST_VALUE = "delete_test_value"

    # question permissions
    READ_QUESTION_VALUE = "read_question_value"
    CREATE_QUESTION_VALUE = "create_question_value"
    UPDATE_QUESTION_VALUE = "update_question_value"
    DELETE_QUESTION_VALUE = "delete_question_value"

    # characteristic permissions
    READ_CHARACTERISTIC_VALUE = "read_characteristic_value"
    CREATE_CHARACTERISTIC_VALUE = "create_characteristic_value"
    UPDATE_CHARACTERISTIC_VALUE = "update_characteristic_value"
    DELETE_CHARACTERISTIC_VALUE = "delete_characteristic_value"

    # answer permissions
    READ_ANSWER_VALUE = "read_answer_value"
    CREATE_ANSWER_VALUE = "create_answer_value"
    UPDATE_ANSWER_VALUE = "update_answer_value"
    DELETE_ANSWER_VALUE = "delete_answer_value"

    # feedback permissions
    READ_FEEDBACK_VALUE = "read_feedback_value"
    CREATE_FEEDBACK_VALUE = "create_feedback_value"
    UPDATE_FEEDBACK_VALUE = "update_feedback_value"
    DELETE_FEEDBACK_VALUE = "delete_feedback_value"

    # blog_category permissions
    READ_BLOG_CATEGORY_VALUE = "read_blog_category_value"
    CREATE_BLOG_CATEGORY_VALUE = "create_blog_category_value"
    UPDATE_BLOG_CATEGORY_VALUE = "update_blog_category_value"
    DELETE_BLOG_CATEGORY_VALUE = "delete_blog_category_value"

    # blog permissions
    READ_BLOG_VALUE = "read_blog_value"
    CREATE_BLOG_VALUE = "create_blog_value"
    UPDATE_BLOG_VALUE = "update_blog_value"
    DELETE_BLOG_VALUE = "delete_blog_value"

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
            READ_QUESTION_VALUE,
            CREATE_QUESTION_VALUE,
            UPDATE_QUESTION_VALUE,
            DELETE_QUESTION_VALUE,
            READ_CHARACTERISTIC_VALUE,
            CREATE_CHARACTERISTIC_VALUE,
            UPDATE_CHARACTERISTIC_VALUE,
            DELETE_CHARACTERISTIC_VALUE,
            READ_TEST_VALUE,
            CREATE_TEST_VALUE,
            UPDATE_TEST_VALUE,
            DELETE_TEST_VALUE,
            READ_ANSWER_VALUE,
            CREATE_ANSWER_VALUE,
            UPDATE_ANSWER_VALUE,
            DELETE_ANSWER_VALUE,
            READ_FEEDBACK_VALUE,
            CREATE_FEEDBACK_VALUE,
            UPDATE_FEEDBACK_VALUE,
            DELETE_FEEDBACK_VALUE,
            READ_BLOG_CATEGORY_VALUE,
            CREATE_BLOG_CATEGORY_VALUE,
            UPDATE_BLOG_CATEGORY_VALUE,
            DELETE_BLOG_CATEGORY_VALUE,
            READ_BLOG_VALUE,
            CREATE_BLOG_VALUE,
            UPDATE_BLOG_VALUE,
            DELETE_BLOG_VALUE,
        ]
    )
