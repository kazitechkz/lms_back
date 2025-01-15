from typing import Generic, TypeVar

from pydantic import BaseModel

from app.adapters.dto.blog.blog_dto import BlogRDTOWithRelated
from app.adapters.dto.characteristic.characteristic_dto import CharacteristicRDTO
from app.adapters.dto.course.course_dto import CourseRDTOWithRelated
from app.adapters.dto.feedback.feedback_dto import FeedbackRDTOWithRelated
from app.adapters.dto.organization.organization_dto import OrganizationRDTOWithRelated
from app.adapters.dto.question.question_dto import QuestionRDTOWithRelated
from app.adapters.dto.test.test_dto import TestRDTO
from app.adapters.dto.user.user_dto import UserRDTOWithRelated
from app.adapters.dto.video_course.video_course_dto import VideoCourseRDTOWithRelated

T = TypeVar("T")


class Pagination(Generic[T]):
    current_page: int
    per_page: int
    last_page: int
    total_pages: int
    total_items: int
    items: list[T]

    def __init__(
            self,
            items: list[T],
            total_pages: int,
            total_items: int,
            per_page: int,
            page: int,
    ) -> None:
        self.items = items
        self.total_pages = total_pages
        self.total_items = total_items
        self.current_page = page
        self.per_page = per_page
        self.last_page = (total_pages + per_page - 1) // per_page


class BasePageModel(BaseModel):
    current_page: int
    per_page: int
    last_page: int
    total_pages: int
    total_items: int


class PaginationCourse(BasePageModel):
    items: list[CourseRDTOWithRelated]


class PaginationUsers(BasePageModel):
    items: list[UserRDTOWithRelated]


class PaginationVideoCourses(BasePageModel):
    items: list[VideoCourseRDTOWithRelated]


class PaginationOrganizations(BasePageModel):
    items: list[OrganizationRDTOWithRelated]


class PaginationTests(BasePageModel):
    items: list[TestRDTO]


class PaginationQuestions(BasePageModel):
    items: list[QuestionRDTOWithRelated]


class PaginationCharacteristics(BasePageModel):
    items: list[CharacteristicRDTO]


class PaginationFeedbacks(BasePageModel):
    items: list[FeedbackRDTOWithRelated]


class PaginationBlogs(BasePageModel):
    items: list[BlogRDTOWithRelated]
