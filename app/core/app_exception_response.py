import logging

from fastapi import HTTPException, status


class AppExceptionResponse:
    """Утилита для создания стандартных HTTP-исключений."""

    logger = logging.getLogger("AppExceptionResponse")

    @staticmethod
    def create_exception(
        status_code: int, message: str, extra: dict | None = None
    ) -> HTTPException:
        """
        Создаёт HTTP-исключение с возможностью добавления дополнительных данных.

        Args:
            status_code (int): Код статуса HTTP.
            message (str): Сообщение об ошибке.
            extra (dict, optional): Дополнительные данные, которые будут включены в `detail`.

        Returns:
            HTTPException: Объект HTTP-исключения.
        """
        detail = {"message": message}
        if extra:
            detail.update(extra)

        # Логгирование ошибки
        AppExceptionResponse.logger.error(f"Error {status_code}: {detail}")

        return HTTPException(status_code=status_code, detail=detail)

    @staticmethod
    def bad_request(message: str = "Bad request", extra: dict | None = None):
        return AppExceptionResponse.create_exception(
            status_code=status.HTTP_400_BAD_REQUEST, message=message, extra=extra
        )

    @staticmethod
    def unauthorized(message: str = "Unauthorized", extra: dict | None = None):
        return AppExceptionResponse.create_exception(
            status_code=status.HTTP_401_UNAUTHORIZED, message=message, extra=extra
        )

    @staticmethod
    def forbidden(message: str = "Forbidden", extra: dict | None = None):
        return AppExceptionResponse.create_exception(
            status_code=status.HTTP_403_FORBIDDEN, message=message, extra=extra
        )

    @staticmethod
    def not_found(message: str = "Resource not found", extra: dict | None = None):
        return AppExceptionResponse.create_exception(
            status_code=status.HTTP_404_NOT_FOUND, message=message, extra=extra
        )

    @staticmethod
    def conflict(message: str = "Conflict occurred", extra: dict | None = None):
        return AppExceptionResponse.create_exception(
            status_code=status.HTTP_409_CONFLICT, message=message, extra=extra
        )

    @staticmethod
    def internal_error(
        message: str = "Internal server error", extra: dict | None = None
    ):
        return AppExceptionResponse.create_exception(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message=message,
            extra=extra,
        )
