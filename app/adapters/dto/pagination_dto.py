from typing import Generic, TypeVar

T = TypeVar("T")


class Pagination(Generic[T]):
    current_page: int
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
        self.last_page = (total_pages + per_page - 1) // per_page
